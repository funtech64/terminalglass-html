/**
 * terminal.glass contact page — form rendering and Formspree submission
 */
(function () {
  "use strict";

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function renderSelectOptions(options, includePlaceholder) {
    return options
      .map(function (opt) {
        if (!includePlaceholder && opt.value === "") return "";
        return (
          '<option value="' +
          escapeHtml(opt.value) +
          '">' +
          escapeHtml(opt.label) +
          "</option>"
        );
      })
      .join("");
  }

  function getQueryParams() {
    var params = {};
    var search = window.location.search.replace(/^\?/, "");
    if (!search) return params;
    search.split("&").forEach(function (pair) {
      var parts = pair.split("=");
      params[decodeURIComponent(parts[0])] = decodeURIComponent(
        (parts[1] || "").replace(/\+/g, " ")
      );
    });
    return params;
  }

  function resolveInitialInterest() {
    var params = getQueryParams();
    if (params.package && contactUrlInterestMap[params.package]) {
      return contactUrlInterestMap[params.package];
    }
    if (params.path && contactPathInterestMap[params.path]) {
      return contactPathInterestMap[params.path];
    }
    return "";
  }

  function renderPathCards() {
    var container = document.getElementById("contact-path-cards");
    if (!container) return;

    var params = getQueryParams();
    var activePath = params.path || "";

    container.innerHTML = contactPathOptions
      .map(function (path) {
        var isActive = activePath === path.id;
        return (
          '<button type="button" class="contact-path-card' +
          (isActive ? " is-active" : "") +
          '" data-path="' +
          escapeHtml(path.id) +
          '" data-interest="' +
          escapeHtml(path.interest) +
          '" aria-pressed="' +
          (isActive ? "true" : "false") +
          '">' +
          "<strong>" +
          escapeHtml(path.title) +
          "</strong>" +
          "<span>" +
          escapeHtml(path.description) +
          "</span>" +
          "</button>"
        );
      })
      .join("");
  }

  function populateSelects() {
    var interest = document.getElementById("interest");
    var deployment = document.getElementById("preferred_deployment");
    var orgSize = document.getElementById("organization_size");

    if (interest) {
      interest.innerHTML =
        '<option value="">Select an option</option>' +
        renderSelectOptions(contactInterestOptions, false);
      var initial = resolveInitialInterest();
      if (initial) interest.value = initial;
    }

    if (deployment) {
      deployment.innerHTML = renderSelectOptions(
        contactDeploymentOptions,
        true
      );
    }

    if (orgSize) {
      orgSize.innerHTML = renderSelectOptions(contactOrganizationSizes, true);
    }
  }

  function bindPathCards() {
    var cards = document.querySelectorAll(".contact-path-card");
    var interest = document.getElementById("interest");
    if (!interest) return;

    cards.forEach(function (card) {
      card.addEventListener("click", function () {
        cards.forEach(function (c) {
          c.classList.remove("is-active");
          c.setAttribute("aria-pressed", "false");
        });
        card.classList.add("is-active");
        card.setAttribute("aria-pressed", "true");
        interest.value = card.getAttribute("data-interest") || "";
        interest.focus();
      });
    });
  }

  function showFormState(state) {
    var formWrap = document.getElementById("contact-form-wrap");
    var success = document.getElementById("contact-success");
    var error = document.getElementById("contact-error");

    if (formWrap) formWrap.hidden = state === "success";
    if (success) success.hidden = state !== "success";
    if (error) error.hidden = state !== "error";
  }

  function setSubmitting(isSubmitting) {
    var btn = document.getElementById("contact-submit");
    if (!btn) return;
    btn.disabled = isSubmitting;
    btn.textContent = isSubmitting
      ? contactFormConfig.submittingLabel
      : contactFormConfig.submitLabel;
  }

  function showFieldErrors(errors) {
    Object.keys(errors).forEach(function (field) {
      var el = document.getElementById(field);
      var msg = document.getElementById(field + "-error");
      if (msg) {
        msg.textContent = Array.isArray(errors[field])
          ? errors[field].join(" ")
          : errors[field];
        msg.hidden = false;
      }
      if (el) el.setAttribute("aria-invalid", "true");
    });
  }

  function clearFieldErrors() {
    document
      .querySelectorAll(".form-field-error")
      .forEach(function (el) {
        el.textContent = "";
        el.hidden = true;
      });
    document
      .querySelectorAll("[aria-invalid]")
      .forEach(function (el) {
        el.removeAttribute("aria-invalid");
      });
  }

  function handleSubmit(event) {
    event.preventDefault();
    clearFieldErrors();
    showFormState("form");

    var form = event.target;
    var gotcha = form.querySelector('[name="_gotcha"]');
    if (gotcha && gotcha.value) return;

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    setSubmitting(true);

    var formData = new FormData(form);

    fetch(contactFormConfig.endpoint, {
      method: "POST",
      body: formData,
      headers: {
        Accept: "application/json",
      },
    })
      .then(function (response) {
        return response.json().then(function (data) {
          return { ok: response.ok, data: data };
        });
      })
      .then(function (result) {
        setSubmitting(false);
        if (result.ok) {
          form.reset();
          populateSelects();
          document
            .querySelectorAll(".contact-path-card")
            .forEach(function (c) {
              c.classList.remove("is-active");
              c.setAttribute("aria-pressed", "false");
            });
          showFormState("success");
          var successPanel = document.getElementById("contact-success");
          if (successPanel) successPanel.focus();
          return;
        }

        if (result.data && result.data.errors) {
          showFieldErrors(result.data.errors);
        }
        showFormState("error");
      })
      .catch(function () {
        setSubmitting(false);
        showFormState("error");
      });
  }

  function init() {
    renderPathCards();
    populateSelects();
    bindPathCards();

    var form = document.getElementById("contact-form");
    if (form) {
      form.addEventListener("submit", handleSubmit);
    }

    var params = getQueryParams();
    if (params.path) {
      var card = document.querySelector(
        '.contact-path-card[data-path="' + params.path + '"]'
      );
      if (card) {
        card.classList.add("is-active");
        card.setAttribute("aria-pressed", "true");
      }
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
