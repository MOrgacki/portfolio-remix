import reflex as rx
from typing import List, Dict, Any, Optional
from portfolio.header import Header
from portfolio.footer import Footer
from portfolio.sidebar import sidebar
from portfolio.animations import animated_background, animations_css
from portfolio.loader import page_transition_loader
from portfolio.floating_button import floating_language_button
from portfolio.main import contact_section
from portfolio.translations import get_translation, TRANSLATIONS
from state import State

def get_project_description(project_id: int, lang: str = "en") -> str:
    """Get translated project description"""
    return get_translation(lang, f"proj_desc_{project_id}")

def get_current_language() -> str:
    """Helper to get current language from State"""
    try:
        from state import State as MainState
        # Access the state router's current state
        import reflex as rx
        if hasattr(rx, 'state') and hasattr(rx.state, 'state_manager'):
            return "en"  # Default fallback
        return "en"
    except:
        return "en"

# Sample project data structure
PROJECT_FIELDS = ["id", "title", "description", "technologies", "domain", "platform", "github", "demo", "image", "status"]

# Static filter data
PLATFORMS = ["All", "Web", "Mobile", "Desktop", "AI/Automation"]
DOMAINS = ["All", "Waste Management", "Fintech", "Automotive IoT", "Construction", "E-learning", "Transport", "HR Tech", "Blockchain", "Web3", "AI", "Health & Fitness", "Testing"]
PROJECT_TYPES = ["All", "Personal Projects", "Client Projects"]

# Technology categories
TECH_CATEGORIES = {
    "Programming Languages": {
        "techs": ["Python", "JavaScript", "TypeScript", "C#", "PHP", "C++", "Bash", "Go", "Rust"],
        "color": "cyan",
        "bg": "rgba(0, 212, 255, 0.1)",
        "border": "rgba(0, 212, 255, 0.3)"
    },
    "Testing Tools": {
        "techs": ["Selenium", "Cypress", "Playwright", "Pytest", "NUnit", "PHPUnit", "Karma", "Codeception", "TestCafe", "Postman", "Fiddler", "Fiddler Classic", "OWASP ZAP", "Proxyman", "API Testing"],
        "color": "blue",
        "bg": "rgba(91, 115, 255, 0.1)",
        "border": "rgba(91, 115, 255, 0.3)"
    },
    "Databases": {
        "techs": ["MySQL", "PostgreSQL", "MongoDB", "Redis", "T-SQL", "NoSQL", "MariaDB", "TimescaleDB", "SQL", "Database", "Database Integration", "Vector Database"],
        "color": "purple",
        "bg": "rgba(139, 92, 246, 0.1)",
        "border": "rgba(139, 92, 246, 0.3)"
    },
    "Frameworks & Technologies": {
        "techs": ["React", "Angular", "Vue.js", "Laravel", "Symfony", "Django", "Flask", "FastAPI", "Node.js", ".NET", ".NET Core", ".NET Framework", "ASP .NET", "ASP .NET Core", "React Native", "Flutter", "Xamarin", "WPF", "MFC", "Redux", "Web3", "Blockchain", "AI", "Smart Contracts", "DePIN"],
        "color": "pink",
        "bg": "rgba(236, 72, 153, 0.1)",
        "border": "rgba(236, 72, 153, 0.3)"
    },
    "DevOps & Tools": {
        "techs": ["Docker", "Jenkins", "GitLab", "GitHub", "TFS", "Octopus", "AWS", "Cloud", "CI/CD"],
        "color": "green",
        "bg": "rgba(34, 197, 94, 0.1)",
        "border": "rgba(34, 197, 94, 0.3)"
    },
    "Other": {
        "techs": ["REST API", "API", "Payment Gateway", "SSO", "Azure AD", "Okta", "GPS", "Push Notifications", "WebOS", "Tizen", "Android TV", "iOS", "Android", "Mobile", "RPA", "Image Processing", "Automation", "Web Scraping", "CSV", "Logging", "Error Handling", "Multi-chain", "MetaMask", "Crypto Wallet", "ERC-20", "BNB Chain", "Solana", "Bridge Protocol", "Airdrop", "Investment Platform", "Admin Panel", "Client Portal", "Report System", "PDF Generation", "Cart Optimization", "Algorithm Testing", "Payment Integration", "Shipping Logic", "Banking Integration", "CRM", "Financial Systems", "Security Testing", "Inventory Management", "Supply Chain", "Logistics", "Product Catalog", "Wallet Integrations", "HTTP", "Crypto Payments", "Decentralized Network", "Node Infrastructure", "Smart TV", "Hardware", "GPU Computing", "LMS", "ATS", "ADB", "Simulators", "Celery", "E-commerce", "OpenAPI", "Pixel Detection", "Async Coroutines", "Requests", "Data Analysis", "Browser Automation", "Data Export", "NFT", "OpenSea"],
        "color": "orange",
        "bg": "rgba(251, 191, 36, 0.1)",
        "border": "rgba(251, 191, 36, 0.3)"
    }
}

