"""
Centralized Content Data Configuration
Contains all service details, industry data, and SEO metadata
This improves maintainability and allows for easy updates
"""

# Service Details with SEO Metadata
SERVICE_DETAILS = {
    'software-development': {
        'name': 'Software Development',
        'description': 'Custom software engineering solutions for web, mobile, desktop, and enterprise applications using modern, scalable architectures.',
        'keywords': 'software development, web development, mobile apps, enterprise software, custom development',
        'full_description': 'Custom software engineering solutions for web, mobile, desktop, and enterprise applications using modern, scalable architectures.',
        'benefits': [
            'Full-stack development expertise',
            'Modern technology stack',
            'Agile development methodology',
            'Scalable architecture design',
            'Performance optimization'
        ],
        'technologies': ['Python', 'Java', 'Node.js', 'React', 'Angular', 'Vue.js', 'AWS', 'Azure', 'Docker', 'Kubernetes'],
        'case_studies': ['E-commerce Platform Modernization', 'Enterprise Mobile App', 'Cloud Migration Success']
    },
    'ai-machine-learning': {
        'name': 'AI & Machine Learning',
        'description': 'Custom AI systems, automation platforms, data-driven intelligence, and advanced analytics for smarter decision-making.',
        'keywords': 'artificial intelligence, machine learning, AI solutions, data analytics, automation',
        'full_description': 'Custom AI systems, automation platforms, data-driven intelligence, and advanced analytics for smarter decision-making.',
        'benefits': [
            'Machine learning model development',
            'Natural language processing',
            'Computer vision solutions',
            'Predictive analytics',
            'AI-driven automation'
        ],
        'technologies': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-learn', 'Keras', 'OpenCV', 'NLP Libraries'],
        'case_studies': ['Fraud Detection System', 'Demand Forecasting AI', 'Customer Sentiment Analysis']
    },
    'bpo-services': {
        'name': 'BPO Services',
        'description': 'High-quality voice and non-voice support, CRM-driven chat operations, and customer engagement services.',
        'keywords': 'BPO services, customer support, business process outsourcing, customer engagement',
        'full_description': 'High-quality voice and non-voice support, CRM-driven chat operations, and customer engagement services.',
        'benefits': [
            'Cost-effective operations',
            '24/7 customer support',
            'Multi-lingual capabilities',
            'Quality assurance programs',
            'Scalable team management'
        ],
        'technologies': ['Salesforce', 'Zendesk', 'Five9', 'NICE Systems', 'Avaya'],
        'case_studies': ['Customer Support Center', 'Back Office Operations', 'Technical Support']
    },
    'it-consulting': {
        'name': 'IT Consulting',
        'description': 'Strategic IT consulting and technical architecture services for organizational transformation and digital strategy.',
        'keywords': 'IT consulting, technology strategy, digital transformation, enterprise architecture',
        'full_description': 'Strategic IT consulting and technical architecture services for organizational transformation and digital strategy.',
        'benefits': [
            'Technology strategy planning',
            'Infrastructure optimization',
            'Security assessment',
            'Digital transformation roadmap',
            'Cost optimization'
        ],
        'technologies': ['Cloud Platforms', 'DevOps', 'Security Tools', 'Monitoring Solutions'],
        'case_studies': ['Digital Transformation', 'Cloud Strategy', 'Infrastructure Modernization']
    },
    'rpo-staffing': {
        'name': 'RPO & Staffing',
        'description': 'Recruitment Process Outsourcing and staffing solutions for building and scaling your team with qualified professionals.',
        'keywords': 'staffing services, recruitment, talent acquisition, RPO, HR services',
        'full_description': 'Recruitment Process Outsourcing and staffing solutions for building and scaling your team with qualified professionals.',
        'benefits': [
            'Pre-vetted talent pipeline',
            'Faster hiring cycles',
            'Reduced recruitment costs',
            'Quality assurance in hiring',
            'Flexible engagement models'
        ],
        'technologies': [],
        'case_studies': ['Tech Talent Acquisition', 'Global Staffing', 'Specialized Hiring']
    },
    'digital-products': {
        'name': 'Digital Products',
        'description': 'Building scalable digital products from concept to market, with focus on user experience and business impact.',
        'keywords': 'digital products, product development, SaaS, startup, product strategy',
        'full_description': 'Building scalable digital products from concept to market, with focus on user experience and business impact.',
        'benefits': [
            'Product strategy consulting',
            'MVP development',
            'User experience design',
            'Market validation',
            'Growth optimization'
        ],
        'technologies': ['React', 'Node.js', 'MongoDB', 'Firebase', 'AWS'],
        'case_studies': ['SaaS Platform Launch', 'Mobile App Launch', 'Platform Scaling']
    }
}

