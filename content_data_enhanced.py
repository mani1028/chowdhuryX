"""
CHOWDHURYX - CENTRALIZED CONTENT DATA
Updated with Client-Provided Enterprise Copy
"""

SERVICE_DETAILS = {
    'ai-solutions': {
        'id': 1,
        'name': 'AI Solutions',
        'tagline': 'Intelligent Systems for Scale',
        'slug': 'ai-solutions',
        'icon': 'fas fa-robot',
        'color': '#f43f5e',
        'philosophy': [
            'Augment human intelligence, not replace it',
            'Integrate seamlessly into existing workflows',
            'Deliver measurable ROI, not experimental outcomes',
            'Remain transparent, ethical, and controllable'
        ],
        'description': 'We build custom AI products and automation agents. Transform your business logic into intelligent software.',
        'short_description': 'Custom AI products and automation agents that transform your business logic into intelligent software solutions.',
        'full_description': 'Our AI solutions are built to solve real operational challenges, not just demonstrate technology. We design and deploy custom systems that enhance efficiency, improve decision-making, and create measurable business value with an enterprise-first mindset.',
        'features': [
            'Custom AI Chatbots & Virtual Assistants (Context-aware, Multi-language, CRM/ERP integrated)',
            'Business Process Automation (AI + RPA) for data validation, invoicing, and onboarding',
            'AI-Powered Analytics & Decision Intelligence (Predictive forecasting, KPI dashboards)',
            'Customer Experience Operations (AI-assisted agents, sentiment analysis)',
            'Legacy Integration (CRM, ERP, Accounting, Cloud/On-premise)',
            'Secure, Ethical & Compliant AI (GDPR, CCPA, Role-based access)'
        ],
        'delivery_model': [
            'Discovery & Strategy', 'AI Design & Architecture', 'Model Development & Integration', 
            'Testing & Optimization', 'Deployment & Scaling', 'Ongoing Support & Evolution'
        ],
        'who_we_serve': ['Enterprises', 'Startups', 'BPO Operations', 'E-commerce', 'Service-based companies'],
        'technologies': ['Python', 'TensorFlow', 'PyTorch', 'OpenAI API', 'LangChain', 'AWS SageMaker'],
        'tech_description': 'Leveraging cutting-edge AI frameworks and platforms for enterprise-grade solutions.',
        'benefits': [
            'Process Automation',
            'Intelligent Decision Making',
            'Scalable Intelligence',
            'Real-time Insights'
        ],
        'pricing': 'Custom quotes based on complexity. Starting from $15,000 for MVP.',
        'keywords': 'AI products, custom AI, machine learning, automation',
        'seo_description': 'Custom AI products and automation solutions tailored to your enterprise needs.',
        'seo_keywords': 'AI products, custom AI, machine learning, automation agents'
    },
    
    'bpo-services': {
        'id': 2,
        'name': 'Customer Support Services (CSR)',
        'tagline': 'Protect Your Brand',
        'slug': 'bpo-services',
        'icon': 'fas fa-headset',
        'color': '#fb923c',
        'philosophy': [
            'Support is a brand-defining function, not a cost center',
            'Clear communication and empathy',
            'Process discipline and accountability',
            'Data security and continuous improvement'
        ],
        'description': 'Experienced customer support executives (Voice/Chat) operating 24/7. Weekly reporting, flexible scalability, and dedicated specialists.',
        'short_description': 'Professional Business Process Outsourcing with 24/7 customer support executives providing Voice and Chat services.',
        'full_description': 'We operate as a true extension of your internal team. With U.S. strategic oversight and Hyderabad offshore execution, we provide 24/7 reliable, scalable, and high-quality voice and non-voice support.',
        'features': [
            'Voice Support: Inbound CSR, General inquiries, Order status, Technical support (L1/L2)',
            'Non-Voice Support: Live website chat, Email, Ticketing systems, CRM logging',
            'AI-Enhanced Ops: Automated ticket categorization, Priority routing, Sentiment detection',
            'Quality Assurance: FCR tracking, CSAT scorecards, Script compliance audits',
            'Security: Role-based access, GDPR/CCPA alignment, NDA enforcement'
        ],
        'use_cases': ['SaaS companies', 'E-commerce platforms', 'Healthcare/Finance (Non-clinical)', 'Startups'],
        'technologies': ['Zendesk', 'Freshdesk', 'AWS Connect', 'CRM Integration', 'VoIP Systems'],
        'tech_description': 'Enterprise-grade BPO infrastructure with world-class communication platforms.',
        'benefits': [
            'Round-the-Clock Support',
            'Cost Efficiency',
            'Professional Quality',
            'Rapid Scaling Capability'
        ],
        'pricing': '$12/hour per agent. Volume discounts available for teams of 5+.',
        'keywords': 'BPO services, customer support outsourcing, call center',
        'seo_description': 'Affordable BPO and customer support outsourcing services starting at $12/hour.',
        'seo_keywords': 'BPO services, customer support, outsourcing, call center'
    },

    'web-development': {
        'id': 3,
        'name': 'Web Development',
        'tagline': 'No WordPress. No Templates.',
        'slug': 'web-development',
        'icon': 'fas fa-laptop-code',
        'color': '#22d3ee',
        'philosophy': [
            'Strategic business asset, not just a digital presence',
            'Load fast, scale smoothly, and remain secure',
            'Clean, maintainable, code-first approach',
            'No third-party CMS limitations or bloated plugins'
        ],
        'description': 'Full-stack development, static web, and dynamic web. Tailored engineering from architecture to deployment and maintenance.',
        'short_description': 'Full-stack web development including static sites, dynamic applications, and complex web platforms.',
        'full_description': 'We design, develop, and maintain fully custom websites built using a traditional, code-first approach. We do not rely on WordPress or page builders. Every site is tailored from the ground up for speed and future flexibility.',
        'features': [
            'Custom Website Design & Development (Tailor-made, code-driven)',
            'Static Website Development (High speed, minimal attack surface, brand profiles)',
            'Dynamic Web Applications (User auth, database workflows, Admin panels)',
            'Website Redesign & Modernization (UX/UI improvement, SEO structure)',
            'Ongoing Maintenance (Performance monitoring, security updates, server monitoring)'
        ],
        'who_we_serve': ['Enterprises', 'Startups', 'SaaS companies', 'High-security organizations'],
        'technologies': ['React', 'Vue.js', 'Node.js', 'Python/Flask', 'PostgreSQL', 'AWS'],
        'tech_description': 'Modern web technologies and frameworks for high-performance applications.',
        'benefits': [
            'Scalable Architecture',
            'Security-First Design',
            'SEO Optimized',
            'Ongoing Support'
        ],
        'pricing': 'Custom quotes based on scope. Simple sites from $3,000, complex platforms from $15,000+.',
        'keywords': 'web development, website design, full-stack development',
        'seo_description': 'Professional full-stack web development services for websites and web applications.',
        'seo_keywords': 'web development, website design, web development company'
    },

    'it-consultant': {
        'id': 4,
        'name': 'Hire Remote Consultants',
        'tagline': 'Global Expertise. On Demand.',
        'slug': 'it-consultant',
        'icon': 'fas fa-user-tie',
        'color': '#4ade80',
        'philosophy': [
            'Immediate productivity, not long onboarding',
            'Full alignment with business objectives',
            'Clear accountability and visibility',
            'Secure, compliant, and professional engagement'
        ],
        'description': 'Dedicated Developers and Engineers aligned with your time zone. Short-term or long-term engagements with US quality assurance.',
        'short_description': 'Dedicated IT consultants and developers aligned with your timezone for flexible short and long-term engagements.',
        'full_description': 'We provide highly skilled IT and Non-IT remote consultants to support individuals, startups, and enterprises on short-term, long-term, or project-based engagements.',
        'features': [
            'IT Roles: Full Stack, AI/ML Engineers, Cloud/DevOps, QA, Cybersecurity',
            'Non-IT Roles: Virtual Assistants, CSR, Operations Executives, HR/Recruitment support',
            'Flexible Models: Short-term projects, Long-term dedicated teams, Part-time/Full-time',
            'Onboarding: Screening, skill validation, background checks, and performance monitoring'
        ],
        'technologies': ['AWS', 'Azure', 'Kubernetes', 'Python', 'React', 'Project Management Tools'],
        'tech_description': 'Expert consultants proficient in enterprise infrastructure and technology strategy.',
        'benefits': [
            'Flexible Engagement Models',
            'US Quality Standards',
            'Deep Technical Expertise',
            'Scalable Team Size'
        ],
        'pricing': '$15/hour per consultant. Team packages available with volume discounts.',
        'keywords': 'IT consultant, dedicated developer, software engineer, tech consulting',
        'seo_description': 'Hire dedicated IT consultants and engineers starting at $15/hour with timezone alignment.',
        'seo_keywords': 'IT consultant, dedicated developer, hire engineer, software consultant'
    },

    'software-dev': {
        'id': 6,
        'name': 'Software Development',
        'tagline': 'End-to-End Engineering',
        'slug': 'software-dev',
        'icon': 'fas fa-code',
        'color': '#60a5fa',
        'philosophy': [
            'Solve real business problems, not add complexity',
            'Scalable, secure, and maintainable from day one',
            'Clean architecture and long-term stability',
            'No pre-built shortcuts—100% custom code'
        ],
        'description': 'Full-stack development, Mobile Apps, and SaaS platforms. Tailored engineering from architecture to deployment and maintenance.',
        'short_description': 'Full-stack software development including mobile apps, SaaS platforms, and enterprise solutions.',
        'full_description': 'We design, develop, deploy, and maintain custom software solutions across web, mobile, and desktop. We manage the full lifecycle from discovery and architecture to deployment and maintenance.',
        'features': [
            'Web Application Development (Dashboards, API-first architecture)',
            'Mobile App Development (iOS/Android Native & Cross-platform)',
            'Desktop Application Development (Enterprise tools, offline systems)',
            'Full-Cycle Delivery: Discovery, Architecture, Custom Dev, QA, and Go-Live',
            'Maintenance: Bug fixes, security updates, and feature enhancements'
        ],
        'technologies': ['Python', 'Node.js', 'React Native', 'PostgreSQL', 'AWS', 'Docker'],
        'tech_description': 'Comprehensive technology stack for building modern, scalable software applications.',
        'benefits': [
            'Rapid Development',
            'Scalable Architecture',
            'Enterprise Security',
            'Long-term Support'
        ],
        'pricing': 'Custom quotes based on project scope. MVP starting from $10,000.',
        'keywords': 'software development, SaaS development, mobile app development',
        'seo_description': 'Professional software development for SaaS, mobile apps, and enterprise solutions.',
        'seo_keywords': 'software development, SaaS development, app development'
    },

    'ai-ml-solutions': {
        'id': 7,
        'name': 'AI & Machine Learning',
        'tagline': 'Advanced Intelligence Systems',
        'slug': 'ai-ml-solutions',
        'icon': 'fas fa-brain',
        'color': '#f59e0b',
        'philosophy': [
            'Solve measurable business problems',
            'Transparent, controllable, and ethical AI',
            'Continuous improvement with real data',
            'Explainable and auditable models'
        ],
        'description': 'Harness the power of AI and ML to automate processes and gain actionable insights.',
        'short_description': 'Advanced AI & ML solutions including Generative AI, automation agents, and predictive analytics.',
        'full_description': 'Transform data into intelligence. We build production-ready ML models using cutting-edge technologies like LLMs, vector databases, and deep learning frameworks. Our solutions integrate seamlessly with existing enterprise systems to deliver measurable business value.',
        'features': [
            'Generative AI: LLM integration, fine-tuning (GPT, Claude), and custom chatbots',
            'Intelligent Automation: RPO/BPO agents, workflow routing, compliance checks',
            'Natural Language Processing (NLP): Document extraction, sentiment analysis, conversational AI',
            'Computer Vision: Image recognition, object detection, quality inspection',
            'Predictive Analytics: Sales forecasting, churn prediction, risk detection',
            'Recommendation Engines: Personalization, pricing optimization, content discovery'
        ],
        'delivery_model': ['Data Engineering', 'Model Training & Fine-tuning', 'Validation & Testing', 'Deployment & Scaling', 'Drift Monitoring & Continuous Learning'],
        'who_we_serve': ['Enterprises', 'Startups', 'BPO Operations', 'E-commerce', 'Healthcare', 'Financial Services'],
        'technologies': ['Python', 'TensorFlow', 'PyTorch', 'OpenAI API', 'LangChain', 'Pinecone', 'Scikit-learn', 'AWS SageMaker', 'Hugging Face'],
        'tech_description': 'Advanced machine learning frameworks including LLM platforms, vector databases, and enterprise AI infrastructure.',
        'benefits': [
            'Process Automation',
            'Predictive Insights',
            'Enhanced Decision Making',
            'Competitive Advantage'
        ],
        'pricing': 'AI consulting: $5,000-$10,000. Custom models: $15,000-$50,000+',
        'keywords': 'AI development, machine learning, artificial intelligence, generative AI, LLM',
        'seo_description': 'Custom AI and machine learning solutions including Generative AI, automation agents, and predictive analytics.',
        'seo_keywords': 'AI development, machine learning, generative AI, LLM, automation agents'
    },

    'recruitment': {
        'id': 8,
        'name': 'US IT Recruitment (C2C)',
        'tagline': 'Precision IT Staffing',
        'slug': 'recruitment',
        'icon': 'fas fa-briefcase',
        'color': '#d946ef',
        'philosophy': [
            'Speed without compromising quality',
            'Deep understanding of US hiring standards',
            'Accurate screening—not keyword matching',
            'Trusted recruitment partner, not a resume agency'
        ],
        'description': 'Hybrid methodology sourcing (Citizens, GC, H1B, TN, OPT). Rigorous screening for US IT requirements and rapid placement.',
        'short_description': 'Expert recruitment services with visa sponsorship support for Citizens, GC, H1B, TN, and OPT candidates.',
        'full_description': 'Strategic C2C staffing powered by onshore US-based screening and offshore sourcing intelligence in Hyderabad. We ensure every candidate is technically qualified and client-ready.',
        'features': [
            'Hybrid Model: Offshore sourcing + Onshore US-standard technical screening',
            'Skill Coverage: Java, Python, .NET, Cloud/DevOps, Data/AI, QA, ERP, PM/BA',
            'Engagement Types: Contract (C2C), Contract-to-Hire (C2H)',
            'Compliance Support: Resume formatting, skill matrix, rate negotiation, interview coordination'
        ],
        'who_we_serve': ['Prime Vendors', 'Tier-1/2 Staffing Companies', 'System Integrators', 'Consulting Firms'],
        'technologies': ['LinkedIn Recruiter', 'USCIS Compliance Tools', 'E-Verify', 'ATS Systems', 'Video Interviewing'],
        'tech_description': 'Specialized tools and processes for US visa sponsorship and compliance management.',
        'benefits': [
            'Rapid Placement',
            'Visa Expertise',
            'Quality Candidates',
            'Compliance Guarantee'
        ],
        'pricing': '20-25% placement fee for permanent positions. Retainer models for ongoing recruitment needs.',
        'keywords': 'recruitment, visa sponsorship, H1B, talent acquisition, IT recruitment',
        'seo_description': 'Expert recruitment with visa sponsorship support for H1B, TN, GC, and OPT candidates.',
        'seo_keywords': 'recruitment, H1B visa, visa sponsorship, IT recruitment, talent acquisition'
    },

    'rpo-solutions': {
        'id': 9,
        'name': 'RPO (Recruitment Process Outsourcing)',
        'tagline': 'Full-Time & Permanent Hiring',
        'slug': 'rpo-solutions',
        'icon': 'fas fa-users-cog',
        'color': '#818cf8',
        'philosophy': [
            'Strategic, not reactive hiring',
            'Skill-driven, not resume-driven',
            'Culture alignment over just credentials',
            'Ownership of the entire recruitment lifecycle'
        ],
        'description': 'Recruitment Process Outsourcing for high-volume needs. Complex Boolean sourcing, background checks, and pipeline management.',
        'short_description': 'Recruitment Process Outsourcing (RPO) for high-volume recruiting with advanced sourcing and pipeline management.',
        'full_description': 'End-to-end acquisition for hard-to-fill, permanent roles. We take complete ownership of the process—from strategy and sourcing to final submission.',
        'features': [
            'Coverage: IT, Non-IT, Pharma, Healthcare, Finance, Manufacturing',
            'Niche Hiring: Passive candidate sourcing, market mapping, senior leadership roles',
            'End-to-End Model: Discovery, Sourcing, Multi-layer screening, Interview management',
            'Accountability: Measured by time-to-hire, submission-to-interview ratio, and long-term retention'
        ],
        'who_we_serve': ['Global Enterprises', 'Healthcare Systems', 'Pharma Companies', 'Manufacturing Firms'],
        'technologies': ['LinkedIn Recruiter', 'ATS Systems', 'HRIS Integration', 'Sourcing Databases', 'Compliance Tools'],
        'tech_description': 'Advanced recruitment technology and Boolean search expertise for efficient hiring.',
        'benefits': [
            'Reduced Time-to-Hire',
            'Cost Efficiency',
            'Quality Candidates',
            'Compliance Assurance'
        ],
        'pricing': '$5,000/month per dedicated recruiter. Volume discounts for enterprise-scale programs.',
        'keywords': 'RPO, recruitment outsourcing, talent acquisition, sourcing',
        'seo_description': 'Enterprise-scale Recruitment Process Outsourcing with advanced sourcing and pipeline management.',
        'seo_keywords': 'RPO, recruitment outsourcing, talent acquisition, recruiting'
    }
}