PROJECTS_DATA = [
    # Client Projects
    {
        "id": 1,
        "title": "Waste Management Platform",
        "description": "Web application for comprehensive waste management for small and medium enterprises. Ensured full compliance with Polish waste management regulations and verified integration with MOS API and payment systems.",
        "technologies": ["ASP .NET", "Angular", "Jenkins", "Octopus", "MySQL", "Karma", "NUnit"],
        "domain": "Waste Management",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/project1.png",
        "status": "Completed",
        "achievements": [
            "100% compliance with Polish waste management regulations",
            "Zero critical bugs in MOS API integration",
            "Verified all payment system integrations"
        ]
    },
    {
        "id": 2,
        "title": "Fintech Banking Platform",
        "description": "Comprehensive fintech platform for Swiss bank. Implemented SonarQube static analysis and TestCafe GUI automation, reducing production bugs by 35%. Built QA process from scratch, cutting testing costs by 40%.",
        "technologies": [".NET Framework", "WPF", "Angular", "T-SQL", "TestCafe", "NUnit", "OWASP ZAP"],
        "domain": "Fintech",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/project2.png",
        "status": "Completed",
        "achievements": [
            "35% reduction in production bugs",
            "40% decrease in testing costs",
            "Built QA process from scratch",
            "Eliminated all high-risk security vulnerabilities"
        ]
    },
    {
        "id": 3,
        "title": "IoT Agricultural Machinery Platform",
        "description": "Web application for communication and management of agricultural machines using CAN/CAM standard. Conducted comprehensive security testing with OWASP ZAP, identifying 12 security vulnerabilities before production.",
        "technologies": ["ASP .NET Core", "Angular", "T-SQL", "Karma", "NUnit", "OWASP ZAP"],
        "domain": "Automotive IoT",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/project3.png",
        "status": "Completed",
        "achievements": [
            "Identified 12 security vulnerabilities before production",
            "Created complete English documentation",
            "50% faster user onboarding"
        ]
    },
    {
        "id": 4,
        "title": "Mobile Banking & Leasing App",
        "description": "Mobile application for Swiss bank leasing management with AI features (face recognition, fingerprint). Tested AI integration achieving 99.9% accuracy and identified 15+ critical biometric security bugs.",
        "technologies": ["Xamarin", "T-SQL", "Proxyman", "NUnit"],
        "domain": "Fintech",
        "platform": "Mobile",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/project4.png",
        "status": "Completed",
        "achievements": [
            "99.9% AI accuracy in production",
            "15+ critical biometric security bugs identified",
            "Zero security incidents post-launch"
        ]
    },
    {
        "id": 5,
        "title": "Construction Engineering Software",
        "description": "Software package for construction engineers for structural analysis. Implemented guided exploratory testing methodology, increasing test coverage by 60%. Identified and fixed 8 memory leaks, improving stability by 45%.",
        "technologies": ["C#", "WPF", "C++", "MFC", "TFS", "Jenkins", "NUnit", "Xmind"],
        "domain": "Construction",
        "platform": "Desktop",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/project5.png",
        "status": "Completed",
        "achievements": [
            "60% increase in test coverage",
            "45% stability improvement",
            "Fixed 8 critical memory leaks"
        ]
    },
    {
        "id": 6,
        "title": "Insurance Comparison Platform",
        "description": "Insurance comparison platform with whitelabel distribution capability. Automated 80% of critical API endpoints with Codeception (PHP) and created utility tools reducing manual testing by 70%.",
        "technologies": ["PHP", "Symfony", "Angular", "Redux", "Codeception", "PHPUnit"],
        "domain": "Fintech",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/insurance_App.png",
        "status": "Completed",
        "achievements": [
            "80% API endpoint automation coverage",
            "70% reduction in manual testing time",
            "50% faster regression testing"
        ]
    },
    {
        "id": 7,
        "title": "Multi-Platform E-learning System",
        "description": "E-learning platform with web, TV, and mobile support. Ensured proper functionality on TV browsers across 5+ smart TV platforms and identified 20+ bugs in admin module before release.",
        "technologies": ["PHP", "Laravel", "Redux", "React Native", "React", "PHPUnit"],
        "domain": "E-learning",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/tv_app.png",
        "status": "Completed",
        "achievements": [
            "5+ smart TV platforms compatibility",
            "20+ bugs prevented in admin module",
            "Zero critical issues in production"
        ]
    },
    {
        "id": 8,
        "title": "Transport & Logistics Mobile App",
        "description": "Mobile app for customers and drivers enabling ride booking, real-time GPS tracking, and notifications. Tested GPS tracking achieving 98% positioning accuracy and ensured offline functionality.",
        "technologies": ["React Native", "GPS", "API", "Push Notifications"],
        "domain": "Transport",
        "platform": "Mobile",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/project8.png",
        "status": "Completed",
        "achievements": [
            "98% GPS positioning accuracy",
            "Full offline functionality verified",
            "10+ critical push notification bugs fixed"
        ]
    },
    {
        "id": 21,
        "title": "Transport E-Commerce Ticket Platform",
        "description": "E-commerce web platform for purchasing bus and train tickets with seat selection, payment processing, and booking management. Tested payment gateway integrations with multiple providers ensuring 99.9% transaction success rate. Verified seat reservation system preventing double bookings.",
        "technologies": ["React", "Node.js", "Payment Gateway", "REST API", "PostgreSQL", "Redis"],
        "domain": "Transport",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/transport_ticket.png",
        "status": "Completed",
        "achievements": [
            "99.9% payment transaction success rate",
            "Zero double-booking incidents",
            "Tested 5+ payment gateway integrations",
            "Verified real-time seat availability accuracy"
        ]
    },
    {
        "id": 9,
        "title": "HR Interview Intelligence Platform",
        "description": "Training platform and interview intelligence tool with AI-powered analytics. Tested SSO integrations with Azure AD and Okta for 10,000+ enterprise users and verified 15+ AI algorithm bugs.",
        "technologies": ["AI", "SSO", "Azure AD", "Okta", "LMS", "ATS"],
        "domain": "HR Tech",
        "platform": "AI/Automation",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/ai_hire_app.png",
        "status": "Completed",
        "achievements": [
            "10,000+ enterprise users seamless authentication",
            "15+ AI algorithm bugs identified",
            "GDPR and SOC 2 compliance verified"
        ]
    },
    {
        "id": 10,
        "title": "Web3 Gaming & Crypto Platform",
        "description": "Web3 platform for account management, crypto wallet, and blockchain processes. Built QA strategy from scratch, leading team of 3 testers. Implemented E2E automation with Cypress, increasing coverage from 10% to 75%.",
        "technologies": ["Laravel", "Vue.js", "Django", "Docker", "Redis", "MySQL", "Cypress", "Playwright"],
        "domain": "Blockchain",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/minig_web.png",
        "status": "Completed",
        "achievements": [
            "75% test coverage (from 10%)",
            "60% reduction in production bugs",
            "Led team of 3 QA engineers"
        ]
    },
    {
        "id": 11,
        "title": "Web3 Gaming Mobile App - Rewards Marketplace",
        "description": "Flutter-based mobile application for Web3 gaming platform featuring marketplace for exchanging crypto rewards for real-world benefits. Integrated MetaMask wallet connectivity for secure transactions. Tested reward code exchange system for Żabka store vouchers and other partner benefits. Used Fiddler Classic for API testing and traffic analysis to ensure secure payment flows and reward distribution.",
        "technologies": ["Flutter", "MetaMask", "Web3", "Mobile", "Fiddler Classic", "API Testing", "Crypto Wallet"],
        "domain": "Blockchain",
        "platform": "Mobile",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/mining_app_mobile.png",
        "status": "Completed",
        "achievements": [
            "MetaMask wallet integration tested",
            "Secure reward exchange system verified",
            "API traffic analysis with Fiddler Classic"
        ]
    },
    {
        "id": 12,
        "title": "Medical Supplements E-commerce Platform",
        "description": "E-commerce platform for medical supplements featuring intelligent cart optimization system. Tested advanced algorithm that automatically assembles product combinations in the most cost-effective and fastest delivery form. Verified smart bundling logic, pricing calculations, and checkout flow to ensure customers receive optimal product packages with best value and shortest delivery times.",
        "technologies": ["E-commerce", "Cart Optimization", "Algorithm Testing", "Payment Integration", "Shipping Logic"],
        "domain": "E-commerce",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "",
        "status": "Completed",
        "achievements": [
            "Smart cart optimization algorithm verified",
            "Cost-effective bundling tested",
            "Delivery optimization validated"
        ]
    },
    {
        "id": 13,
        "title": "Banking Products Sales Platform",
        "description": "Web application for bank employees to offer and sell financial products to retail customers. Platform integrated with major Swiss bank database infrastructure, enabling real-time product catalog access, customer data management, and transaction processing. Tested complex workflows for product recommendations, customer onboarding, compliance checks, and sales tracking. Verified secure integration with banking systems and data synchronization across distributed architecture.",
        "technologies": ["Banking Integration", "Database Integration", "CRM", "Financial Systems", "Security Testing", "API Integration"],
        "domain": "Fintech",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/elearning.png",
        "status": "Completed",
        "achievements": [
            "Swiss bank database integration verified",
            "Complex sales workflows tested",
            "Secure financial data handling validated"
        ]
    },
    {
        "id": 14,
        "title": "Welding Industry Management Platform",
        "description": "Symfony-based web platform for welding industry enabling clients to submit quotes, review completed welding tests, order new inspections, and generate reports. Tested quote submission workflows, test result viewing, inspection ordering system, and automated report generation. Successfully deployed to production environment. Verified data integrity, PDF report generation, and customer notification systems.",
        "technologies": ["PHP", "Symfony", "MySQL", "PDF Generation", "Report System", "Client Portal"],
        "domain": "Industry",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/weld_app.png",
        "status": "Completed",
        "achievements": [
            "Successfully deployed to production",
            "Quote and inspection system verified",
            "Automated report generation tested"
        ]
    },
    {
        "id": 15,
        "title": "Oil & Gas Tubular Goods Management System",
        "description": "Web platform for managing Oil Country Tubular Goods (OCTG) inventory, drilling operations, and supply chain logistics. System handles tubular product catalog, inventory tracking, logistics coordination, and order management for oil and gas drilling operations. Tested complex workflows for product specifications, inventory management, order processing, and supply chain integration. Verified data accuracy for technical product specifications and delivery tracking.",
        "technologies": ["Inventory Management", "Supply Chain", "Logistics", "Database", "API Integration", "Product Catalog"],
        "domain": "Oil & Gas",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/oil_app.png",
        "status": "Completed",
        "achievements": [
            "Complex inventory system verified",
            "Supply chain workflows tested",
            "Technical specifications validated"
        ]
    },
    {
        "id": 16,
        "title": "Web3 Staking & Vesting Platform",
        "description": "Web3 application built in Laravel for staking, vesting, and ranking mechanisms. Tested staking smart contract integrations, vesting schedules, and ranking algorithms. Verified multi-chain support and Web3 wallet integrations across different blockchain networks.",
        "technologies": ["Laravel", "Web3", "Blockchain", "Smart Contracts", "Multi-chain", "Wallet Integrations"],
        "domain": "Blockchain",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/staking_app.png",
        "status": "Completed",
        "achievements": [
            "Multi-chain integration tested successfully",
            "Zero critical bugs in staking mechanisms",
            "Seamless Web3 wallet connectivity across chains",
            "Verified vesting schedules accuracy"
        ]
    },
    {
        "id": 18,
        "title": "Web3 Gamification Platform",
        "description": "Web3 platform combining gamification and blockchain. Implemented QA processes and E2E/API automation from scratch, improving release stability by 50%. Tested Web3 wallet integrations ensuring seamless user onboarding.",
        "technologies": ["Web3", "Blockchain", "AI", "React", "API"],
        "domain": "Web3",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/ai_gamification_app.png",
        "status": "Completed",
        "achievements": [
            "50% improvement in release stability",
            "Seamless Web3 wallet onboarding",
            "Zero critical bugs in token mechanisms"
        ]
    },
    {
        "id": 19,
        "title": "Web3 Investment Panel",
        "description": "Investment panel for managing staking, vesting, ranking, and airdrop mechanisms across multiple blockchain networks. Tested multi-chain integrations and Web3 wallet connectivity ensuring smooth operations. Verified airdrop distribution mechanisms and investor portfolio tracking with no major bugs found.",
        "technologies": ["Web3", "Blockchain", "Multi-chain", "Smart Contracts", "Airdrop", "Investment Platform"],
        "domain": "Web3",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/panel_ai_gaminifaction.png",
        "status": "Completed",
        "achievements": [
            "Zero major bugs in airdrop distribution",
            "Successful multi-chain integration testing",
            "Verified staking and vesting accuracy",
            "Seamless ranking system implementation"
        ]
    },
    {
        "id": 20,
        "title": "Crypto Mining Mobile App",
        "description": "Mobile application built in Flutter for crypto mining and in-app purchases. Used Fiddler to capture and analyze HTTP traffic for debugging. Tested top-up mechanisms and cryptocurrency payment integrations for purchasing various in-app items.",
        "technologies": ["Flutter", "Fiddler", "HTTP", "Crypto Payments", "iOS", "Android", "Mobile"],
        "domain": "Blockchain",
        "platform": "Mobile",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/mining_app_mobile.png",
        "status": "Completed",
        "achievements": [
            "HTTP traffic analysis with Fiddler",
            "Verified crypto payment integrations",
            "Zero critical bugs in top-up mechanisms",
            "Successful in-app purchase testing"
        ]
    },
    {
        "id": 22,
        "title": "Token Distribution Panel & Multi-Chain Bridge",
        "description": "Token distribution panel with token release mechanisms on ERC-20 and cross-chain bridge functionality to BNB Chain and Solana. Tested smart contract integrations for token vesting, distribution schedules, and cross-chain bridge operations. Verified transaction integrity across multiple blockchain networks.",
        "technologies": ["Web3", "ERC-20", "BNB Chain", "Solana", "Smart Contracts", "Bridge Protocol", "Multi-chain"],
        "domain": "Blockchain",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/project22.png",
        "status": "Completed",
        "achievements": [
            "Verified token distribution across 3 blockchain networks",
            "Zero critical bugs in bridge transactions",
            "100% accuracy in vesting schedule releases",
            "Successful cross-chain interoperability testing"
        ]
    },
    {
        "id": 23,
        "title": "Client App & Partner Zone Platform",
        "description": "Partner system for purchasing gold, medals, wedding rings and jewelry. Dual-platform solution with client-facing application for browsing products, placing orders, and account management. Partner zone provides business partners with dashboard, commission tracking, order management, and analytics tools. Tested integrations between both platforms ensuring seamless data synchronization and inventory management.",
        "technologies": ["React", "Node.js", "REST API", "PostgreSQL", "Redis", "Admin Panel"],
        "domain": "E-commerce",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/pz.png",
        "status": "Completed",
        "achievements": [
            "Verified seamless data sync between client and partner platforms",
            "Tested role-based access control for 3 user types",
            "Zero critical bugs in commission calculation system",
            "Validated partner dashboard analytics accuracy"
        ]
    },
    {
        "id": 24,
        "title": "DePIN - Decentralized AI Network",
        "description": "Decentralized Physical Infrastructure Network (DePIN) platform built on decentralized network infrastructure delivering AI-powered content generation to Web3 communities. Tested decentralized node operations, AI content generation APIs, and blockchain-based reward distribution. Verified network stability and content delivery across distributed nodes.",
        "technologies": ["DePIN", "Web3", "AI", "Blockchain", "Decentralized Network", "Node Infrastructure", "API"],
        "domain": "AI",
        "platform": "AI/Automation",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/gentok.png",
        "status": "Completed",
        "achievements": [
            "Tested decentralized node network with 100+ active nodes",
            "Verified AI content generation across distributed infrastructure",
            "Zero critical bugs in blockchain reward distribution",
            "Validated network resilience and fault tolerance"
        ]
    },
    {
        "id": 25,
        "title": "Internal TV Display Application",
        "description": "Smart TV application designed for internal corporate displays showing company announcements, KPIs, dashboards, and real-time data. Tested across multiple TV hardware platforms ensuring compatibility with various screen resolutions and TV operating systems. Verified content synchronization, automatic updates, and display scheduling functionality.",
        "technologies": ["Smart TV", "Hardware", "WebOS", "Tizen", "Android TV", "React", "REST API"],
        "domain": "E-learning",
        "platform": "Desktop",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/project25.png",
        "status": "Completed",
        "achievements": [
            "Tested compatibility across 5+ smart TV platforms",
            "Verified 24/7 stability with zero crashes over 30 days",
            "Validated automatic content refresh and scheduling",
            "Ensured proper rendering on 4K and Full HD displays"
        ]
    },
    {
        "id": 12,
        "title": "AI-Powered GPU Computing App",
        "description": "Windows desktop app allowing users to share GPU power for AI computations and content generation. Tested GPU/Compute integrations and AI modules ensuring stable content generation. Verified rewards mechanisms achieving 100% accuracy.",
        "technologies": ["C#", ".NET", "GPU Computing", "AI"],
        "domain": "AI",
        "platform": "Desktop",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/mining_app.png",
        "status": "Completed",
        "achievements": [
            "100% accuracy in rewards mechanisms",
            "Stable AI content generation",
            "Optimized GPU resource usage"
        ]
    },
    {
        "id": 13,
        "title": "Generative AI API Platform",
        "description": "Unified API for integration with generative AI models offering text-to-image, text-to-speech, and video transcription. Tested all API endpoints ensuring 99.5% uptime and verified 95% accuracy rate for generated content.",
        "technologies": ["AI", "REST API", "Python", "Cloud"],
        "domain": "AI",
        "platform": "AI/Automation",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/deapi.png",
        "status": "Completed",
        "achievements": [
            "99.5% API uptime",
            "95% content accuracy rate",
            "1000+ concurrent requests supported"
        ]
    },
    {
        "id": 14,
        "title": "Brainwave Meditation Mobile App",
        "description": "Mobile meditation app with EEG data analysis and brainwave-based coaching. 5/5 star rating in stores. Tested app using hardware EEG device integrations (MUSE) ensuring stable connection in 98% of sessions.",
        "technologies": ["Hardware", "React", "React Native", "iOS", "Android", "ADB", "Simulators", "Django", "Python", "Playwright", "Pytest", "Docker", "Celery", "Redis"],
        "domain": "Health & Fitness",
        "platform": "Mobile",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/meditation_app.png",
        "status": "Completed",
        "achievements": [
            "Prepared successful strategy when joining the project making able to release the product to stores",
            "Successful migration from MQTT processing to Local processing without critical production found",
            "Prepared complex custom automation framework combining Playwright, Requests, Pytest in Python speeding the release process by about 50%, implemented that in CI/CD",
            "Implemented a few AI agents solving problem of no PM and no Junior QA in Project"
        ]
    },
    {
        "id": 15,
        "title": "Professional Development E-learning Platform",
        "description": "E-learning platform combining online courses with social features similar to LinkedIn Learning. Tested course system ensuring proper progress tracking for 5,000+ users and verified AI recommendation algorithms achieving 85% satisfaction.",
        "technologies": ["React", "Angular", "Vue", "API", "AI"],
        "domain": "E-learning",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/project15.png",
        "status": "Completed",
        "achievements": [
            "5,000+ users proper progress tracking",
            "85% AI recommendation satisfaction",
            "Zero critical authentication bugs"
        ]
    },

    # Personal Projects
    {
        "id": 16,
        "title": "MMORPG Game Bot - Tibia Automation",
        "description": "Pixel-based automation bot for Tibia MMORPG game with smart in-game function automation, designed to bypass BattlEye anti-cheat protection. Optimized for 800x600 resolution for performance. Features include map navigation via pixel detection, monster detection and combat, auto-chase mode, health/mana management, auto-looting, and food consumption. Implemented using async coroutines, RPA techniques, and image processing with comprehensive Pytest coverage.",
        "technologies": ["Python", "RPA", "Image Processing", "Async Coroutines", "Pytest", "Pixel Detection", "Automation"],
        "domain": "Gaming",
        "platform": "Desktop",
        "project_type": "Personal Projects",
        "github": "https://github.com/MOrgacki?tab=repositories",
        "demo": "",
        "image": "",
        "status": "Completed",
        "achievements": [
            "BattlEye anti-cheat bypass implemented",
            "Pixel-based map navigation system",
            "Async automation with coroutines",
            "Comprehensive test coverage with Pytest"
        ]
    },
    {
        "id": 17,
        "title": "Job Market Statistics Web Scraper",
        "description": "Python web scraper for collecting job market statistics and storing data in MongoDB database. Utilizes Selenium for browser automation to navigate dynamic job listing pages and requests library for HTTP requests. Automatically extracts job data including titles, salaries, locations, and requirements, then aggregates statistics for market analysis.",
        "technologies": ["Python", "Selenium", "MongoDB", "Web Scraping", "Requests", "Data Analysis", "Browser Automation"],
        "domain": "Data Analysis",
        "platform": "AI/Automation",
        "project_type": "Personal Projects",
        "github": "https://github.com/MOrgacki?tab=repositories",
        "demo": "",
        "image": "",
        "status": "Completed",
        "achievements": [
            "Automated job data collection",
            "MongoDB integration for data storage",
            "Market statistics aggregation"
        ]
    },
    {
        "id": 18,
        "title": "Job Listings Web Scraper with CSV Export",
        "description": "Python web scraper for extracting job offer listings from job portals. Features robust error handling with exception logging to text files and exports scraped data to CSV format for easy analysis. Implements retry logic and handles dynamic content loading to ensure reliable data collection.",
        "technologies": ["Python", "Web Scraping", "CSV", "Logging", "Error Handling", "Data Export"],
        "domain": "Data Analysis",
        "platform": "AI/Automation",
        "project_type": "Personal Projects",
        "github": "https://github.com/MOrgacki?tab=repositories",
        "demo": "",
        "image": "",
        "status": "Completed",
        "achievements": [
            "Robust exception handling and logging",
            "CSV data export functionality",
            "Automated job listing extraction"
        ]
    },
    {
        "id": 19,
        "title": "Automated Testing Frameworks",
        "description": "Collection of custom testing frameworks and utilities for automated testing across different platforms and technologies.",
        "technologies": ["Python", "Selenium", "Pytest", "Docker"],
        "domain": "Testing",
        "platform": "AI/Automation",
        "project_type": "Personal Projects",
        "github": "https://github.com/MOrgacki?tab=repositories",
        "demo": "",
        "image": "/project16.png",
        "status": "In Progress",
        "achievements": [
            "Multi-platform support",
            "Reusable test utilities",
            "Open source contributions"
        ]
    },
    {
        "id": 17,
        "title": "API Integration Tools",
        "description": "Custom tools and scripts for API testing, integration verification, and data quality validation.",
        "technologies": ["Python", "REST", "Postman", "OpenAPI"],
        "domain": "Testing",
        "platform": "AI/Automation",
        "project_type": "Personal Projects",
        "github": "https://github.com/MOrgacki?tab=repositories",
        "demo": "",
        "image": "/project17.png",
        "status": "In Progress",
        "achievements": [
            "Automated API validation",
            "Data quality checks",
            "Integration testing utilities"
        ]
    },
    {
        "id": 26,
        "title": "NFT Marketplace Platform",
        "description": "NFT marketplace platform with OpenSea integration enabling users to trade, buy, and sell NFTs. Backend built with Go for high-performance API services and Rust for blockchain smart contract interactions. Tested NFT minting, trading workflows, wallet integrations, and OpenSea API compatibility. Verified transaction security, gas optimization, and metadata handling across multiple blockchain networks.",
        "technologies": ["Go", "Rust", "Web3", "Blockchain", "NFT", "OpenSea", "Smart Contracts", "API", "Crypto Wallet"],
        "domain": "Blockchain",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "",
        "status": "Completed",
        "achievements": [
            "OpenSea API integration tested successfully",
            "Verified NFT minting and trading workflows",
            "Zero critical bugs in wallet integrations",
            "Gas optimization validated across multiple chains"
        ]
    },
    {
        "id": 27,
        "title": "AI Research Analysis Platform (RAG)",
        "description": "AI-powered SaaS platform for analyzing scientific papers and research documents using Retrieval-Augmented Generation. React Native frontend, FastAPI backend, vector database for semantic indexing, PostgreSQL for structured data. Evolved into a microservice for enterprise research teams.",
        "technologies": ["Python", "TypeScript", "React Native", "FastAPI", "PostgreSQL", "Vector Database", "AI", "REST API", "Docker", "Pytest"],
        "domain": "AI",
        "platform": "Web",
        "project_type": "Client Projects",
        "github": "",
        "demo": "",
        "image": "/ai_app.png",
        "status": "Completed",
        "achievements": [
            "Pre-production functional audit identified 25+ critical issues before launch",
            "Zero critical defects in production release",
            "Built QA standards and test automation framework from scratch",
            "As Technical Lead: designed and delivered RAG pipeline for semantic document indexing",
            "Scaled platform to SaaS microservice architecture serving enterprise research teams"
        ]
    }
]