# Industries Data with Solutions
INDUSTRIES_DATA = {
    'healthcare': {
        'name': 'Healthcare',
        'icon': 'fa-hospital',
        'description': 'Advanced solutions for modern healthcare providers, patient management, and medical innovations.',
        'content': 'Healthcare systems require secure, HIPAA-compliant solutions that improve patient outcomes and operational efficiency. Our healthcare experts have delivered enterprise platforms for hospitals, clinics, pharmaceutical companies, and medical device manufacturers worldwide.',
        'solutions': [
            'Electronic Health Records (EHR) Systems',
            'Telemedicine Platforms',
            'Patient Management Systems',
            'Medical Device Integration',
            'Healthcare Analytics & Reporting',
            'HIPAA-Compliant Infrastructure'
        ]
    },
    'education': {
        'name': 'Education',
        'icon': 'fa-graduation-cap',
        'description': 'Comprehensive educational technology solutions for institutions and learning platforms.',
        'content': 'Education technology transformation is essential for modern institutions. We deliver Learning Management Systems (LMS), student information systems, and digital learning platforms that engage students and streamline administration.',
        'solutions': [
            'Learning Management Systems (LMS)',
            'Student Information Systems',
            'Virtual Classroom Platforms',
            'Digital Assessment Tools',
            'Educational Analytics',
            'Online Exam & Proctoring Solutions'
        ]
    },
    'retail': {
        'name': 'Retail & E-commerce',
        'icon': 'fa-shopping-cart',
        'description': 'E-commerce and retail transformation solutions for omnichannel excellence.',
        'content': 'Retail companies need seamless omnichannel experiences. We build e-commerce platforms, point-of-sale systems, inventory management, and customer engagement solutions that drive sales and loyalty.',
        'solutions': [
            'E-commerce Platforms',
            'Point of Sale (POS) Systems',
            'Inventory Management',
            'Customer Loyalty Programs',
            'Mobile Shopping Apps',
            'Omnichannel Integration'
        ]
    },
    'manufacturing': {
        'name': 'Manufacturing',
        'icon': 'fa-industry',
        'description': 'Industry 4.0 solutions including IoT, automation, and smart factory implementations.',
        'content': 'Manufacturing companies are transforming through Industry 4.0 technologies. We implement IoT sensors, predictive maintenance, supply chain optimization, and smart factory solutions.',
        'solutions': [
            'IoT & Sensor Networks',
            'Predictive Maintenance',
            'Production Planning & Scheduling',
            'Supply Chain Optimization',
            'Quality Control Systems',
            'Industrial Analytics'
        ]
    },
    'finance': {
        'name': 'Financial Services',
        'icon': 'fa-university',
        'description': 'Fintech solutions, digital banking, and financial services modernization.',
        'content': 'Financial institutions require secure, compliant, and cutting-edge technology solutions. We deliver digital banking platforms, trading systems, risk management, and regulatory compliance solutions.',
        'solutions': [
            'Digital Banking Platforms',
            'Payment Processing Systems',
            'Risk Management Solutions',
            'Regulatory Compliance Software',
            'Trading & Investment Platforms',
            'Fraud Detection Systems'
        ]
    },
    'enterprise': {
        'name': 'Enterprise',
        'icon': 'fa-users',
        'description': 'Large-scale enterprise solutions for complex business operations and transformation.',
        'content': 'Large enterprises demand robust, scalable solutions that integrate across multiple systems and geographies. We deliver enterprise ERP, CRM, business intelligence, and digital transformation services.',
        'solutions': [
            'ERP Implementation',
            'CRM Solutions',
            'Business Intelligence',
            'Cloud Migration',
            'Enterprise Integration',
            'Digital Transformation'
        ]
    }
}


def get_service_details(slug):
    """Retrieve service details by slug"""
    return SERVICE_DETAILS.get(slug.lower())


def get_all_services_details():
    """Get all service details"""
    return SERVICE_DETAILS


def get_industry_details(slug):
    """Retrieve industry details by slug"""
    return INDUSTRIES_DATA.get(slug.lower())


def get_all_industries():
    """Get all industry details"""
    return INDUSTRIES_DATA
