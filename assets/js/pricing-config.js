/**
 * terminal.glass pricing configuration
 * Sales content lives here; presentation is built by pricing-page.js
 */

const pricingConfig = {
  promotionsEnabled: false,
  promotionLabel: "",
  starterPromotionalPrice: null,
  businessPromotionalPrice: null,
  expansionPromotionalPrice: null,
  bonusLicenses: 0,
  promotionExpiration: null,
};

const pricingPlans = [
  {
    id: "sunrise-starter",
    name: "Sunrise Starter",
    price: 199,
    billingLabel: "One-time package price",
    badge: null,
    featured: false,
    description:
      "For small businesses, professionals, and early adopters who want to begin using private AI without overcommitting.",
    licenseCount: 2,
    features: [
      "2 server licenses (2 Terminal.Glass instances)",
      "Deploy NoCloudGPT on Ubuntu Linux VMs or standalone servers",
      "Deploy on customer-owned AWS or DigitalOcean",
      "Assign licenses to Glass Agents or Jet Agents",
      "Happy Nerds Menu included in every instance",
      "Built-in DokuWiki per server instance",
      "Glass Agents powered by OpenClaw beta eligibility",
      "Private customer-controlled deployment",
      "Complete guided deployment instructions",
      "License reassignment from the customer dashboard when available",
    ],
    ctaLabel: "Get Sunrise Starter",
    ctaHref: "/contact/?intent=order&package=sunrise-starter",
    ctaPrimary: false,
    secondaryText: "Every Sunrise account includes two server licenses.",
  },
  {
    id: "sunrise-business",
    name: "Sunrise Business",
    price: 399,
    billingLabel: "One-time package price",
    badge: "Best Value",
    featured: true,
    description:
      "For businesses that want several private AI helpers, multiple servers, or a flexible local-and-cloud deployment strategy.",
    licenseCount: 6,
    features: [
      "6 server licenses (6 Terminal.Glass instances)",
      "Everything included with Sunrise Starter",
      "Better local and cloud hybrid flexibility",
      "Expanded Happy Nerds Menu access",
      "Multiple server or agent deployments",
      "Priority access to Glass Agent and Jet Agent betas",
      "Better fit for teams, departments, and multi-location businesses",
      "Mix NoCloudGPT, AWS, DigitalOcean, Glass Agents, and Jet Agents",
    ],
    ctaLabel: "Choose Sunrise Business",
    ctaHref: "/contact/?intent=order&package=sunrise-business",
    ctaPrimary: true,
    secondaryText: "Six server licenses for less than buying them separately.",
  },
  {
    id: "glass-license-expansion",
    name: "Additional Server License",
    price: 99,
    billingLabel: "Expansion price for existing customers",
    badge: null,
    featured: false,
    description:
      "Add server licenses to a Sunrise account for $99 each — one license activates one Terminal.Glass instance on one computer or cloud server.",
    licenseCount: 1,
    features: [
      "Add one additional server license",
      "Use it for another NoCloudGPT server",
      "Use it for another AWS or DigitalOcean deployment",
      "Assign it to a Glass Agent workload",
      "Assign it to a Jet Agent workload",
      "Reassign it later to a different supported deployment",
      "Available to existing terminal.glass customers",
      "No need to purchase another complete starter package",
    ],
    ctaLabel: "Add a Server License",
    ctaHref: "/contact/?intent=order&package=glass-license",
    ctaPrimary: false,
    secondaryText: null,
    footnote:
      "Additional licenses require an active terminal.glass customer account or qualifying Sunrise package.",
  },
];

const pricingPromotions = {
  launchSpecial: {
    type: "launch",
    title: "Launch Special",
    description: "Limited-time discount on Sunrise Starter.",
    planId: "sunrise-starter",
    regularPrice: 199,
    promotionalPrice: 149,
  },
  bonusLicense: {
    type: "bonus",
    title: "Bonus License Offer",
    description:
      "Buy Sunrise Starter and receive one additional server license at no charge.",
    planId: "sunrise-starter",
    bonusLicenses: 1,
  },
  expansionSale: {
    type: "expansion",
    title: "Expansion Sale",
    description: "Discount on additional server licenses for existing customers.",
    planId: "glass-license-expansion",
    regularPrice: 99,
    promotionalPrice: 79,
  },
  foundingCustomer: {
    type: "founding",
    title: "Founding Customer Offer",
    description:
      "Founding customers receive priority access to Glass Agent and Jet Agent betas.",
    planId: "sunrise-business",
  },
};

const pricingLogicExamples = [
  {
    title: "Sunrise Starter",
    lines: [
      { label: "Sunrise Starter", value: "2 server licenses", price: "$199" },
      { label: "Add one instance", value: "1 additional server license", price: "+$99" },
    ],
    totalLabel: "Total",
    totalValue: "3 active Terminal.Glass instances",
    totalPrice: "$298",
  },
  {
    title: "Sunrise Business savings",
    lines: [
      { label: "Sunrise Business", value: "6 server licenses", price: "$399" },
      {
        label: "Equivalent separate value",
        value: "2 licenses at $199 plus 4 expansion licenses at $99",
        price: "$595",
      },
    ],
    totalLabel: "Sunrise Business saves",
    totalValue: null,
    totalPrice: "$196",
    highlight: true,
  },
];