def _compute_popular_rest_techs(category: str, top_n: int):
    all_used: set = set()
    for p in PROJECTS_DATA:
        all_used.update(p["technologies"])
    techs = [t for t in TECH_CATEGORIES.get(category, {}).get("techs", []) if t in all_used]
    counts: Dict[str, int] = {}
    for p in PROJECTS_DATA:
        for t in p["technologies"]:
            if t in techs:
                counts[t] = counts.get(t, 0) + 1
    popular = sorted(techs, key=lambda x: counts.get(x, 0), reverse=True)[:top_n]
    rest = sorted([t for t in techs if t not in set(popular)])
    return popular, rest

_PROG_LANG_POPULAR, _PROG_LANG_REST = _compute_popular_rest_techs("Programming Languages", 4)
_TESTING_TOOLS_POPULAR, _TESTING_TOOLS_REST = _compute_popular_rest_techs("Testing Tools", 5)
_DATABASES_POPULAR, _DATABASES_REST = _compute_popular_rest_techs("Databases", 4)
_FRAMEWORKS_POPULAR, _FRAMEWORKS_REST = _compute_popular_rest_techs("Frameworks & Technologies", 5)
_DEVOPS_POPULAR, _DEVOPS_REST = _compute_popular_rest_techs("DevOps & Tools", 4)
_OTHER_POPULAR, _OTHER_REST = _compute_popular_rest_techs("Other", 5)

