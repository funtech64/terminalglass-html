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
      "2 portable Glass Licenses",
      "Deploy NoCloudGPT on customer-owned hardware",
      "Deploy YourCloudGPT in the customer's own cloud",
      "Assign licenses to servers with Glass Agent and Jet Agent beta eligibility",
      "Starter Happy Nerds Menu agents",
      "OpenClaw-Glass beta eligibility",
      "Private customer-controlled deployment",
      "Access to supported terminal.glass installer packages",
      "License reassignment from the customer dashboard when available",
    ],
    ctaLabel: "Get Sunrise Starter",
    ctaHref: "/contact/?intent=order&package=sunrise-starter",
    ctaPrimary: false,
    secondaryText: "Includes two active deployments.",
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
      "6 portable Glass Licenses",
      "Everything included with Sunrise Starter",
      "Better local and cloud hybrid flexibility",
      "More Happy Nerds Menu agents",
      "Multiple server or agent deployments",
      "Priority access to Glass Agent and Jet Agent betas",
      "Founding-member discount for Alchemist Conductor",
      "Better fit for teams, departments, and multi-location businesses",
      "Ability to mix NoCloudGPT, YourCloudGPT, and eligible Glass Agent or Jet Agent betas",
    ],
    ctaLabel: "Choose Sunrise Business",
    ctaHref: "/contact/?intent=order&package=sunrise-business",
    ctaPrimary: true,
    secondaryText: "Six licenses for less than buying them separately.",
  },
  {
    id: "glass-license-expansion",
    name: "Additional Glass License",
    price: 99,
    billingLabel: "Expansion price for existing customers",
    badge: null,
    featured: false,
    description:
      "Expand one server, cloud deployment, office, department, or AI agent at a time.",
    licenseCount: 1,
    features: [
      "Add one additional portable Glass License",
      "Use it for another NoCloudGPT server",
      "Use it for another YourCloudGPT server",
      "Assign it to an eligible Glass Agent beta",
      "Assign it to an eligible Jet Agent beta",
      "Reassign it later to a different supported deployment",
      "Available to existing terminal.glass customers",
      "No need to purchase another complete starter package",
    ],
    ctaLabel: "Add a Glass License",
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
      "Buy Sunrise Starter and receive one additional Glass License at no charge.",
    planId: "sunrise-starter",
    bonusLicenses: 1,
  },
  expansionSale: {
    type: "expansion",
    title: "Expansion Sale",
    description: "Discount on additional Glass Licenses for existing customers.",
    planId: "glass-license-expansion",
    regularPrice: 99,
    promotionalPrice: 79,
  },
  foundingCustomer: {
    type: "founding",
    title: "Founding Customer Offer",
    description:
      "Founding customers receive priority access and a future Alchemist Conductor discount.",
    planId: "sunrise-business",
  },
};