const glassLicenseDeploymentTypes = [
  {
    id: "nocloudgpt",
    name: "NoCloudGPT",
    description: "Ubuntu Linux 24/26 VM or standalone server you control",
  },
  {
    id: "aws",
    name: "AWS",
    description: "Customer-owned AWS instance with guided sizing",
  },
  {
    id: "digitalocean",
    name: "DigitalOcean",
    description: "Customer-owned DigitalOcean server with guided sizing",
  },
  {
    id: "glass-agent",
    name: "Glass Agent",
    description:
      "Glass Agents powered by OpenClaw in approved tools and workflows",
  },
  {
    id: "jet-agent",
    name: "Jet Agent",
    description:
      "Ollama-powered CPU or GPU compute agents for selected AI models",
  },
];

const pricingComparison = {
  columns: ["sunrise-starter", "sunrise-business", "glass-license-expansion"],
  rows: [
    { feature: "Price", values: ["$199", "$399", "$99"] },
    { feature: "Included server licenses", values: ["2 licenses", "6 licenses", "1 license"] },
    { feature: "NoCloudGPT eligibility", values: ["Yes", "Yes", "Yes"] },
    { feature: "AWS deployment eligibility", values: ["Yes", "Yes", "Yes"] },
    { feature: "DigitalOcean eligibility", values: ["Yes", "Yes", "Yes"] },
    { feature: "Glass Agent eligibility", values: ["Yes", "Yes", "Yes"] },
    { feature: "Jet Agent eligibility", values: ["Yes", "Yes", "Yes"] },
    { feature: "Happy Nerds Menu", values: ["Included", "Expanded access", "Based on existing package"] },
    { feature: "Built-in DokuWiki", values: ["Included", "Included", "Based on existing package"] },
    { feature: "Multi-server flexibility", values: ["Limited", "Strong", "Adds one instance"] },
    { feature: "Hybrid local/cloud deployments", values: ["Yes", "Strong", "Adds one instance"] },
    { feature: "Group plan expansion ($49/license)", values: ["Contact sales", "Contact sales", "Contact sales"] },
    { feature: "Priority beta access", values: ["Standard", "Priority", "Based on existing package"] },
    { feature: "Best use case", values: [
      "Small businesses and first deployments",
      "Teams, departments, and multi-location businesses",
      "Existing customers expanding capacity",
    ]},
  ],
};

const pricingFaqs = [
  {
    question: "Is the $199 price per server?",
    answer:
      "No. Every Sunrise account includes two server licenses, so you can begin with two private AI server instances. Each server license activates one Terminal.Glass instance on one computer or cloud server.",
  },
  {
    question: "Can I add another server later?",
    answer:
      "Yes. Add server licenses to a Sunrise account for $99 each. Group accounts can add server licenses for $49 each; larger deployments may qualify for private volume pricing.",
  },
  {
    question: "Can I use one license for two servers?",
    answer:
      "No. One server license supports one active Terminal.Glass instance at a time.",
  },
  {
    question: "Can I move a license between servers?",
    answer:
      "Yes. A server license may be deactivated from one deployment and reassigned to another supported deployment.",
  },
  {
    question: "Does terminal.glass host my business data?",
    answer:
      "Not by default. Your private AI runs on your server or inside your cloud account. terminal.glass handles licensing, deployment access, and related account services.",
  },
  {
    question: "What is the difference between NoCloudGPT and AWS or DigitalOcean?",
    answer:
      "NoCloudGPT runs on an Ubuntu Linux 24/26 virtual machine or standalone server you control. AWS and DigitalOcean deployments run in cloud accounts you own, with Terminal.Glass recommending the appropriate instance.",
  },
  {
    question: "What are Glass Agents?",
    answer:
      "Glass Agents powered by OpenClaw work through customer-approved tools and workflows inside the Terminal.Glass environment.",
  },
  {
    question: "What are Jet Agents?",
    answer:
      "Jet Agents use Ollama-powered CPU or GPU compute to run the private AI models selected for the workload.",
  },
  {
    question: "Is $99 a promotional price?",
    answer:
      "$99 is the standard expansion price for one additional server license unless a separate limited-time promotion is active.",
  },
  {
    question: "Can terminal.glass offer promotional pricing?",
    answer:
      "Yes. Promotional offers may include discounted starter packages, bonus server licenses, expansion discounts, or founding-customer benefits.",
  },
  {
    question: "Is cloud infrastructure included?",
    answer:
      "No. Customers remain responsible for the cost of their hardware, cloud server, storage, model API usage, and other third-party infrastructure unless a specific offer states otherwise.",
  },
  {
    question: "Is installation support included?",
    answer:
      "Complete guided deployment instructions and supported installer access are included. Deployment documentation and available support options are provided with your account. Custom engineering or managed service work may require a separate quote.",
  },
];
