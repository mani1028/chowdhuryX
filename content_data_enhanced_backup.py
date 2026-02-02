"""
CHOWDHURYX - CENTRALIZED CONTENT DATA
Updated with Client-Provided Enterprise Copy
"""

# Enhanced Service Details with Detailed Content - 8 Services from Reference Design
SERVICE_DETAILS = {
    'ai-solutions': {
        'id': 1,
        'name': 'AI Solutions',
        'tagline': 'Custom AI Products',
        'slug': 'ai-solutions',
        'icon': 'fas fa-robot',
        'color': '#f43f5e',
        'description': 'We build custom AI products and automation agents. Transform your business logic into intelligent software.',
        'short_description': 'Custom AI products and automation agents that transform your business logic into intelligent software solutions.',
        'full_description': 'ChowdhuryX specializes in building custom AI products and automation agents that integrate seamlessly with your business operations. From chatbots and predictive analytics to custom machine learning models, we deliver enterprise-grade AI systems tailored to your specific needs. Our AI solutions help you automate complex processes, gain actionable insights, and make data-driven decisions at scale.',
        'features': [
            'Custom AI Model Development',
            'Automation Agent Integration',
            'Predictive Analytics & Insights',
            'Natural Language Processing',
            'Computer Vision Solutions',
            'Enterprise AI Deployment'
        ],
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
        'name': 'BPO Services',
        'tagline': '$12/hr',
        'slug': 'bpo-services',
        'icon': 'fas fa-headset',
        'color': '#fb923c',
        'description': 'Experienced customer support executives (Voice/Chat) operating 24/7. Weekly reporting, flexible scalability, and dedicated specialists.',
        'short_description': 'Professional Business Process Outsourcing with 24/7 customer support executives providing Voice and Chat services.',
        'full_description': 'Our BPO services connect you with highly trained customer support specialists operating around the clock. We provide Voice support, Chat support, Email management, and comprehensive ticket handling with professional service standards. With flexible scaling capabilities and detailed weekly reporting, we ensure your customers receive exceptional service quality while you focus on core business operations. Our team is trained in industry best practices and equipped with state-of-the-art communication tools.',
        'features': [
            '24/7 Customer Support Operations',
            'Voice & Chat Support',
            'Email & Ticket Management',
            'Weekly Performance Reports',
            'Flexible Scalability',
            'Dedicated Specialist Teams'
        ],
        'technologies': ['VoIP Systems', 'CRM Integration', 'Live Chat Platforms', 'AWS Connect', 'Zendesk', 'Freshdesk'],
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
        'tagline': 'Custom Quotes',
        'slug': 'web-development',
        'icon': 'fas fa-laptop-code',
        'color': '#22d3ee',
        'description': 'Full-stack development, static web, and dynamic web. Tailored engineering from architecture to deployment and maintenance.',
        'short_description': 'Full-stack web development including static sites, dynamic applications, and complex web platforms.',
        'full_description': 'We deliver comprehensive web development services spanning from custom static websites to complex dynamic web applications. Our expert team handles complete project lifecycle including architecture design, responsive UI/UX development, backend engineering, database design, and post-launch maintenance. Whether you need an e-commerce platform, content management system, or custom web application, we build scalable, secure, and performance-optimized solutions using modern frameworks and best practices.',
        'features': [
            'Full-Stack Web Development',
            'Responsive UI/UX Design',
            'Backend API Development',
            'Database Architecture',
            'E-Commerce Solutions',
            'Performance Optimization'
        ],
        'technologies': ['React', 'Vue.js', 'Node.js', 'Python', 'PostgreSQL', 'MongoDB', 'AWS', 'Docker'],
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
        'name': 'Hire IT Consultant',
        'tagline': '$15/hr',
        'slug': 'it-consultant',
        'icon': 'fas fa-laptop',
        'color': '#4ade80',
        'description': 'Dedicated Developers and Engineers aligned with your time zone. Short-term or long-term engagements with US quality assurance.',
        'short_description': 'Dedicated IT consultants and developers aligned with your timezone for flexible short and long-term engagements.',
        'full_description': 'Access dedicated IT professionals and engineers who integrate seamlessly into your team with timezone-aligned support. Our consultants bring expertise across multiple domains including system architecture, infrastructure management, security consulting, and technology strategy. Whether you need short-term project support, interim leadership, or long-term strategic partnership, we provide experienced professionals with proven track records and US-standard quality assurance practices ensuring accountability and excellence.',
        'features': [
            'Timezone-Aligned Availability',
            'Dedicated Team Members',
            'Architecture & Strategy Consulting',
            'Infrastructure Management',
            'Security & Compliance Consulting',
            'Technical Training & Mentoring'
        ],
        'technologies': ['AWS', 'Azure', 'Kubernetes', 'Linux', 'Network Architecture', 'Security Tools'],
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
    
    'digital-marketing': {
        'id': 5,
        'name': 'Digital Marketing',
        'tagline': '$10/hr',
        'slug': 'digital-marketing',
        'icon': 'fas fa-bullhorn',
        'color': '#ec4899',
        'description': 'SEO, Social Media Management, Content Strategy, and Google Ads. We manage campaigns during peak engagement hours for maximum ROI.',
        'short_description': 'Comprehensive digital marketing services including SEO, social media, content strategy, and paid advertising.',
        'full_description': 'Maximize your online presence with our comprehensive digital marketing solutions. We develop and execute integrated marketing strategies spanning SEO optimization, social media management, content creation, Google Ads management, and analytics tracking. Our team strategically manages campaigns during peak engagement hours to ensure maximum reach and ROI. From improving search rankings to building engaged social communities, we deliver measurable results that drive business growth.',
        'features': [
            'SEO Optimization & Strategy',
            'Social Media Management',
            'Content Marketing & Creation',
            'Google Ads Management',
            'Analytics & Reporting',
            'Email Marketing Campaigns'
        ],
        'technologies': ['Google Analytics', 'Google Ads', 'SEMrush', 'Hootsuite', 'Mailchimp', 'WordPress'],
        'tech_description': 'Industry-leading marketing tools and platforms for comprehensive campaign management.',
        'benefits': [
            'Increased Visibility',
            'Higher Conversion Rates',
            'Brand Authority',
            'Measurable ROI'
        ],
        'pricing': '$10/hour per specialist. Package rates available for comprehensive campaigns.',
        'keywords': 'digital marketing, SEO, social media marketing, content marketing',
        'seo_description': 'Professional digital marketing services for SEO, social media, and paid advertising.',
        'seo_keywords': 'digital marketing, SEO, social media, Google Ads, marketing agency'
    },
    
    'software-dev': {
        'id': 6,
        'name': 'Software Dev',
        'tagline': 'Custom Quotes',
        'slug': 'software-dev',
        'icon': 'fas fa-laptop-code',
        'color': '#60a5fa',
        'description': 'Full-stack development, Mobile Apps, and SaaS platforms. Tailored engineering from architecture to deployment and maintenance.',
        'short_description': 'Full-stack software development including mobile apps, SaaS platforms, and enterprise solutions.',
        'full_description': 'We deliver enterprise-grade software development services covering the complete development lifecycle. Our team specializes in building scalable SaaS platforms, native mobile applications, and complex backend systems. With expertise in modern development frameworks and cloud technologies, we create software solutions that are reliable, secure, and built for growth. From initial architecture through deployment and ongoing support, we ensure your software meets the highest quality standards.',
        'features': [
            'SaaS Platform Development',
            'Mobile App Development',
            'Enterprise Software Solutions',
            'API & Backend Development',
            'Cloud Architecture Design',
            'DevOps & Deployment'
        ],
        'technologies': ['Python', 'Node.js', 'React', 'React Native', 'PostgreSQL', 'AWS', 'Kubernetes'],
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
    
    'rpo-solutions': {
        'id': 7,
        'name': 'RPO Solutions',
        'tagline': 'Enterprise Scale',
        'slug': 'rpo-solutions',
        'icon': 'fas fa-share-nodes',
        'color': '#818cf8',
        'description': 'Recruitment Process Outsourcing for high-volume needs. Complex Boolean sourcing, background checks, and pipeline management.',
        'short_description': 'Recruitment Process Outsourcing (RPO) for high-volume recruiting with advanced sourcing and pipeline management.',
        'full_description': 'Scale your recruitment operations with our comprehensive Recruitment Process Outsourcing solutions. We handle end-to-end recruitment including candidate sourcing, screening, interviewing, background verification, and offer management. Our team uses advanced Boolean search techniques and database leveraging to identify passive candidates that match your specific requirements. With dedicated account managers and detailed reporting, we ensure efficient hiring at scale while maintaining strict compliance and confidentiality standards.',
        'features': [
            'Complex Boolean Sourcing',
            'Candidate Screening & Assessment',
            'Background Check Coordination',
            'Interview Management',
            'Offer & Onboarding Support',
            'Pipeline Analytics & Reporting'
        ],
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
    },
    
    'recruitment': {
        'id': 8,
        'name': 'Recruitment',
        'tagline': 'C2C / C2H Full-Time',
        'slug': 'recruitment',
        'icon': 'fas fa-briefcase',
        'color': '#d946ef',
        'description': 'Hybrid methodology sourcing (Citizens, GC, H1B, TN, OPT). Rigorous screening for US IT requirements and rapid placement.',
        'short_description': 'Expert recruitment services with visa sponsorship support for Citizens, GC, H1B, TN, and OPT candidates.',
        'full_description': 'ChowdhuryX provides specialized recruitment services with deep expertise in US visa sponsorship scenarios. Our hybrid sourcing methodology connects you with qualified candidates including US Citizens, Green Card holders, H1B visa holders, TN visa workers, and OPT students. We conduct rigorous technical and cultural screening, coordinate interviews, manage background checks, and guide candidates through the visa sponsorship process. With a focus on rapid placement and candidate retention, we deliver IT talent that meets your exact requirements.',
        'features': [
            'Visa Sponsorship Expertise',
            'Multi-Status Sourcing',
            'Technical Screening & Assessment',
            'Background Verification',
            'Interview Coordination',
            'Placement & Onboarding Support'
        ],
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
    
    'ai-ml-solutions': {
        'id': 4,
        'name': 'AI & Machine Learning Solutions',
        'tagline': 'Intelligent automation for modern business',
        'icon': 'fas fa-brain',
        'color': '#f59e0b',
        'description': 'Harness the power of AI and ML to automate processes and gain actionable insights.',
        'short_description': 'Harness the power of AI and ML to automate processes and gain actionable insights.',
        'full_description': 'Our AI and ML experts develop intelligent systems that learn from your data to solve complex business problems. We create predictive models, chatbots, recommendation engines, and automation solutions that drive real business value and competitive advantage in your industry.',
        'features': [
            'Custom ML model development',
            'Predictive analytics',
            'NLP chatbots & conversational AI',
            'Computer vision solutions',
            'Recommendation engines',
            'Data preprocessing & feature engineering'
        ],
        'technologies': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-learn', 'OpenAI', 'LangChain'],
        'tech_description': 'Advanced machine learning and deep learning frameworks for intelligent solutions.',
        'benefits': [
            'Process Automation',
            'Predictive Insights',
            'Enhanced Decision Making',
            'Competitive Advantage'
        ],
        'pricing': 'AI consulting: $5,000-$10,000. Custom models: $15,000-$50,000+',
        'keywords': 'AI development, machine learning, artificial intelligence',
        'seo_description': 'Custom AI and machine learning solutions for business automation and intelligence.',
        'seo_keywords': 'AI development, machine learning, AI solutions'
    }
}

# Industries Data
INDUSTRIES_DATA = {
    'healthcare': {
        'name': 'Healthcare',
        'description': 'HIPAA-compliant solutions for modern healthcare systems',
        'icon': 'fas fa-hospital',
        'services': ['Cloud Solutions', 'Mobile Applications', 'Enterprise Solutions']
    },
    'finance': {
        'name': 'Finance & Banking',
        'description': 'Secure, compliant fintech solutions',
        'icon': 'fas fa-university',
        'services': ['Enterprise Solutions', 'Custom Software', 'AI Solutions']
    },
    'retail': {
        'name': 'Retail & E-commerce',
        'description': 'Omnichannel retail technology solutions',
        'icon': 'fas fa-shopping-cart',
        'services': ['Mobile Applications', 'Cloud Solutions', 'AI Solutions']
    },
    'manufacturing': {
        'name': 'Manufacturing',
        'description': 'IoT and Industry 4.0 solutions',
        'icon': 'fas fa-industry',
        'services': ['AI Solutions', 'Enterprise Solutions', 'Custom Software']
    },
    'education': {
        'name': 'Education',
        'description': 'EdTech platforms and learning management systems',
        'icon': 'fas fa-graduation-cap',
        'services': ['Web Development', 'Mobile Applications', 'Cloud Solutions']
    },
    'government': {
        'name': 'Government',
        'description': 'Secure, compliant government technology solutions',
        'icon': 'fas fa-landmark',
        'services': ['Enterprise Solutions', 'Cloud Solutions', 'Custom Software']
    },
    'enterprise': {
        'name': 'Enterprise',
        'description': 'Scalable enterprise solutions for large organizations',
        'icon': 'fas fa-building',
        'services': ['Enterprise Solutions', 'AI Solutions', 'Cloud Solutions', 'Custom Software']
    }
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
