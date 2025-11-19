"""
Project Planning & Requirements Gathering System
Asks clarifying questions before generation to ensure consistency and save tokens
"""

import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


# ============================================================================
# PROJECT TYPES & CONFIGURATIONS
# ============================================================================

class ProjectType(Enum):
    """Types of projects we can generate"""
    STATIC_HTML = "static_html"          # Simple HTML/CSS/JS (no build step)
    REACT_SPA = "react_spa"              # React Single Page App (npm, CRA)
    REACT_VITE = "react_vite"            # React with Vite (faster)
    NEXTJS = "nextjs"                    # Next.js (SSR/SSG)
    FULLSTACK_NODE = "fullstack_node"    # React + Node.js + Database
    FULLSTACK_NEXTJS = "fullstack_nextjs" # Next.js + API routes + Database


class DeploymentTarget(Enum):
    """Where the project will be deployed"""
    GITHUB_PAGES = "github_pages"        # Static hosting (HTML only)
    VERCEL = "vercel"                    # Vercel (Next.js, React)
    NETLIFY = "netlify"                  # Netlify (Static, React)
    AWS_S3 = "aws_s3"                    # S3 + CloudFront
    HEROKU = "heroku"                    # Heroku (Full-stack)
    DOCKER = "docker"                    # Docker container
    VPS = "vps"                          # Self-hosted VPS


@dataclass
class ProjectRequirements:
    """Gathered requirements from user"""

    # Core features
    has_authentication: bool = False
    has_payment: bool = False
    has_database: bool = False
    has_api: bool = False
    has_admin_panel: bool = False
    has_user_accounts: bool = False

    # E-commerce specific
    has_product_catalog: bool = False
    has_shopping_cart: bool = False
    has_checkout: bool = False
    has_inventory_management: bool = False

    # Content features
    has_blog: bool = False
    has_gallery: bool = False
    has_contact_form: bool = False
    has_booking_system: bool = False

    # Technical requirements
    needs_seo: bool = False
    needs_analytics: bool = False
    needs_email: bool = False
    needs_file_upload: bool = False

    # Scale & performance
    expected_traffic: str = "low"  # low, medium, high
    needs_cdn: bool = False
    needs_caching: bool = False


@dataclass
class ProjectPlan:
    """Complete project plan with roadmap"""

    # Project configuration
    project_type: ProjectType
    deployment_target: DeploymentTarget
    requirements: ProjectRequirements

    # Technology stack
    frontend_framework: str  # "react", "html", "nextjs"
    backend_framework: Optional[str]  # "node", "nextjs-api", None
    database: Optional[str]  # "mongodb", "postgresql", "sqlite", None
    payment_gateway: Optional[str]  # "stripe", "paypal", None

    # Build & deployment
    build_command: str
    deploy_command: str
    install_command: str
    dev_command: str

    # File structure
    file_structure: Dict[str, str]  # path -> description

    # Dependencies
    npm_packages: List[str]
    env_variables: List[str]

    # Templates needed
    templates_needed: List[str]  # List of template IDs
    custom_components: List[str]  # Components to generate

    # Deployment roadmap
    deployment_steps: List[str]


# ============================================================================
# REQUIREMENTS ANALYZER
# ============================================================================

