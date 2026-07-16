/**
 * terminal.glass pricing page — builds UI from pricing-config.js
 */
(function () {
  "use strict";

  function formatPrice(amount) {
    return "$" + amount;
  }

  function getPromotionalPrice(planId) {
    if (!pricingConfig.promotionsEnabled) return null;
    if (planId === "sunrise-starter" && pricingConfig.starterPromotionalPrice != null) {
      return pricingConfig.starterPromotionalPrice;
    }
    if (planId === "sunrise-business" && pricingConfig.businessPromotionalPrice != null) {
      return pricingConfig.businessPromotionalPrice;
    }
    if (planId === "glass-license-expansion" && pricingConfig.expansionPromotionalPrice != null) {
      return pricingConfig.expansionPromotionalPrice;
    }
    return null;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function renderPriceDisplay(plan) {
    const promo = getPromotionalPrice(plan.id);
    if (promo != null && promo < plan.price) {
      return (
        '<div class="plan-price-block">' +
        '<p class="plan-price plan-price-promo">' +
        formatPrice(promo) +
        "</p>" +
        '<p class="plan-price-original"><s>' +
        formatPrice(plan.price) +
        "</s></p>" +
        "</div>"
      );
    }
    return '<p class="plan-price">' + formatPrice(plan.price) + "</p>";
  }

  function renderPromotionBanner() {
    if (!pricingConfig.promotionsEnabled || !pricingConfig.promotionLabel) return "";
    let html =
      '<div class="promo-banner" role="status">' +
      '<span class="promo-banner-badge">Promotion</span>' +
      "<span>" +
      escapeHtml(pricingConfig.promotionLabel) +
      "</span>";
    if (pricingConfig.promotionExpiration) {
      html +=
        '<span class="promo-banner-expiry">Offer ends ' +
        escapeHtml(pricingConfig.promotionExpiration) +
        "</span>";
    }
    html += "</div>";
    return html;
  }

  function renderPricingCards() {
    const container = document.getElementById("pricing-cards");
    if (!container) return;

    let html = renderPromotionBanner();

    html += '<div class="price-grid pricing-cards-grid">';
    pricingPlans.forEach(function (plan) {
      const promo = getPromotionalPrice(plan.id);
      const featured = plan.featured ? " featured" : "";
      const badge = plan.badge
        ? '<span class="price-badge">' + escapeHtml(plan.badge) + "</span>"
        : "";
      const promoBadge =
        promo != null && promo < plan.price
          ? '<span class="price-badge price-badge-promo">Promotional</span>'
          : "";
      const btnClass = plan.ctaPrimary ? "btn btn-primary" : "btn btn-secondary";
      let bonusNote = "";
      if (
        pricingConfig.promotionsEnabled &&
        pricingConfig.bonusLicenses > 0 &&
        plan.id === "sunrise-starter"
      ) {
        bonusNote =
          '<p class="plan-bonus-note">+' +
          pricingConfig.bonusLicenses +
          " bonus Glass License" +
          (pricingConfig.bonusLicenses > 1 ? "s" : "") +
          " included</p>";
      }

      html +=
        '<article class="card price-card' +
        featured +
        '" aria-labelledby="plan-' +
        plan.id +
        '">' +
        '<div class="price-card-header">' +
        promoBadge +
        badge +
        "<h3 id=\"plan-" +
        plan.id +
        '">' +
        escapeHtml(plan.name) +
        "</h3>" +
        renderPriceDisplay(plan) +
        '<p class="plan-billing">' +
        escapeHtml(plan.billingLabel) +
        "</p>" +
        "</div>" +
        '<p class="plan-desc">' +
        escapeHtml(plan.description) +
        "</p>" +
        bonusNote +
        '<ul class="check-list plan-features">' +
        plan.features
          .map(function (f) {
            return "<li>" + escapeHtml(f) + "</li>";
          })
          .join("") +
        "</ul>";

      if (plan.footnote) {
        html +=
          '<p class="plan-footnote">' + escapeHtml(plan.footnote) + "</p>";
      }

      html +=
        '<div class="card-cta">' +
        '<a class="' +
        btnClass +
        '" href="' +
        escapeHtml(plan.ctaHref) +
        '">' +
        escapeHtml(plan.ctaLabel) +
        "</a>";
      if (plan.secondaryText) {
        html +=
          '<p class="plan-secondary-text">' +
          escapeHtml(plan.secondaryText) +
          "</p>";
      }
      html += "</div></article>";
    });
    html += "</div>";

    html +=
      '<p class="infra-disclaimer">Buy private AI licenses once. Run them on your server, in your cloud, or as Glass and Jet Agents. Hardware, cloud servers, storage, and third-party model usage are billed separately by your provider.</p>';

    container.innerHTML = html;
  }

  function renderPromotionsSection() {
    const section = document.getElementById("promotions-section");
    if (!section) return;

    if (!pricingConfig.promotionsEnabled) {
      section.hidden = true;
      return;
    }

    section.hidden = false;
    const grid = document.getElementById("promotions-grid");
    if (!grid) return;

    const activeTypes = [];
    if (pricingConfig.starterPromotionalPrice != null) activeTypes.push("launch");
    if (pricingConfig.bonusLicenses > 0) activeTypes.push("bonus");
    if (pricingConfig.expansionPromotionalPrice != null) activeTypes.push("expansion");
    if (pricingConfig.businessPromotionalPrice != null || pricingConfig.promotionLabel.toLowerCase().indexOf("founding") >= 0) {
      activeTypes.push("founding");
    }

    const promos = [];
    if (activeTypes.indexOf("launch") >= 0) promos.push(pricingPromotions.launchSpecial);
    if (activeTypes.indexOf("bonus") >= 0) promos.push(pricingPromotions.bonusLicense);
    if (activeTypes.indexOf("expansion") >= 0) promos.push(pricingPromotions.expansionSale);
    if (activeTypes.indexOf("founding") >= 0) promos.push(pricingPromotions.foundingCustomer);

    if (promos.length === 0) {
      section.hidden = true;
      return;
    }

    grid.innerHTML = promos
      .map(function (promo) {
        let detail = "";
        if (promo.regularPrice != null && promo.promotionalPrice != null) {
          detail =
            '<p class="promo-offer-price"><s>' +
            formatPrice(promo.regularPrice) +
            "</s> " +
            formatPrice(promo.promotionalPrice) +
            "</p>";
        }
        if (promo.bonusLicenses) {
          detail =
            '<p class="promo-offer-detail">+' +
            promo.bonusLicenses +
            " bonus Glass License at no charge</p>";
        }
        return (
          '<div class="card promo-card">' +
          '<span class="tag">OFFER</span>' +
          "<h3>" +
          escapeHtml(promo.title) +
          "</h3>" +
          "<p>" +
          escapeHtml(promo.description) +
          "</p>" +
          detail +
          "</div>"
        );
      })
      .join("");
  }

  function renderPricingLogic() {
    const container = document.getElementById("pricing-logic-examples");
    if (!container) return;

    container.innerHTML = pricingLogicExamples
      .map(function (example) {
        const highlight = example.highlight ? " pricing-example-highlight" : "";
        let lines = example.lines
          .map(function (line) {
            return (
              '<div class="pricing-example-line">' +
              '<div class="pricing-example-line-main">' +
              "<strong>" +
              escapeHtml(line.label) +
              "</strong>" +
              "<span>" +
              escapeHtml(line.value) +
              "</span>" +
              "</div>" +
              '<span class="pricing-example-price">' +
              escapeHtml(line.price) +
              "</span>" +
              "</div>"
            );
          })
          .join("");

        return (
          '<div class="card pricing-example' +
          highlight +
          '">' +
          (example.title
            ? "<h3>" + escapeHtml(example.title) + "</h3>"
            : "") +
          '<div class="pricing-example-body">' +
          lines +
          '<div class="pricing-example-total">' +
          "<strong>" +
          escapeHtml(example.totalLabel) +
          "</strong>" +
          (example.totalValue
            ? "<span>" + escapeHtml(example.totalValue) + "</span>"
            : "") +
          '<span class="pricing-example-price">' +
          escapeHtml(example.totalPrice) +
          "</span>" +
          "</div>" +
          "</div></div>"
        );
      })
      .join("");
  }

  function renderDeploymentTypes() {
    const grid = document.getElementById("deployment-types-grid");
    if (!grid) return;

    grid.innerHTML = glassLicenseDeploymentTypes
      .map(function (type) {
        return (
          '<div class="card deployment-type-card">' +
          '<span class="deployment-type-icon" aria-hidden="true">◇</span>' +
          "<h3>" +
          escapeHtml(type.name) +
          "</h3>" +
          "<p>" +
          escapeHtml(type.description) +
          "</p>" +
          "</div>"
        );
      })
      .join("");
  }

  function renderComparisonTable() {
    const wrapper = document.getElementById("comparison-table-wrapper");
    if (!wrapper) return;

    const planNames = pricingPlans.map(function (p) {
      return p.name;
    });

    let html =
      '<div class="comparison-scroll" tabindex="0" role="region" aria-label="Feature comparison table">' +
      "<table class=\"comparison-table\">" +
      "<thead><tr><th scope=\"col\">Feature</th>";

    planNames.forEach(function (name, i) {
      html +=
        '<th scope="col">' +
        escapeHtml(name) +
        "</th>";
    });
    html += "</tr></thead><tbody>";

    pricingComparison.rows.forEach(function (row, rowIndex) {
      html += "<tr>";
      html +=
        '<th scope="row">' + escapeHtml(row.feature) + "</th>";
      row.values.forEach(function (val, colIndex) {
        html +=
          '<td data-label="' +
          escapeHtml(planNames[colIndex]) +
          '">' +
          escapeHtml(val) +
          "</td>";
      });
      html += "</tr>";
    });

    html += "</tbody></table></div>";

    wrapper.innerHTML = html;
  }

  function renderAlchemistSection() {
    const container = document.getElementById("alchemist-section-content");
    if (!container) return;

    container.innerHTML =
      "<p>" +
      escapeHtml(alchemistConductor.description) +
      "</p>" +
      "<p>It will:</p>" +
      '<ul class="check-list">' +
      alchemistConductor.capabilities
        .map(function (c) {
          return "<li>" + escapeHtml(c) + "</li>";
        })
        .join("") +
      "</ul>" +
      '<p class="alchemist-bridge"><strong>' +
      escapeHtml(alchemistConductor.bridge) +
      "</strong></p>" +
      '<div class="cta-row">' +
      '<a class="btn btn-secondary" href="' +
      escapeHtml(alchemistConductor.ctaHref) +
      '">' +
      escapeHtml(alchemistConductor.ctaLabel) +
      "</a></div>";
  }

  function renderFaqs() {
    const container = document.getElementById("faq-list");
    if (!container) return;

    container.innerHTML = pricingFaqs
      .map(function (faq, i) {
        return (
          '<details class="faq-item">' +
          '<summary><span class="faq-question">' +
          escapeHtml(faq.question) +
          '</span><span class="faq-toggle" aria-hidden="true"></span></summary>' +
          '<div class="faq-answer"><p>' +
          escapeHtml(faq.answer) +
          "</p></div></details>"
        );
      })
      .join("");
  }

  function renderStructuredData() {
    const script = document.getElementById("pricing-structured-data");
    if (!script) return;

    const offers = pricingPlans.map(function (plan) {
      const promo = getPromotionalPrice(plan.id);
      const price = promo != null ? promo : plan.price;
      return {
        "@type": "Offer",
        name: plan.name,
        price: price,
        priceCurrency: "USD",
        availability: "https://schema.org/InStock",
        url: "https://terminal.glass/pricing/",
        description: plan.description,
        eligibleQuantity: {
          "@type": "QuantitativeValue",
          value: plan.licenseCount,
          unitText: "Glass License",
        },
      };
    });

    const data = {
      "@context": "https://schema.org",
      "@type": "Product",
      name: "terminal.glass Glass Licenses",
      description:
        "Portable Glass Licenses for private business AI deployments on your server or in your cloud.",
      brand: {
        "@type": "Brand",
        name: "terminal.glass",
      },
      offers: offers,
    };

    script.textContent = JSON.stringify(data);
  }

  function init() {
    renderPricingCards();
    renderPromotionsSection();
    renderPricingLogic();
    renderDeploymentTypes();
    renderComparisonTable();
    renderAlchemistSection();
    renderFaqs();
    renderStructuredData();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