def _compute_popular_rest_domains(top_n: int):
    counts: Dict[str, int] = {}
    for p in PROJECTS_DATA:
        d = p.get("domain", "")
        if d:
            counts[d] = counts.get(d, 0) + 1
    no_all = [d for d in DOMAINS if d != "All"]
    by_count = sorted(no_all, key=lambda x: counts.get(x, 0), reverse=True)
    return ["All"] + by_count[:top_n], by_count[top_n:]

_DOMAINS_POPULAR, _DOMAINS_REST = _compute_popular_rest_domains(5)

_SHOW_MORE_BTN_STYLE = {
    "color": "#64748b",
    "fontSize": "0.7rem",
    "padding": "0.1rem 0.4rem",
    "cursor": "pointer",
    "border": "1px solid rgba(100, 116, 139, 0.2)",
    "borderRadius": "0.4rem",
    "background": "rgba(30, 41, 59, 0.3)",
    "_hover": {
        "color": "#94a3b8",
        "background": "rgba(30, 41, 59, 0.5)"
    }
}


class ProjectsState(State):
    selected_technologies: List[str] = ["All"]
    selected_domain: str = "All"
    selected_platform: str = "All"
    selected_project_type: str = "All"
    search_query: str = ""
    show_modal: bool = False

    # Selected project details
    selected_title: str = ""
    selected_description: str = ""
    selected_domain_badge: str = ""
    selected_platform_badge: str = ""
    selected_technologies_list: List[str] = []
    selected_achievements_list: List[str] = []
    selected_github: str = ""
    selected_demo: str = ""
    selected_project_id: int = 0

    show_more_programming_languages: bool = False
    show_more_testing_tools: bool = False
    show_more_databases: bool = False
    show_more_frameworks: bool = False
    show_more_devops: bool = False
    show_more_other: bool = False
    show_more_domains: bool = False

    @rx.var
    def all_technologies(self) -> List[str]:
        """Get all unique technologies from projects"""
        techs = set()
        for project in PROJECTS_DATA:
            techs.update(project["technologies"])
        return ["All"] + sorted(list(techs))

    @rx.var
    def categorized_technologies(self) -> Dict[str, Dict[str, Any]]:
        """Get technologies grouped by category"""
        all_techs = set()
        for project in PROJECTS_DATA:
            all_techs.update(project["technologies"])

        result = {}
        for category, data in TECH_CATEGORIES.items():
            category_techs = [tech for tech in data["techs"] if tech in all_techs]
            if category_techs:
                result[category] = {
                    "techs": sorted(category_techs),
                    "color": data["color"],
                    "bg": data["bg"],
                    "border": data["border"]
                }
        return result

    @rx.var
    def programming_languages_techs(self) -> List[str]:
        """Get programming languages technologies"""
        return self.categorized_technologies.get("Programming Languages", {}).get("techs", [])

    @rx.var
    def testing_tools_techs(self) -> List[str]:
        """Get testing tools technologies"""
        return self.categorized_technologies.get("Testing Tools", {}).get("techs", [])

    @rx.var
    def databases_techs(self) -> List[str]:
        """Get databases technologies"""
        return self.categorized_technologies.get("Databases", {}).get("techs", [])

    @rx.var
    def frameworks_techs(self) -> List[str]:
        """Get frameworks & technologies"""
        return self.categorized_technologies.get("Frameworks & Technologies", {}).get("techs", [])

    @rx.var
    def devops_techs(self) -> List[str]:
        """Get DevOps & Tools technologies"""
        return self.categorized_technologies.get("DevOps & Tools", {}).get("techs", [])

    @rx.var
    def other_techs(self) -> List[str]:
        """Get other technologies"""
        return self.categorized_technologies.get("Other", {}).get("techs", [])

    @rx.var
    def translated_description(self) -> str:
        """Get translated description for selected project"""
        if self.selected_project_id > 0:
            return get_project_description(self.selected_project_id, self.language)
        return self.selected_description

    @rx.var
    def projects(self) -> List[Dict[str, Any]]:
        """Get filtered projects with translated descriptions"""
        lang = self.language
        filtered = PROJECTS_DATA

        # Search by title
        if self.search_query:
            filtered = [p for p in filtered if self.search_query.lower() in p["title"].lower()]

        # Only filter by technologies if there are selections and "All" is not selected
        if self.selected_technologies and "All" not in self.selected_technologies:
            filtered = [p for p in filtered if any(tech in p["technologies"] for tech in self.selected_technologies)]

        if self.selected_domain != "All":
            filtered = [p for p in filtered if p["domain"] == self.selected_domain]

        if self.selected_platform != "All":
            filtered = [p for p in filtered if p["platform"] == self.selected_platform]

        if self.selected_project_type != "All":
            filtered = [p for p in filtered if p["project_type"] == self.selected_project_type]

        # Sort by ID descending (newest first)
        filtered = sorted(filtered, key=lambda x: x["id"], reverse=True)

        # Translate descriptions
        translated_projects = []
        for project in filtered:
            proj_copy = project.copy()
            proj_copy["description"] = get_project_description(project["id"], lang)
            translated_projects.append(proj_copy)

        return translated_projects
    
    def toggle_technology_filter(self, tech: str):
        if tech == "All":
            # If "All" is clicked, clear all selections or select only "All"
            if "All" in self.selected_technologies:
                self.selected_technologies = []
            else:
                self.selected_technologies = ["All"]
        else:
            # If any specific technology is clicked
            if tech in self.selected_technologies:
                self.selected_technologies.remove(tech)
            else:
                # Remove "All" if it was selected, then add the specific technology
                if "All" in self.selected_technologies:
                    self.selected_technologies.remove("All")
                self.selected_technologies.append(tech)

    def set_domain_filter(self, domain: str):
        self.selected_domain = domain

    def set_platform_filter(self, platform: str):
        self.selected_platform = platform

    def set_project_type_filter(self, project_type: str):
        self.selected_project_type = project_type

    def clear_all_filters(self):
        self.selected_technologies = ["All"]
        self.selected_domain = "All"
        self.selected_platform = "All"
        self.selected_project_type = "All"
        self.search_query = ""

    def set_search_query(self, query: str):
        self.search_query = query

    def toggle_show_more_programming_languages(self):
        self.show_more_programming_languages = not self.show_more_programming_languages

    def toggle_show_more_testing_tools(self):
        self.show_more_testing_tools = not self.show_more_testing_tools

    def toggle_show_more_databases(self):
        self.show_more_databases = not self.show_more_databases

    def toggle_show_more_frameworks(self):
        self.show_more_frameworks = not self.show_more_frameworks

    def toggle_show_more_devops(self):
        self.show_more_devops = not self.show_more_devops

    def toggle_show_more_other(self):
        self.show_more_other = not self.show_more_other

    def toggle_show_more_domains(self):
        self.show_more_domains = not self.show_more_domains

    def open_project_modal(self, project: Dict[str, Any]):
        self.selected_project_id = project["id"]
        self.selected_title = project["title"]
        self.selected_description = project["description"]
        self.selected_domain_badge = project["domain"]
        self.selected_platform_badge = project["platform"]
        self.selected_technologies_list = project["technologies"]
        self.selected_achievements_list = project["achievements"]
        self.selected_github = project["github"]
        self.selected_demo = project["demo"]
        self.show_modal = True

    def close_project_modal(self):
        self.show_modal = False
        self.selected_project_id = 0
        self.selected_title = ""
        self.selected_description = ""
        self.selected_domain_badge = ""
        self.selected_platform_badge = ""
        self.selected_technologies_list = []
        self.selected_achievements_list = []
        self.selected_github = ""
        self.selected_demo = ""