const pricingLogicExamples = [
  {
    title: "Sunrise Starter",
    lines: [
      { label: "Sunrise Starter", value: "2 Glass Licenses", price: "$199" },
      { label: "Add one deployment", value: "1 additional Glass License", price: "+$99" },
    ],
    totalLabel: "Total",
    totalValue: "3 active deployments",
    totalPrice: "$298",
  },
  {
    title: "Sunrise Business savings",
    lines: [
      { label: "Sunrise Business", value: "6 Glass Licenses", price: "$399" },
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
    description: "Private AI on your own server",
  },
  {
    id: "yourcloudgpt",
    name: "YourCloudGPT",
    description: "Private AI in your own cloud account",
  },
  {
    id: "glass-agent",
    name: "Glass Agent",
    description:
      "Supported beta: an action-capable worker operating inside an approved environment",
  },
  {
    id: "jet-agent",
    name: "Jet Agent",
    description:
      "Supported beta: a cloud-model-powered AI helper for advanced reasoning, drafting, research, and technical work",
  },
];

const pricingComparison = {
  columns: ["sunrise-starter", "sunrise-business", "glass-license-expansion"],
  rows: [
    { feature: "Price", values: ["$199", "$399", "$99"] },
    { feature: "Included Glass Licenses", values: ["2 licenses", "6 licenses", "1 license"] },
    { feature: "NoCloudGPT eligibility", values: ["Yes", "Yes", "Yes"] },
    { feature: "YourCloudGPT eligibility", values: ["Yes", "Yes", "Yes"] },
    { feature: "Glass Agent eligibility", values: ["Yes", "Yes", "Yes"] },
    { feature: "Jet Agent eligibility", values: ["Yes", "Yes", "Yes"] },
    { feature: "Happy Nerds Menu access", values: ["Starter access", "Expanded access", "Based on existing package"] },
    { feature: "Multi-server flexibility", values: ["Limited", "Strong", "Adds one deployment"] },
    { feature: "Hybrid local/cloud deployments", values: ["Yes", "Strong", "Adds one deployment"] },
    { feature: "Alchemist founding discount", values: ["Standard eligibility", "Included founding-member discount", "Based on existing package"] },
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
      "No. Sunrise Starter includes two portable Glass Licenses, allowing up to two active supported deployments.",
  },
  {
    question: "Can I add another server later?",
    answer:
      "Yes. Existing customers can add another Glass License for $99 and assign it to an additional supported server or agent.",
  },
  {
    question: "Can I use one license for two servers?",
    answer:
      "No. One Glass License supports one active deployment at a time.",
  },
  {
    question: "Can I move a license between servers?",
    answer:
      "Yes. A Glass License may be deactivated from one deployment and reassigned to another supported deployment.",
  },
  {
    question: "Does terminal.glass host my business data?",
    answer:
      "Not by default. Your private AI runs on your server or inside your cloud account. terminal.glass handles licensing, deployment access, and related account services.",
  },
  {
    question: "What is the difference between NoCloudGPT and YourCloudGPT?",
    answer:
      "NoCloudGPT runs on customer-owned local hardware or a private server. YourCloudGPT runs inside a cloud account controlled by the customer.",
  },
  {
    question: "What are Glass Agents?",
    answer:
      "Glass Agents are supported beta offerings: action-capable workers that operate within an environment approved by the customer. Eligibility is included with Sunrise packages; availability and rollout vary by deployment path and current beta access.",
  },
  {
    question: "What are Jet Agents?",
    answer:
      "Jet Agents are supported beta offerings that use powerful cloud models for reasoning, research, drafting, coding, and other advanced tasks. Eligibility is included with Sunrise packages; availability and rollout vary by deployment path and current beta access.",
  },
  {
    question: "Is $99 a promotional price?",
    answer:
      "$99 is the standard expansion price for one additional Glass License unless a separate limited-time promotion is active.",
  },
  {
    question: "Can terminal.glass offer promotional pricing?",
    answer:
      "Yes. Promotional offers may include discounted starter packages, bonus Glass Licenses, expansion discounts, or founding-customer benefits.",
  },
  {
    question: "Is cloud infrastructure included?",
    answer:
      "No. Customers remain responsible for the cost of their hardware, cloud server, storage, model API usage, and other third-party infrastructure unless a specific offer states otherwise.",
  },
  {
    question: "Is installation support included?",
    answer:
      "Package-specific deployment guidance and supported installer access are included. Custom engineering, migration work, extensive administration, or managed service work may require a separate quote.",
  },
];

const alchemistConductor = {
  title: "Grow into Alchemist Conductor",
  description:
    "Alchemist Conductor is the future premium coordination layer for terminal.glass.",
  capabilities: [
    "Coordinate Glass Agents and Jet Agents",
    "Assign and route tasks",
    "Send private work to local Glass Agents",
    "Send heavy reasoning work to Jet Agents",
    "Require owner approval for risky actions",
    "Maintain workflow logs and memory",
    "Coordinate multiple licensed deployments",
  ],
  bridge:
    "Buy Sunrise now, use private AI now, and keep your Glass Licenses ready for Alchemist later.",
  ctaLabel: "Join the Alchemist Founders List",
  ctaHref: "/contact/?intent=alchemist-founders",
};
