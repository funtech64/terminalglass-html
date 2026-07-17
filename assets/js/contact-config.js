/**
 * terminal.glass contact page configuration
 */

const contactFormConfig = {
  endpoint: "https://formspree.io/f/xnjepnjq",
  submitLabel: "Contact terminal.glass",
  submittingLabel: "Sending…",
  fallbackEmail: "jonathan@nocloudgpt.com",
};

const contactInterestOptions = [
  { value: "Sunrise Starter", label: "Sunrise Starter" },
  { value: "Sunrise Business", label: "Sunrise Business" },
  { value: "Additional Glass License", label: "Additional Glass License" },
  { value: "NoCloudGPT Deployment", label: "NoCloudGPT Deployment" },
  { value: "AWS or DigitalOcean Deployment", label: "AWS or DigitalOcean Deployment" },
  { value: "Glass Agents", label: "Glass Agents" },
  { value: "Jet Agents", label: "Jet Agents" },
  { value: "Enterprise Deployment", label: "Enterprise Deployment" },
  { value: "Partnership", label: "Partnership" },
  { value: "Technical Support", label: "Technical Support" },
  { value: "General Question", label: "General Question" },
];

const contactDeploymentOptions = [
  { value: "", label: "Select an option (optional)" },
  { value: "My own server — NoCloudGPT", label: "My own server — NoCloudGPT" },
  { value: "My own cloud — AWS or DigitalOcean", label: "My own cloud — AWS or DigitalOcean" },
  { value: "Hybrid local and cloud", label: "Hybrid local and cloud" },
  { value: "Glass or Jet Agents", label: "Glass or Jet Agents" },
  { value: "Not sure yet", label: "Not sure yet" },
];

const contactOrganizationSizes = [
  { value: "", label: "Select an option (optional)" },
  { value: "Just me", label: "Just me" },
  { value: "2–10 people", label: "2–10 people" },
  { value: "11–50 people", label: "11–50 people" },
  { value: "51–250 people", label: "51–250 people" },
  { value: "More than 250 people", label: "More than 250 people" },
];

const contactPathOptions = [
  {
    id: "sunrise",
    title: "Start with Sunrise",
    description:
      "For customers choosing between the $199 Starter and $399 Business packages.",
    interest: "Sunrise Starter",
    param: "path=sunrise",
  },
  {
    id: "expand",
    title: "Expand an existing deployment",
    description:
      "For customers adding another $99 Glass License.",
    interest: "Additional Glass License",
    param: "path=expand",
  },
  {
    id: "custom",
    title: "Plan a custom deployment",
    description:
      "For businesses, teams, partners, or multi-server environments.",
    interest: "Enterprise Deployment",
    param: "path=custom",
  },
];

/** Maps URL query params from pricing CTAs to interest values */
const contactUrlInterestMap = {
  "sunrise-starter": "Sunrise Starter",
  "sunrise-business": "Sunrise Business",
  "glass-license": "Additional Glass License",
};

const contactPathInterestMap = {
  sunrise: "Sunrise Starter",
  expand: "Additional Glass License",
  custom: "Enterprise Deployment",
};