def project_modal() -> rx.Component:
    """Modal with full project details"""
    return rx.dialog.root(
        rx.dialog.content(
            rx.vstack(
                # Close button
                rx.box(
                    rx.dialog.close(
                        rx.icon("x", size=24, color="gray.400", cursor="pointer")
                    ),
                    width="100%",
                    text_align="right",
                    margin_bottom="1rem"
                ),

                # Project title
                rx.heading(
                    ProjectsState.selected_title,
                    size="7",
                    margin_bottom="1rem",
                    font_weight="800",
                    text_align="center",
                    style={
                        "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 50%, #8b5cf6 100%)",
                        "backgroundClip": "text",
                        "WebkitBackgroundClip": "text",
                        "color": "transparent"
                    }
                ),

                # Domain and Platform badges
                rx.hstack(
                    rx.badge(
                        ProjectsState.selected_domain_badge,
                        style={
                            "background": "rgba(91, 115, 255, 0.15)",
                            "color": "blue.300",
                            "border": "1px solid rgba(91, 115, 255, 0.3)",
                            "padding": "0.5rem 1.2rem",
                            "borderRadius": "1.5rem",
                            "fontSize": "0.9rem",
                            "fontWeight": "600"
                        }
                    ),
                    rx.badge(
                        ProjectsState.selected_platform_badge,
                        style={
                            "background": "rgba(139, 92, 246, 0.15)",
                            "color": "purple.300",
                            "border": "1px solid rgba(139, 92, 246, 0.3)",
                            "padding": "0.5rem 1.2rem",
                            "borderRadius": "1.5rem",
                            "fontSize": "0.9rem",
                            "fontWeight": "600"
                        }
                    ),
                    spacing="3",
                    justify="center",
                    margin_bottom="2rem"
                ),

                # Description
                rx.text(
                    ProjectsState.translated_description,
                    color="gray.300",
                    font_size="1rem",
                    line_height="1.8",
                    margin_bottom="2rem",
                    text_align="center"
                ),

                # Achievements section with medals
                rx.vstack(
                    rx.heading(
                        State.proj_achievements,
                        size="5",
                        color="orange.300",
                        margin_bottom="1.5rem",
                        text_align="center"
                    ),
                    rx.vstack(
                        rx.foreach(
                            ProjectsState.selected_achievements_list,
                            lambda achievement: rx.hstack(
                                rx.box(
                                    rx.text("🏅", font_size="2rem"),
                                    display="flex",
                                    align_items="center",
                                    justify_content="center",
                                    width="50px",
                                    height="50px",
                                    border_radius="50%",
                                    style={
                                        "background": "linear-gradient(135deg, rgba(251, 191, 36, 0.1), rgba(245, 158, 11, 0.1))",
                                        "border": "2px solid rgba(251, 191, 36, 0.4)",
                                        "boxShadow": "0 0 20px rgba(251, 191, 36, 0.3)"
                                    }
                                ),
                                rx.text(
                                    achievement,
                                    color="gray.300",
                                    font_size="0.95rem",
                                    line_height="1.6",
                                    flex="1"
                                ),
                                align="center",
                                spacing="4",
                                width="100%",
                                padding="0.75rem",
                                border_radius="lg",
                                style={
                                    "background": "rgba(15, 23, 42, 0.4)",
                                    "border": "1px solid rgba(251, 191, 36, 0.2)",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                        "background": "rgba(15, 23, 42, 0.6)",
                                        "borderColor": "rgba(251, 191, 36, 0.4)",
                                        "transform": "translateX(4px)"
                                    }
                                }
                            )
                        ),
                        spacing="3",
                        width="100%"
                    ),
                    width="100%",
                    margin_bottom="2rem"
                ),

                # Technologies section
                rx.vstack(
                    rx.heading(
                        "🛠️ Technologies",
                        size="5",
                        color="cyan.300",
                        margin_bottom="1rem",
                        text_align="center"
                    ),
                    rx.flex(
                        rx.foreach(
                            ProjectsState.selected_technologies_list,
                            lambda tech: rx.badge(
                                tech,
                                style={
                                    "background": "rgba(0, 212, 255, 0.1)",
                                    "color": "cyan.300",
                                    "border": "1px solid rgba(0, 212, 255, 0.3)",
                                    "padding": "0.4rem 0.8rem",
                                    "fontSize": "0.85rem",
                                    "fontWeight": "500"
                                }
                            )
                        ),
                        gap="8px",
                        wrap="wrap",
                        justify="center"
                    ),
                    width="100%",
                    margin_bottom="2rem"
                ),

                # Action buttons
                rx.hstack(
                    rx.cond(
                        ProjectsState.selected_github != "",
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("github", size=18),
                                    rx.text(State.proj_view_code),
                                    spacing="2"
                                ),
                                style={
                                    "background": "rgba(36, 41, 47, 0.8)",
                                    "color": "white",
                                    "padding": "0.7rem 1.5rem",
                                    "borderRadius": "0.75rem"
                                }
                            ),
                            href=ProjectsState.selected_github,
                            target="_blank"
                        )
                    ),
                    rx.cond(
                        ProjectsState.selected_demo != "",
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("external-link", size=18),
                                    rx.text(State.proj_live_demo),
                                    spacing="2"
                                ),
                                style={
                                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                                    "color": "white",
                                    "padding": "0.7rem 1.5rem",
                                    "borderRadius": "0.75rem"
                                }
                            ),
                            href=ProjectsState.selected_demo,
                            target="_blank"
                        )
                    ),
                    spacing="4",
                    justify="center",
                    width="100%"
                ),

                spacing="4",
                align="center",
                width="100%"
            ),
            max_width="800px",
            padding="2rem",
            style={
                "background": "linear-gradient(145deg, rgba(15, 23, 42, 0.98), rgba(30, 41, 59, 0.98))",
                "backdropFilter": "blur(20px)",
                "border": "1px solid rgba(148, 163, 184, 0.2)",
                "borderRadius": "1.5rem",
                "maxHeight": "90vh",
                "overflowY": "auto"
            }
        ),
        open=ProjectsState.show_modal,
        on_open_change=ProjectsState.close_project_modal
    )