# Industry Data Update - Complete 11 Sectors with Segments
INDUSTRIES_DATA = {
    'it-software': {
        'name': 'Information Technology & Software',
        'subtitle': 'Enabling Innovation, Scale, and Engineering Excellence',
        'icon': 'fa-laptop-code',
        'description': 'Enterprise IT solutions and digital transformation',
        'tagline': 'Enabling Innovation, Scale, and Engineering Excellence',
        'segments': ['SaaS & Cloud Platforms', 'Product Engineering Companies', 'IT Services & Consulting Firms', 'Cybersecurity & Infrastructure Providers'],
        'support': [
            'Software, web, mobile, and desktop development',
            'AI & ML solutions',
            'IT staffing (C2C, RPO, contract & permanent)',
            'Remote IT consultants',
            'Technical customer support'
        ],
        'ideal_for': ['SaaS companies', 'IT services firms', 'product startups', 'cloud providers'],
        'how_we_support': [
            'Software, web, mobile, and desktop development',
            'AI & ML solutions',
            'IT staffing (C2C, RPO, contract & permanent)',
            'Remote IT consultants',
            'Technical customer support'
        ],
        'solutions': ['C2C IT Staffing', 'Cloud Migration', 'Custom Software Development', 'DevOps & Automation', 'AI/ML Solutions']
    },
    'healthcare': {
        'name': 'Healthcare & Medical Services (Non-Clinical)',
        'subtitle': 'Operational Excellence for Healthcare Organizations',
        'icon': 'fa-hospital-user',
        'description': 'HIPAA-compliant solutions for modern healthcare systems',
        'tagline': 'Operational Excellence for Healthcare Organizations',
        'segments': ['Hospitals & Clinics (non-clinical roles)', 'Healthcare IT companies', 'Medical service providers', 'Telehealth platforms'],
        'support': [
            'Healthcare RPO & permanent hiring',
            'Non-clinical customer support (voice & non-voice)',
            'Administrative and back-office operations',
            'Healthcare software platforms',
            'Automation and reporting systems'
        ],
        'ideal_for': ['Hospitals', 'clinics', 'healthcare IT firms', 'telehealth platforms'],
        'how_we_support': [
            'Healthcare RPO & permanent hiring',
            'Non-clinical customer support (voice & non-voice)',
            'Administrative and back-office operations',
            'Healthcare software platforms',
            'Automation and reporting systems'
        ],
        'solutions': ['Clinical RPO', 'HIPAA AI Solutions', 'EHR Integration', 'Telemedicine Platforms', 'Healthcare Analytics']
    },
    'finance': {
        'name': 'Finance, Banking & Professional Services',
        'subtitle': 'Secure, Scalable Solutions for High-Trust Industries',
        'icon': 'fa-university',
        'description': 'Secure fintech solutions and digital banking transformation',
        'tagline': 'Secure, Scalable Solutions for High-Trust Industries',
        'segments': ['Banking & Financial Services', 'Accounting & Advisory Firms', 'Insurance & Risk Services'],
        'support': [
            'Secure web and internal systems',
            'Data analytics and dashboards',
            'Back-office and operations support',
            'Customer support services',
            'Recruitment for finance, accounting, and operations roles'
        ],
        'ideal_for': ['Banks', 'accounting firms', 'insurance companies', 'advisory firms'],
        'how_we_support': [
            'Secure web and internal systems',
            'Data analytics and dashboards',
            'Back-office and operations support',
            'Customer support services',
            'Recruitment for finance, accounting, and operations roles'
        ],
        'solutions': ['Digital Banking', 'Fraud Detection AI', 'Financial CSR', 'Payment Solutions', 'Compliance Automation']
    },
    'ecommerce': {
        'name': 'E-Commerce, Retail & Consumer Services',
        'subtitle': 'Customer-First Digital and Operational Support',
        'icon': 'fa-shopping-bag',
        'description': 'Omnichannel retail solutions and personalized shopping experiences',
        'tagline': 'Customer-First Digital and Operational Support',
        'segments': ['Online retail platforms', 'D2C brands', 'Subscription-based services'],
        'support': [
            'Custom e-commerce platforms',
            'Website design, redesign, and maintenance',
            'Voice & non-voice customer support',
            'Order processing and back-office support',
            'AI-driven personalization and analytics'
        ],
        'ideal_for': ['Online retailers', 'D2C brands', 'subscription businesses'],
        'how_we_support': [
            'Custom e-commerce platforms',
            'Website design, redesign, and maintenance',
            'Voice & non-voice customer support',
            'Order processing and back-office support',
            'AI-driven personalization and analytics'
        ],
        'solutions': ['E-Commerce Development', 'Personalization ML', 'Customer Support CSR', 'Mobile Commerce', 'Supply Chain Tech']
    },
    'manufacturing': {
        'name': 'Manufacturing, Engineering & Industrial',
        'subtitle': 'Digital Transformation for Operational Efficiency',
        'icon': 'fa-industry',
        'description': 'Industry 4.0 solutions with IoT and predictive maintenance',
        'tagline': 'Digital Transformation for Operational Efficiency',
        'segments': ['Manufacturing companies', 'Engineering services firms', 'Industrial suppliers'],
        'support': [
            'ERP and internal system development',
            'Data reporting and automation',
            'Recruitment for technical and non-technical roles',
            'Documentation and operations support',
            'AI-enabled performance analytics'
        ],
        'ideal_for': ['Manufacturing companies', 'engineering services', 'industrial firms'],
        'how_we_support': [
            'ERP and internal system development',
            'Data reporting and automation',
            'Recruitment for technical and non-technical roles',
            'Documentation and operations support',
            'AI-enabled performance analytics'
        ],
        'solutions': ['IoT Solutions', 'Predictive Maintenance AI', 'Quality Control Systems', 'MES Development', 'Supply Chain Tech']
    },
    'logistics': {
        'name': 'Logistics, Supply Chain & Transportation',
        'subtitle': 'Visibility, Control, and Scalable Operations',
        'icon': 'fa-truck',
        'description': 'Supply chain optimization and fleet management solutions',
        'tagline': 'Visibility, Control, and Scalable Operations',
        'segments': ['Logistics providers', 'Warehousing & distribution companies', 'Transportation services'],
        'support': [
            'Operations and tracking software',
            'Customer service support',
            'Back-office coordination teams',
            'Data analytics and reporting',
            'Workforce and recruitment solutions'
        ],
        'ideal_for': ['Logistics providers', 'warehouses', 'transportation companies'],
        'how_we_support': [
            'Operations and tracking software',
            'Customer service support',
            'Back-office coordination teams',
            'Data analytics and reporting',
            'Workforce and recruitment solutions'
        ],
        'solutions': ['Fleet Management', 'Route Optimization AI', 'WMS Development', 'Tracking Systems', 'Logistics Analytics']
    },
    'education': {
        'name': 'Education, Training & EdTech',
        'subtitle': 'Intelligent Systems for Learning-Driven Organizations',
        'icon': 'fa-graduation-cap',
        'description': 'Modern learning platforms and educational technology',
        'tagline': 'Intelligent Systems for Learning-Driven Organizations',
        'segments': ['EdTech platforms', 'Training and certification providers', 'Educational institutions'],
        'support': [
            'Learning management platforms',
            'AI-enabled student support',
            'Voice & non-voice assistance',
            'Administrative operations',
            'Recruitment and staffing'
        ],
        'ideal_for': ['EdTech startups', 'training institutes', 'online education platforms'],
        'how_we_support': [
            'Learning management platforms',
            'AI-enabled student support',
            'Voice & non-voice assistance',
            'Administrative operations',
            'Recruitment and staffing'
        ],
        'solutions': ['LMS Development', 'Student Portals', 'Virtual Classrooms', 'Administrative Automation', 'AI Tutoring']
    },
    'startups': {
        'name': 'Startups & Emerging Businesses',
        'subtitle': 'From Idea to Scale—One Partner',
        'icon': 'fa-rocket',
        'description': 'Rapid development and scalable infrastructure for growing businesses',
        'tagline': 'From Idea to Scale—One Partner',
        'segments': ['Early-stage startups', 'Scaling startups', 'Venture-backed companies'],
        'support': [
            'MVP and product development',
            'AI & automation from early stages',
            'Remote IT & non-IT consultants',
            'Customer support setup',
            'Hiring strategy and RPO'
        ],
        'ideal_for': ['Early-stage and scaling startups'],
        'how_we_support': [
            'MVP and product development',
            'AI & automation from early stages',
            'Remote IT & non-IT consultants',
            'Customer support setup',
            'Hiring strategy and RPO'
        ],
        'solutions': ['MVP Development', 'Full-Stack Teams', 'Cloud Infrastructure', 'Product Consulting', 'Offshore Teams']
    },
    'enterprise': {
        'name': 'Enterprises & Large Organizations',
        'subtitle': 'Structured, Secure, and Scalable Global Delivery',
        'icon': 'fa-building',
        'description': 'Enterprise-grade solutions for complex business operations',
        'tagline': 'Structured, Secure, and Scalable Global Delivery',
        'segments': ['Global enterprises', 'Multinational organizations', 'Large-scale firms'],
        'support': [
            'Enterprise software development',
            'AI & data intelligence platforms',
            'Global BPO & customer support',
            'Large-scale RPO and staffing',
            'Dedicated offshore and hybrid teams'
        ],
        'ideal_for': ['Global enterprises', 'multinational organizations'],
        'how_we_support': [
            'Enterprise software development',
            'AI & data intelligence platforms',
            'Global BPO & customer support',
            'Large-scale RPO and staffing',
            'Dedicated offshore and hybrid teams'
        ],
        'solutions': ['Digital Transformation', 'C2C IT Staffing', 'Enterprise Apps', 'Global Delivery', 'Compliance Solutions']
    },
    'government': {
        'name': 'Government & Regulated Industries',
        'subtitle': 'Technology and Operations Support Where Permitted',
        'icon': 'fa-landmark',
        'description': 'Secure, compliant solutions for public sector organizations',
        'tagline': 'Technology and Operations Support Where Permitted',
        'segments': ['Public sector agencies', 'Regulated environments', 'Government contractors'],
        'support': [
            'Software and systems development',
            'Process automation and reporting',
            'Back-office operations',
            'Recruitment support'
        ],
        'ideal_for': ['Government agencies and regulated public sector bodies'],
        'how_we_support': [
            'Software and systems development',
            'Process automation and reporting',
            'Back-office operations',
            'Recruitment support'
        ],
        'solutions': ['Secure Portals', 'Compliance Systems', 'Accessibility Solutions', 'Case Management', 'Cybersecurity']
    },
    'pharmaceutical': {
        'name': 'Pharmaceutical & Life Sciences',
        'subtitle': 'Precision Support for Research-Driven Organizations',
        'icon': 'fa-flask',
        'description': 'Regulatory-compliant solutions for drug development and research',
        'tagline': 'Precision Support for Research-Driven Organizations',
        'segments': ['Pharmaceutical manufacturers', 'Research & life sciences firms', 'Regulatory and compliance teams'],
        'support': [
            'Permanent & contract hiring (RPO)',
            'Recruitment for niche scientific and operational roles',
            'Data analytics and reporting tools',
            'AI-driven process automation',
            'Internal software and compliance support'
        ],
        'ideal_for': ['Pharma companies', 'research organizations', 'life sciences firms'],
        'how_we_support': [
            'Permanent & contract hiring (RPO)',
            'Recruitment for niche scientific and operational roles',
            'Data analytics and reporting tools',
            'AI-driven process automation',
            'Internal software and compliance support'
        ],
        'solutions': ['CTMS Development', 'EDC Platforms', 'Regulatory Compliance', 'Research Analytics', 'LIMS Solutions']
    },
}

def get_service_details(slug):
    """Get service details by slug"""
    return SERVICE_DETAILS.get(slug)

def get_all_services_details():
    """Get all services with detailed content"""
    return SERVICE_DETAILS

def get_industry_details(slug):
    """Get industry details by slug"""
    return INDUSTRIES_DATA.get(slug)

def get_all_industries():
    """Get all industries"""
    return INDUSTRIES_DATA