class RequirementsAnalyzer:
    """
    Analyzes user prompt to infer requirements
    Uses keyword detection + LLM for ambiguous cases
    """

    def __init__(self):
        self.keyword_patterns = self._load_keyword_patterns()

    def _load_keyword_patterns(self) -> Dict[str, List[str]]:
        """Load keyword patterns for requirement detection"""
        return {
            # E-commerce indicators
            'has_payment': [
                'sell', 'purchase', 'buy', 'shop', 'store', 'e-commerce',
                'ecommerce', 'cart', 'checkout', 'payment', 'stripe', 'paypal',
                'products', 'accessories', 'merchandise', 'pricing'
            ],
            'has_product_catalog': [
                'products', 'catalog', 'inventory', 'items', 'accessories',
                'merchandise', 'shop', 'store', 'browse'
            ],
            'has_shopping_cart': [
                'cart', 'basket', 'add to cart', 'shopping cart'
            ],
            'has_checkout': [
                'checkout', 'purchase', 'buy now', 'order'
            ],

            # Authentication indicators
            'has_authentication': [
                'login', 'signup', 'register', 'account', 'profile',
                'sign in', 'sign up', 'user account', 'member'
            ],
            'has_user_accounts': [
                'user account', 'member area', 'profile', 'dashboard',
                'my account', 'user profile'
            ],

            # Database indicators
            'has_database': [
                'save', 'store data', 'database', 'persistent', 'orders',
                'users', 'members', 'save orders', 'order history'
            ],

            # Content features
            'has_blog': [
                'blog', 'articles', 'posts', 'news', 'updates'
            ],
            'has_gallery': [
                'gallery', 'photos', 'images', 'portfolio', 'showcase'
            ],
            'has_contact_form': [
                'contact', 'contact form', 'get in touch', 'reach out',
                'contact us', 'inquiry'
            ],
            'has_booking_system': [
                'book', 'booking', 'reservation', 'schedule', 'appointment',
                'class schedule', 'reserve'
            ],

            # Admin features
            'has_admin_panel': [
                'admin', 'manage', 'cms', 'content management', 'backend',
                'admin panel', 'dashboard'
            ],

            # Technical features
            'needs_seo': [
                'seo', 'search engine', 'google', 'ranking', 'visibility'
            ],
            'needs_email': [
                'email', 'newsletter', 'notifications', 'send email',
                'email confirmation'
            ],
        }

    def analyze_prompt(self, user_prompt: str) -> ProjectRequirements:
        """
        Analyze user prompt to infer requirements

        Args:
            user_prompt: User's description of what they want

        Returns:
            ProjectRequirements with inferred needs
        """
        prompt_lower = user_prompt.lower()
        requirements = ProjectRequirements()

        # Check each requirement pattern
        for req_name, keywords in self.keyword_patterns.items():
            if any(keyword in prompt_lower for keyword in keywords):
                setattr(requirements, req_name, True)

        # Infer additional requirements based on detected features

        # If selling anything, need payment + catalog + cart
        if requirements.has_payment:
            requirements.has_product_catalog = True
            requirements.has_shopping_cart = True
            requirements.has_checkout = True

        # If has user accounts or checkout, need authentication
        if requirements.has_user_accounts or requirements.has_checkout:
            requirements.has_authentication = True

        # If has authentication, payment, or user accounts, need database
        if requirements.has_authentication or requirements.has_payment or requirements.has_user_accounts:
            requirements.has_database = True

        # If has database or admin, need API
        if requirements.has_database or requirements.has_admin_panel:
            requirements.has_api = True

        # If selling products, probably need email for confirmations
        if requirements.has_payment:
            requirements.needs_email = True

        # SEO is good for most public-facing sites
        if 'internal' not in prompt_lower and 'admin' not in prompt_lower:
            requirements.needs_seo = True

        logger.info(f"Inferred requirements from prompt: {requirements}")
        return requirements


# ============================================================================
# PROJECT TYPE SELECTOR
# ============================================================================

class ProjectTypeSelector:
    """
    Determines appropriate project type based on requirements
    """

    def select_project_type(self, requirements: ProjectRequirements) -> ProjectType:
        """
        Select best project type based on requirements

        Returns:
            Appropriate ProjectType
        """
        # Full-stack needed if has database + API
        if requirements.has_database and requirements.has_api:
            # Use Next.js if needs SEO (SSR)
            if requirements.needs_seo:
                return ProjectType.FULLSTACK_NEXTJS
            # Otherwise Node.js backend
            return ProjectType.FULLSTACK_NODE

        # SSR needed for SEO-heavy sites
        if requirements.needs_seo and (requirements.has_blog or requirements.has_product_catalog):
            return ProjectType.NEXTJS

        # React SPA for dynamic sites without SSR
        if (requirements.has_authentication or
            requirements.has_shopping_cart or
            requirements.has_admin_panel):
            return ProjectType.REACT_VITE

        # Static HTML for simple sites
        if not any([
            requirements.has_authentication,
            requirements.has_payment,
            requirements.has_database,
            requirements.has_api,
            requirements.has_shopping_cart
        ]):
            return ProjectType.STATIC_HTML

        # Default to React Vite (modern, fast)
        return ProjectType.REACT_VITE

    def select_deployment_target(
        self,
        project_type: ProjectType,
        requirements: ProjectRequirements
    ) -> DeploymentTarget:
        """Select best deployment target"""

        # Static HTML → GitHub Pages or Netlify
        if project_type == ProjectType.STATIC_HTML:
            return DeploymentTarget.NETLIFY

        # Next.js → Vercel (best support)
        if project_type in [ProjectType.NEXTJS, ProjectType.FULLSTACK_NEXTJS]:
            return DeploymentTarget.VERCEL

        # Full-stack Node → Heroku or VPS
        if project_type == ProjectType.FULLSTACK_NODE:
            # High traffic → VPS/Docker
            if requirements.expected_traffic == "high":
                return DeploymentTarget.DOCKER
            # Otherwise Heroku
            return DeploymentTarget.HEROKU

        # React SPA → Vercel or Netlify
        if project_type in [ProjectType.REACT_SPA, ProjectType.REACT_VITE]:
            return DeploymentTarget.VERCEL

        return DeploymentTarget.NETLIFY