def get_platform_icon(platform: str) -> str:
    """Get emoji icon for platform type"""
    platform_icons = {
        "Web": "🌐",
        "Mobile": "📱",
        "Desktop": "💻",
        "AI/Automation": "🤖"
    }
    return platform_icons.get(platform, "🚀")

def project_card(project) -> rx.Component:
    """Create a project card component"""
    return rx.box(
        # Project image with modern gradient and platform icon
        rx.box(
            rx.cond(
                project["image"] != "",
                # Show actual image if available
                rx.image(
                    src=project["image"],
                    alt=project["title"],
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    object_position="center 45%"
                ),
                # Fallback to emoji icon if no image
                rx.vstack(
                    rx.text(
                        get_platform_icon(project["platform"]),
                        font_size="4rem",
                        text_align="center"
                    ),
                    rx.badge(
                        project["platform"],
                        style={
                            "background": "rgba(139, 92, 246, 0.2)",
                            "color": "purple.200",
                            "border": "1px solid rgba(139, 92, 246, 0.4)",
                            "padding": "0.3rem 0.8rem",
                            "borderRadius": "1rem",
                            "fontSize": "0.75rem",
                            "fontWeight": "600"
                        }
                    ),
                    spacing="3",
                    align="center"
                )
            ),
            height="180px",
            width="100%",
            display="flex",
            align_items="center",
            justify_content="center",
            background="linear-gradient(135deg, rgba(0, 212, 255, 0.05) 0%, rgba(91, 115, 255, 0.05) 50%, rgba(139, 92, 246, 0.05) 100%)",
            border_radius="xl",
            margin_bottom="1.5rem",
            position="relative",
            overflow="hidden",
            style={
                "_before": {
                    "content": "''",
                    "position": "absolute",
                    "top": "-50%",
                    "left": "-50%",
                    "width": "200%",
                    "height": "200%",
                    "background": "radial-gradient(circle, rgba(0, 212, 255, 0.1) 0%, transparent 70%)",
                    "opacity": "0",
                    "transition": "opacity 0.3s ease"
                },
                "_hover:before": {
                    "opacity": "1"
                }
            }
        ),

        # Project title with modern styling
        rx.heading(
            project["title"],
            size="5",
            margin_bottom="1rem",
            line_height="1.2",
            font_weight="800",
            text_align="center",
            style={
                "background": "linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%)",
                "backgroundClip": "text",
                "WebkitBackgroundClip": "text",
                "color": "transparent",
                "textShadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                "letterSpacing": "-0.025em",
                "transition": "all 0.3s ease"
            }
        ),

        # Project description (truncated)
        rx.text(
            project["description"],
            color="gray.400",
            line_height="1.7",
            margin_bottom="1.5rem",
            min_height="4rem",
            max_height="5rem",
            overflow="hidden",
            font_size="0.85rem",
            padding_x="0.5rem",
            text_align="center",
            style={
                "display": "-webkit-box",
                "WebkitLineClamp": "3",
                "WebkitBoxOrient": "vertical",
                "textOverflow": "ellipsis"
            }
        ),

        # Domain badge
        rx.box(
            rx.badge(
                project["domain"],
                style={
                    "background": "rgba(91, 115, 255, 0.15)",
                    "color": "blue.300",
                    "border": "1px solid rgba(91, 115, 255, 0.3)",
                    "padding": "0.4rem 1rem",
                    "borderRadius": "1.5rem",
                    "fontSize": "0.8rem",
                    "fontWeight": "600",
                    "textTransform": "uppercase",
                    "letterSpacing": "0.05em"
                }
            ),
            text_align="center",
            margin_bottom="1rem"
        ),

        # Technologies placeholder - shown in modal
        rx.box(
            height="2rem",
            margin_bottom="1.5rem"
        ),

        # View Details button
        rx.button(
            rx.hstack(
                rx.icon("eye", size=16),
                rx.text(State.proj_view_details, font_size="0.85rem", font_weight="500"),
                spacing="2",
                align="center"
            ),
            on_click=lambda: ProjectsState.open_project_modal(project),
            size="2",
            style={
                "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                "color": "white",
                "border": "none",
                "padding": "0.6rem 1.5rem",
                "borderRadius": "0.75rem",
                "transition": "all 0.2s ease",
                "width": "100%",
                "_hover": {
                    "transform": "translateY(-1px)",
                    "boxShadow": "0 8px 25px rgba(0, 212, 255, 0.4)"
                }
            }
        ),

        # Modern card styling with cursor pointer
        padding="8",
        border_radius="2xl",
        cursor="pointer",
        on_click=lambda: ProjectsState.open_project_modal(project),
        style={
            "background": "linear-gradient(145deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.9))",
            "backdropFilter": "blur(20px)",
            "border": "1px solid rgba(148, 163, 184, 0.1)",
            "boxShadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
            "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
            "position": "relative",
            "overflow": "hidden",
            "_before": {
                "content": "''",
                "position": "absolute",
                "top": "0",
                "left": "0",
                "right": "0",
                "height": "1px",
                "background": "linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.4), transparent)",
                "opacity": "0",
                "transition": "opacity 0.3s ease"
            },
            "_hover": {
                "transform": "translateY(-4px)",
                "boxShadow": "0 25px 50px -12px rgba(0, 0, 0, 0.25), 0 0 30px rgba(0, 212, 255, 0.1)",
                "borderColor": "rgba(0, 212, 255, 0.2)"
            },
            "_hover:before": {
                "opacity": "1"
            }
        },
        width="100%"
    )