# ============================================================================
# PROJECT PLANNER
# ============================================================================

class ProjectPlanner:
    """
    Creates complete project plan with roadmap
    """

    def __init__(self):
        self.requirements_analyzer = RequirementsAnalyzer()
        self.type_selector = ProjectTypeSelector()

    def create_plan(
        self,
        user_prompt: str,
        explicit_requirements: Optional[ProjectRequirements] = None
    ) -> ProjectPlan:
        """
        Create complete project plan

        Args:
            user_prompt: User's description
            explicit_requirements: Explicit requirements (overrides inference)

        Returns:
            Complete ProjectPlan
        """
        # Step 1: Analyze requirements
        if explicit_requirements:
            requirements = explicit_requirements
        else:
            requirements = self.requirements_analyzer.analyze_prompt(user_prompt)

        # Step 2: Select project type
        project_type = self.type_selector.select_project_type(requirements)
        deployment_target = self.type_selector.select_deployment_target(
            project_type, requirements
        )

        # Step 3: Determine tech stack
        tech_stack = self._determine_tech_stack(project_type, requirements)

        # Step 4: Define build commands
        build_config = self._get_build_config(project_type, deployment_target)

        # Step 5: Define file structure
        file_structure = self._get_file_structure(project_type, requirements)

        # Step 6: Determine dependencies
        npm_packages = self._get_npm_packages(project_type, requirements)
        env_variables = self._get_env_variables(requirements)

        # Step 7: Identify templates needed
        templates_needed = self._identify_templates(requirements)

        # Step 8: Create deployment roadmap
        deployment_steps = self._create_deployment_roadmap(
            project_type, deployment_target, requirements
        )

        # Create plan
        plan = ProjectPlan(
            project_type=project_type,
            deployment_target=deployment_target,
            requirements=requirements,
            frontend_framework=tech_stack['frontend'],
            backend_framework=tech_stack.get('backend'),
            database=tech_stack.get('database'),
            payment_gateway=tech_stack.get('payment'),
            build_command=build_config['build'],
            deploy_command=build_config['deploy'],
            install_command=build_config['install'],
            dev_command=build_config['dev'],
            file_structure=file_structure,
            npm_packages=npm_packages,
            env_variables=env_variables,
            templates_needed=templates_needed,
            custom_components=[],
            deployment_steps=deployment_steps
        )

        return plan

    def _determine_tech_stack(
        self,
        project_type: ProjectType,
        requirements: ProjectRequirements
    ) -> Dict[str, str]:
        """Determine technology stack"""

        stack = {}

        # Frontend
        if project_type == ProjectType.STATIC_HTML:
            stack['frontend'] = 'html'
        elif project_type in [ProjectType.REACT_SPA, ProjectType.REACT_VITE]:
            stack['frontend'] = 'react'
        elif project_type in [ProjectType.NEXTJS, ProjectType.FULLSTACK_NEXTJS]:
            stack['frontend'] = 'nextjs'
        elif project_type == ProjectType.FULLSTACK_NODE:
            stack['frontend'] = 'react'  # React frontend with Node backend

        # Backend
        if project_type == ProjectType.FULLSTACK_NODE:
            stack['backend'] = 'express'
        elif project_type == ProjectType.FULLSTACK_NEXTJS:
            stack['backend'] = 'nextjs-api'

        # Database
        if requirements.has_database:
            if requirements.has_product_catalog or requirements.has_payment:
                stack['database'] = 'postgresql'  # Better for e-commerce
            else:
                stack['database'] = 'mongodb'  # Flexible for general use

        # Payment
        if requirements.has_payment:
            stack['payment'] = 'stripe'  # Most popular

        return stack

    def _get_build_config(
        self,
        project_type: ProjectType,
        deployment_target: DeploymentTarget
    ) -> Dict[str, str]:
        """Get build and deployment commands"""

        configs = {
            ProjectType.STATIC_HTML: {
                'install': 'echo "No dependencies"',
                'dev': 'npx serve .',
                'build': 'echo "No build needed"',
                'deploy': 'echo "Upload to hosting"'
            },
            ProjectType.REACT_VITE: {
                'install': 'npm install',
                'dev': 'npm run dev',
                'build': 'npm run build',
                'deploy': 'npm run build && vercel --prod'
            },
            ProjectType.NEXTJS: {
                'install': 'npm install',
                'dev': 'npm run dev',
                'build': 'npm run build',
                'deploy': 'vercel --prod'
            },
            ProjectType.FULLSTACK_NEXTJS: {
                'install': 'npm install',
                'dev': 'npm run dev',
                'build': 'npm run build',
                'deploy': 'vercel --prod'
            },
            ProjectType.FULLSTACK_NODE: {
                'install': 'npm install && cd client && npm install',
                'dev': 'npm run dev',
                'build': 'cd client && npm run build',
                'deploy': 'git push heroku main'
            }
        }

        return configs.get(project_type, configs[ProjectType.REACT_VITE])

    def _get_file_structure(
        self,
        project_type: ProjectType,
        requirements: ProjectRequirements
    ) -> Dict[str, str]:
        """Define file structure"""

        if project_type == ProjectType.STATIC_HTML:
            return {
                'index.html': 'Main HTML file',
                'styles.css': 'Global styles',
                'script.js': 'JavaScript functionality',
                'images/': 'Image assets'
            }

        elif project_type in [ProjectType.REACT_SPA, ProjectType.REACT_VITE]:
            structure = {
                'src/App.jsx': 'Main app component',
                'src/main.jsx': 'Entry point',
                'src/components/': 'React components',
                'src/pages/': 'Page components',
                'src/styles/': 'CSS/styling',
                'public/': 'Static assets',
                'package.json': 'Dependencies',
                'vite.config.js': 'Vite configuration'
            }

            if requirements.has_api:
                structure['src/api/'] = 'API client functions'

            return structure

        elif project_type in [ProjectType.NEXTJS, ProjectType.FULLSTACK_NEXTJS]:
            structure = {
                'app/': 'Next.js app directory',
                'app/layout.jsx': 'Root layout',
                'app/page.jsx': 'Home page',
                'components/': 'Shared components',
                'public/': 'Static assets',
                'styles/': 'Global styles',
                'package.json': 'Dependencies'
            }

            if requirements.has_api:
                structure['app/api/'] = 'API routes'

            return structure

        return {}

    def _get_npm_packages(
        self,
        project_type: ProjectType,
        requirements: ProjectRequirements
    ) -> List[str]:
        """Determine npm packages needed"""

        packages = []

        # Base packages by project type
        if project_type == ProjectType.REACT_VITE:
            packages.extend(['react', 'react-dom', 'vite', '@vitejs/plugin-react'])
        elif project_type in [ProjectType.NEXTJS, ProjectType.FULLSTACK_NEXTJS]:
            packages.extend(['next', 'react', 'react-dom'])
        elif project_type == ProjectType.FULLSTACK_NODE:
            packages.extend(['express', 'cors', 'dotenv'])

        # Feature-based packages
        if requirements.has_authentication:
            packages.extend(['bcryptjs', 'jsonwebtoken'])

        if requirements.has_payment:
            packages.append('stripe')

        if requirements.has_database:
            if 'postgresql' in str(requirements):
                packages.append('pg')
            else:
                packages.append('mongoose')

        if requirements.needs_email:
            packages.append('nodemailer')

        # Always useful
        packages.extend(['react-router-dom', 'axios'])

        return list(set(packages))  # Remove duplicates

    def _get_env_variables(self, requirements: ProjectRequirements) -> List[str]:
        """Determine environment variables needed"""

        env_vars = []

        if requirements.has_database:
            env_vars.append('DATABASE_URL')

        if requirements.has_payment:
            env_vars.extend(['STRIPE_SECRET_KEY', 'STRIPE_PUBLISHABLE_KEY'])

        if requirements.needs_email:
            env_vars.extend(['EMAIL_HOST', 'EMAIL_USER', 'EMAIL_PASS'])

        if requirements.has_authentication:
            env_vars.append('JWT_SECRET')

        return env_vars

    def _identify_templates(self, requirements: ProjectRequirements) -> List[str]:
        """Identify which templates are needed"""

        templates = []

        # Always need header/footer
        templates.extend(['navigation.header', 'navigation.footer'])

        # Landing page
        templates.extend(['landing.hero', 'landing.features'])

        if requirements.has_authentication:
            templates.extend(['authentication.login', 'authentication.signup'])

        if requirements.has_product_catalog:
            templates.extend(['ecommerce.product_grid', 'ecommerce.product_card'])

        if requirements.has_shopping_cart:
            templates.append('ecommerce.cart')

        if requirements.has_checkout:
            templates.append('ecommerce.checkout')

        if requirements.has_contact_form:
            templates.append('forms.contact')

        if requirements.has_gallery:
            templates.append('content.gallery')

        if requirements.has_blog:
            templates.extend(['content.blog_list', 'content.blog_post'])

        return templates

    def _create_deployment_roadmap(
        self,
        project_type: ProjectType,
        deployment_target: DeploymentTarget,
        requirements: ProjectRequirements
    ) -> List[str]:
        """Create step-by-step deployment roadmap"""

        steps = []

        # Step 1: Local development
        if project_type == ProjectType.STATIC_HTML:
            steps.append("1. Open index.html in browser for local testing")
        else:
            steps.append("1. Run `npm install` to install dependencies")
            steps.append("2. Run `npm run dev` to start development server")
            steps.append("3. Test all features locally")

        # Step 2: Environment setup
        if requirements.has_database or requirements.has_payment:
            steps.append("4. Create .env file with required variables:")
            env_vars = self._get_env_variables(requirements)
            for var in env_vars:
                steps.append(f"   - {var}")

        # Step 3: Build
        if project_type != ProjectType.STATIC_HTML:
            steps.append("5. Run `npm run build` to create production build")
            steps.append("6. Test production build locally")

        # Step 4: Deployment platform setup
        if deployment_target == DeploymentTarget.VERCEL:
            steps.append("7. Install Vercel CLI: `npm i -g vercel`")
            steps.append("8. Run `vercel login` to authenticate")
            steps.append("9. Run `vercel --prod` to deploy")
        elif deployment_target == DeploymentTarget.NETLIFY:
            steps.append("7. Install Netlify CLI: `npm i -g netlify-cli`")
            steps.append("8. Run `netlify login` to authenticate")
            steps.append("9. Run `netlify deploy --prod` to deploy")
        elif deployment_target == DeploymentTarget.HEROKU:
            steps.append("7. Install Heroku CLI")
            steps.append("8. Run `heroku login`")
            steps.append("9. Run `heroku create your-app-name`")
            steps.append("10. Run `git push heroku main`")

        # Step 5: Post-deployment
        steps.append("10. Configure custom domain (optional)")

        if requirements.needs_seo:
            steps.append("11. Submit sitemap to Google Search Console")

        if requirements.needs_analytics:
            steps.append("12. Set up Google Analytics")

        return steps

    def print_plan(self, plan: ProjectPlan):
        """Print project plan in readable format"""

        print("=" * 80)
        print("PROJECT PLAN")
        print("=" * 80)
        print()

        print(f"📦 Project Type: {plan.project_type.value}")
        print(f"🚀 Deployment: {plan.deployment_target.value}")
        print()

        print("🛠️  Tech Stack:")
        print(f"   Frontend: {plan.frontend_framework}")
        if plan.backend_framework:
            print(f"   Backend: {plan.backend_framework}")
        if plan.database:
            print(f"   Database: {plan.database}")
        if plan.payment_gateway:
            print(f"   Payment: {plan.payment_gateway}")
        print()

        print("📋 Requirements:")
        req = plan.requirements
        if req.has_authentication:
            print("   ✅ Authentication & User Accounts")
        if req.has_payment:
            print("   ✅ Payment Processing")
        if req.has_product_catalog:
            print("   ✅ Product Catalog")
        if req.has_shopping_cart:
            print("   ✅ Shopping Cart")
        if req.has_database:
            print("   ✅ Database")
        if req.has_contact_form:
            print("   ✅ Contact Form")
        if req.has_gallery:
            print("   ✅ Gallery")
        print()

        print("📦 Dependencies:")
        for pkg in plan.npm_packages[:10]:  # Show first 10
            print(f"   - {pkg}")
        if len(plan.npm_packages) > 10:
            print(f"   ... and {len(plan.npm_packages) - 10} more")
        print()

        print("🔧 Commands:")
        print(f"   Install: {plan.install_command}")
        print(f"   Dev: {plan.dev_command}")
        print(f"   Build: {plan.build_command}")
        print(f"   Deploy: {plan.deploy_command}")
        print()

        print("📂 File Structure:")
        for path, desc in list(plan.file_structure.items())[:8]:
            print(f"   {path:<30} {desc}")
        print()

        print("🎨 Templates Needed:")
        for template in plan.templates_needed:
            print(f"   - {template}")
        print()

        print("🚀 Deployment Roadmap:")
        for step in plan.deployment_steps:
            print(f"   {step}")
        print()

        print("=" * 80)