def filter_section() -> rx.Component:
    """Create the filter section"""
    return rx.vstack(
        # Header section
        rx.box(
            rx.heading(
                State.proj_title,
                size="9",
                text_align="center",
                margin_bottom="0.5rem",
                font_weight="900",
                line_height="1.2",
                padding_y="0.5rem",
                margin_top="2rem",
                style={
                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 50%, #8b5cf6 100%)",
                    "backgroundClip": "text",
                    "WebkitBackgroundClip": "text",
                    "color": "transparent",
                    "textShadow": "0 0 30px rgba(0, 212, 255, 0.3)",
                    "letterSpacing": "-0.05em",
                    "animation": "slideInUp 0.8s ease-out",
                    "position": "relative",
                    "zIndex": "10",
                    "overflow": "visible"
                }
            ),
            rx.text(
                rx.cond(
                    State.language == "pl",
                    "Z ponad 8-letnim doświadczeniem, pomyślnie zrealizowałem ponad 34 projekty w software house'ach, instytucjach bankowych i firmach produktowych. Od frameworków automatyzacji testów po rozwiązania zapewnienia jakości wspierające sukces biznesowy.",
                    "With over 8 years of experience, I've successfully delivered 34+ projects across software houses, banking institutions, and product companies. From test automation frameworks to quality assurance solutions that drive business success."
                ),
                color="gray.400",
                text_align="center",
                font_size="1.1rem",
                margin_bottom="2rem",
                max_width="700px",
                margin_x="auto",
                line_height="1.6",
                style={
                    "animation": "slideInUp 0.8s ease-out 0.2s both",
                    "position": "relative",
                    "zIndex": "10"
                }
            ),
            # Quick filter buttons for project type
            rx.hstack(
                rx.foreach(
                    PROJECT_TYPES,
                    lambda ptype: rx.button(
                        ptype,
                        on_click=ProjectsState.set_project_type_filter(ptype),
                        size="3",
                        variant="solid",
                        style={
                            "background": rx.cond(
                                ProjectsState.selected_project_type == ptype,
                                "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                                "rgba(30, 41, 59, 0.6)"
                            ),
                            "color": rx.cond(
                                ProjectsState.selected_project_type == ptype,
                                "white",
                                "gray.400"
                            ),
                            "border": rx.cond(
                                ProjectsState.selected_project_type == ptype,
                                "2px solid rgba(0, 212, 255, 0.8)",
                                "2px solid rgba(100, 116, 139, 0.3)"
                            ),
                            "padding": "0.6rem 1.5rem",
                            "borderRadius": "1.5rem",
                            "fontSize": "0.95rem",
                            "fontWeight": "700",
                            "transition": "all 0.3s ease",
                            "cursor": "pointer",
                            "boxShadow": rx.cond(
                                ProjectsState.selected_project_type == ptype,
                                "0 8px 20px rgba(0, 212, 255, 0.3)",
                                "0 4px 10px rgba(0, 0, 0, 0.2)"
                            ),
                            "_hover": {
                                "transform": "translateY(-2px)",
                                "boxShadow": "0 10px 25px rgba(0, 212, 255, 0.4)"
                            }
                        }
                    )
                ),
                spacing="4",
                justify="center",
                margin_bottom="2rem",
                style={
                    "animation": "slideInUp 0.8s ease-out 0.3s both",
                    "position": "relative",
                    "zIndex": "10"
                }
            ),
            width="100%",
            max_width="1400px",
            margin="0 auto 2rem auto",
            padding="0 2rem"
        ),

        # Filter section - compact 2-column layout
        rx.box(
            rx.vstack(
                # Search bar
                rx.hstack(
                    rx.icon("search", size=17, color="gray.500"),
                    rx.input(
                        placeholder=State.proj_search,
                        value=ProjectsState.search_query,
                        on_change=ProjectsState.set_search_query,
                        style={
                            "background": "transparent",
                            "border": "none",
                            "color": "white",
                            "fontSize": "0.95rem",
                            "width": "100%",
                            "_focus": {"outline": "none"},
                            "_placeholder": {"color": "gray.500"}
                        }
                    ),
                    spacing="2",
                    align="center",
                    width="100%",
                    padding="0.6rem 1rem",
                    background="rgba(30, 41, 59, 0.4)",
                    border_radius="lg",
                    border="1px solid rgba(100, 116, 139, 0.2)",
                ),

                # 2-column: Technologies | Platform + Domain
                rx.flex(
                  # LEFT: Technologies compact
                  rx.vstack(
                    # Header + All inline
                    rx.hstack(
                        rx.text(State.proj_technologies, color="gray.300", font_weight="700", font_size="0.85rem"),
                        rx.badge(
                            "All", cursor="pointer",
                            on_click=ProjectsState.toggle_technology_filter("All"),
                            style={
                                "background": rx.cond(ProjectsState.selected_technologies.contains("All"), "linear-gradient(135deg,#00d4ff,#5b73ff)", "rgba(30,41,59,0.5)"),
                                "color": rx.cond(ProjectsState.selected_technologies.contains("All"), "white", "gray.400"),
                                "border": rx.cond(ProjectsState.selected_technologies.contains("All"), "1px solid rgba(0,212,255,0.5)", "1px solid rgba(100,116,139,0.2)"),
                                "padding": "0.15rem 0.6rem", "borderRadius": "0.75rem", "fontSize": "0.72rem", "fontWeight": "600", "cursor": "pointer"
                            }
                        ),
                        spacing="2", align="center",
                    ),

                    # --- compact category rows ---
                    *[
                        rx.cond(
                            ProjectsState.categorized_technologies.contains(cat),
                            rx.box(
                                rx.flex(
                                    rx.badge(label, style={"background": f"rgba({cr},0.12)", "color": hex_c, "border": f"1px solid rgba({cr},0.28)", "padding": "0.1rem 0.42rem", "borderRadius": "0.3rem", "fontSize": "0.6rem", "fontWeight": "700", "whiteSpace": "nowrap", "flexShrink": "0"}),
                                    *[rx.badge(tech, cursor="pointer", on_click=ProjectsState.toggle_technology_filter(tech),
                                        style={"background": rx.cond(ProjectsState.selected_technologies.contains(tech), f"rgba({cr},0.22)", f"rgba({cr},0.05)"),
                                               "color": rx.cond(ProjectsState.selected_technologies.contains(tech), light_c, dim_c),
                                               "border": rx.cond(ProjectsState.selected_technologies.contains(tech), f"1px solid rgba({cr},0.55)", f"1px solid rgba({cr},0.18)"),
                                               "padding": "0.18rem 0.55rem", "borderRadius": "0.5rem", "fontSize": "0.7rem", "fontWeight": "500", "cursor": "pointer", "transition": "all 0.15s ease"})
                                      for tech in pop],
                                    rx.button(f"+{len(rest)}", on_click=toggle, size="1", variant="ghost", style=_SHOW_MORE_BTN_STYLE) if rest else rx.box(),
                                    gap="5px", flex_wrap="wrap", align_items="center",
                                ),
                                rx.cond(
                                    show_var,
                                    rx.flex(
                                        *[rx.badge(tech, cursor="pointer", on_click=ProjectsState.toggle_technology_filter(tech),
                                            style={"background": rx.cond(ProjectsState.selected_technologies.contains(tech), f"rgba({cr},0.22)", f"rgba({cr},0.05)"),
                                                   "color": rx.cond(ProjectsState.selected_technologies.contains(tech), light_c, dim_c),
                                                   "border": rx.cond(ProjectsState.selected_technologies.contains(tech), f"1px solid rgba({cr},0.55)", f"1px solid rgba({cr},0.18)"),
                                                   "padding": "0.18rem 0.55rem", "borderRadius": "0.5rem", "fontSize": "0.7rem", "fontWeight": "500", "cursor": "pointer", "transition": "all 0.15s ease"})
                                          for tech in rest],
                                        gap="5px", flex_wrap="wrap", padding_top="4px", padding_left="2px",
                                    ),
                                    rx.box()
                                ) if rest else rx.box(),
                                width="100%", margin_bottom="0.4rem",
                            )
                        )
                        for cat, label, cr, hex_c, light_c, dim_c, pop, rest, show_var, toggle in [
                            ("Programming Languages", "Programming", "0,212,255", "#00d4ff", "cyan.300", "cyan.400",
                             _PROG_LANG_POPULAR, _PROG_LANG_REST,
                             ProjectsState.show_more_programming_languages, ProjectsState.toggle_show_more_programming_languages),
                            ("Testing Tools", "Testing", "91,115,255", "#5b73ff", "blue.300", "blue.400",
                             _TESTING_TOOLS_POPULAR, _TESTING_TOOLS_REST,
                             ProjectsState.show_more_testing_tools, ProjectsState.toggle_show_more_testing_tools),
                            ("Databases", "Databases", "139,92,246", "#8b5cf6", "purple.300", "purple.400",
                             _DATABASES_POPULAR, _DATABASES_REST,
                             ProjectsState.show_more_databases, ProjectsState.toggle_show_more_databases),
                            ("Frameworks & Technologies", "Frameworks", "236,72,153", "#ec4899", "pink.300", "pink.400",
                             _FRAMEWORKS_POPULAR, _FRAMEWORKS_REST,
                             ProjectsState.show_more_frameworks, ProjectsState.toggle_show_more_frameworks),
                            ("DevOps & Tools", "DevOps", "34,197,94", "#22c55e", "green.300", "green.400",
                             _DEVOPS_POPULAR, _DEVOPS_REST,
                             ProjectsState.show_more_devops, ProjectsState.toggle_show_more_devops),
                            ("Other", "Other", "251,191,36", "#fbba24", "orange.300", "orange.400",
                             _OTHER_POPULAR, _OTHER_REST,
                             ProjectsState.show_more_other, ProjectsState.toggle_show_more_other),
                        ]
                    ],

                    align="start", spacing="1", min_width="0", flex_shrink="1",
                    style={"flexBasis": "55%", "minWidth": "260px"},
                  ),  # end LEFT

                  # RIGHT: Platform + Domain + Clear
                  rx.vstack(
                    # Platform
                    rx.vstack(
                        rx.text(State.proj_platform, color="gray.300", font_weight="700", font_size="0.82rem"),
                        rx.flex(
                            rx.foreach(
                                PLATFORMS,
                                lambda p: rx.badge(p, cursor="pointer", on_click=ProjectsState.set_platform_filter(p),
                                    style={"background": rx.cond(ProjectsState.selected_platform == p, "linear-gradient(135deg,#8b5cf6,#a855f7)", "rgba(30,41,59,0.4)"),
                                           "color": rx.cond(ProjectsState.selected_platform == p, "white", "gray.400"),
                                           "border": rx.cond(ProjectsState.selected_platform == p, "1px solid rgba(139,92,246,0.55)", "1px solid rgba(100,116,139,0.2)"),
                                           "padding": "0.22rem 0.65rem", "borderRadius": "0.75rem", "fontSize": "0.75rem", "fontWeight": "500", "cursor": "pointer", "transition": "all 0.15s ease"})
                            ),
                            gap="6px", flex_wrap="wrap",
                        ),
                        align="start", spacing="1",
                    ),
                    rx.divider(style={"borderColor": "rgba(100,116,139,0.12)", "margin": "0.4rem 0"}),
                    # Domain
                    rx.vstack(
                        rx.hstack(
                            rx.text(State.proj_domain, color="gray.300", font_weight="700", font_size="0.82rem"),
                            rx.button(
                                rx.cond(ProjectsState.show_more_domains,
                                    rx.hstack(rx.text("less", font_size="0.65rem"), rx.icon("chevron-up", size=10), spacing="1"),
                                    rx.hstack(rx.text(f"+{len(_DOMAINS_REST)}", font_size="0.65rem"), rx.icon("chevron-down", size=10), spacing="1"),
                                ),
                                on_click=ProjectsState.toggle_show_more_domains,
                                size="1", variant="ghost", style=_SHOW_MORE_BTN_STYLE,
                            ) if _DOMAINS_REST else rx.box(),
                            justify="between", align="center", width="100%",
                        ),
                        rx.flex(
                            *[rx.badge(d, cursor="pointer", on_click=ProjectsState.set_domain_filter(d),
                                style={"background": rx.cond(ProjectsState.selected_domain == d, "linear-gradient(135deg,#8b5cf6,#ec4899)", "rgba(30,41,59,0.4)"),
                                       "color": rx.cond(ProjectsState.selected_domain == d, "white", "gray.400"),
                                       "border": rx.cond(ProjectsState.selected_domain == d, "1px solid rgba(139,92,246,0.55)", "1px solid rgba(100,116,139,0.2)"),
                                       "padding": "0.22rem 0.65rem", "borderRadius": "0.75rem", "fontSize": "0.75rem", "fontWeight": "500", "cursor": "pointer", "transition": "all 0.15s ease"})
                              for d in _DOMAINS_POPULAR],
                            gap="6px", flex_wrap="wrap",
                        ),
                        rx.cond(
                            ProjectsState.show_more_domains,
                            rx.flex(
                                *[rx.badge(d, cursor="pointer", on_click=ProjectsState.set_domain_filter(d),
                                    style={"background": rx.cond(ProjectsState.selected_domain == d, "linear-gradient(135deg,#8b5cf6,#ec4899)", "rgba(30,41,59,0.4)"),
                                           "color": rx.cond(ProjectsState.selected_domain == d, "white", "gray.400"),
                                           "border": rx.cond(ProjectsState.selected_domain == d, "1px solid rgba(139,92,246,0.55)", "1px solid rgba(100,116,139,0.2)"),
                                           "padding": "0.22rem 0.65rem", "borderRadius": "0.75rem", "fontSize": "0.75rem", "fontWeight": "500", "cursor": "pointer", "transition": "all 0.15s ease"})
                                  for d in _DOMAINS_REST],
                                gap="6px", flex_wrap="wrap", padding_top="4px",
                            ),
                            rx.box()
                        ) if _DOMAINS_REST else rx.box(),
                        align="start", spacing="1",
                    ),
                    rx.divider(style={"borderColor": "rgba(100,116,139,0.12)", "margin": "0.4rem 0"}),
                    # Clear button
                    rx.button(
                        rx.hstack(rx.icon("x", size=13), rx.text(State.proj_clear_filters, font_size="0.78rem"), spacing="1"),
                        on_click=ProjectsState.clear_all_filters, size="1",
                        style={"background": "rgba(239,68,68,0.09)", "color": "red.300", "border": "1px solid rgba(239,68,68,0.25)",
                               "padding": "0.35rem 0.9rem", "borderRadius": "0.6rem", "fontWeight": "600", "transition": "all 0.2s ease",
                               "_hover": {"background": "rgba(239,68,68,0.18)"}}
                    ),
                    align="start", spacing="1",
                    style={"flexBasis": "40%", "minWidth": "200px", "flexShrink": "0"},
                  ),  # end RIGHT

                  gap="2rem",
                  flex_wrap="wrap",
                  width="100%",
                  align_items="start",
                ),  # end 2-column flex

                spacing="0",
                gap="0.7rem",
                width="100%",
            ),

            width="100%",
            max_width="1400px",
            margin="0 auto 3rem auto",
            padding="1.25rem 1.5rem",
            background="rgba(15, 23, 42, 0.6)",
            border_radius="xl",
            border="1px solid rgba(100, 116, 139, 0.1)",
            style={
                "animation": "slideInUp 0.8s ease-out 0.3s both",
                "position": "relative",
                "zIndex": "10"
            }
        ),

        align="center",
        width="100%"
    )

@rx.page(route="/projects", title="Marcin Orgacki | Projects")
def projects_page() -> rx.Component:
    """Projects page component"""
    header = Header()
    footer = Footer()
    header_component = header.build()
    footer_component = footer.build()
    sidebar_component = sidebar()
    
    # Layout without sidebar - same as main page
    layout = rx.vstack(
        header_component,
        rx.box(
            # Header section with filters
            filter_section(),

            # Projects grid - modern multi-column layout
            rx.box(
                rx.grid(
                    rx.foreach(
                        ProjectsState.projects,
                        project_card
                    ),
                    columns={"base": "1", "sm": "1", "md": "2", "lg": "3", "xl": "3"},
                    spacing="8",
                    width="100%"
                ),
                width="100%",
                max_width="1400px",
                margin="0 auto",
                padding="2rem"
            ),
            
            # Content styling
            padding="2rem 0",
            flex="1"
        ),

        # Contact section
        contact_section(),

        footer_component,
        align="stretch",
        spacing="0",
        width="100%",
        min_height="100vh",
        style={
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "space-between",
        }
    )

    return rx.fragment(
        # Page transition loader
        rx.cond(
            State.is_page_loading,
            page_transition_loader()
        ),

        # Project details modal
        rx.cond(
            ProjectsState.show_modal,
            project_modal()
        ),

        # Main content
        rx.box(
            # Animated background
            animated_background(),

            # Main content
            layout,

            # Floating language button
            floating_language_button(),

            background="linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%)",
            style={
                **animations_css,
                "boxSizing": "border-box",
                "width": "100%",
                "minHeight": "100vh",
                "margin": "0",
                "padding": "0",
                "position": "relative",
                "overflow": "hidden"
            },
            width="100%",
            min_height="100vh",
            on_mount=State.finish_page_transition
        )
    )