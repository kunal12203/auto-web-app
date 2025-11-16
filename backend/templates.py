"""
Template Library for AI Website Builder
Contains pre-built professional templates to reduce token usage by 75-85%
"""

TEMPLATES = {
    "modern-landing": {
        "name": "Modern Landing Page",
        "category": "Landing Page",
        "description": "Clean, modern landing page with hero section, features, and CTA",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Hero Section */
        .hero { background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; padding: 100px 0; text-align: center; }
        .hero h1 { font-size: 3.5rem; margin-bottom: 1rem; font-weight: 700; }
        .hero p { font-size: 1.25rem; margin-bottom: 2rem; opacity: 0.9; }
        .cta-btn { display: inline-block; padding: 15px 40px; background: white; color: {{PRIMARY_COLOR}}; text-decoration: none; border-radius: 50px; font-weight: 600; transition: transform 0.3s ease, box-shadow 0.3s ease; }
        .cta-btn:hover { transform: translateY(-3px); box-shadow: 0 10px 30px rgba(0,0,0,0.2); }

        /* Features Section */
        .features { padding: 80px 0; background: #f8f9fa; }
        .features h2 { text-align: center; font-size: 2.5rem; margin-bottom: 3rem; color: #2c3e50; }
        .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        .feature-card { background: white; padding: 30px; border-radius: 10px; text-align: center; transition: transform 0.3s ease, box-shadow 0.3s ease; }
        .feature-card:hover { transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        .feature-icon { width: 60px; height: 60px; margin: 0 auto 20px; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; }
        .feature-card h3 { margin-bottom: 15px; color: #2c3e50; }
        .feature-card p { color: #666; line-height: 1.6; }

        /* CTA Section */
        .cta-section { padding: 80px 0; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; text-align: center; }
        .cta-section h2 { font-size: 2.5rem; margin-bottom: 1.5rem; }
        .cta-section p { font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.9; }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 40px 0; text-align: center; }
        footer p { opacity: 0.8; }

        /* Responsive */
        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .hero p { font-size: 1.1rem; }
            .features h2, .cta-section h2 { font-size: 2rem; }
            .features-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <section class="hero">
        <div class="container">
            <h1>{{HERO_TITLE}}</h1>
            <p>{{HERO_SUBTITLE}}</p>
            <a href="#features" class="cta-btn">{{CTA_TEXT}}</a>
        </div>
    </section>

    <section id="features" class="features">
        <div class="container">
            <h2>{{FEATURES_TITLE}}</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>{{FEATURE_1_TITLE}}</h3>
                    <p>{{FEATURE_1_DESC}}</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎯</div>
                    <h3>{{FEATURE_2_TITLE}}</h3>
                    <p>{{FEATURE_2_DESC}}</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🚀</div>
                    <h3>{{FEATURE_3_TITLE}}</h3>
                    <p>{{FEATURE_3_DESC}}</p>
                </div>
            </div>
        </div>
    </section>

    <section class="cta-section">
        <div class="container">
            <h2>{{CTA_SECTION_TITLE}}</h2>
            <p>{{CTA_SECTION_DESC}}</p>
            <a href="#" class="cta-btn">{{CTA_BUTTON_TEXT}}</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    },

    "portfolio": {
        "name": "Portfolio Website",
        "category": "Portfolio",
        "description": "Professional portfolio with projects grid and about section",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Header */
        header { background: {{PRIMARY_COLOR}}; color: white; padding: 60px 0; text-align: center; }
        header h1 { font-size: 3rem; margin-bottom: 0.5rem; }
        header p { font-size: 1.3rem; opacity: 0.9; }

        /* Navigation */
        nav { background: #2c3e50; padding: 15px 0; position: sticky; top: 0; z-index: 100; }
        nav ul { list-style: none; display: flex; justify-content: center; gap: 30px; }
        nav a { color: white; text-decoration: none; font-weight: 500; transition: color 0.3s; }
        nav a:hover { color: {{PRIMARY_COLOR}}; }

        /* About Section */
        .about { padding: 80px 0; background: #f8f9fa; }
        .about h2 { font-size: 2.5rem; margin-bottom: 2rem; text-align: center; color: #2c3e50; }
        .about p { font-size: 1.1rem; line-height: 1.8; color: #666; max-width: 800px; margin: 0 auto; text-align: center; }

        /* Projects Section */
        .projects { padding: 80px 0; }
        .projects h2 { font-size: 2.5rem; margin-bottom: 3rem; text-align: center; color: #2c3e50; }
        .projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; }
        .project-card { background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 20px rgba(0,0,0,0.1); transition: transform 0.3s ease; }
        .project-card:hover { transform: translateY(-10px); }
        .project-image { width: 100%; height: 250px; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); display: flex; align-items: center; justify-content: center; font-size: 3rem; }
        .project-content { padding: 25px; }
        .project-content h3 { margin-bottom: 10px; color: #2c3e50; }
        .project-content p { color: #666; margin-bottom: 15px; }
        .project-link { display: inline-block; color: {{PRIMARY_COLOR}}; text-decoration: none; font-weight: 600; }

        /* Contact Section */
        .contact { padding: 80px 0; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; text-align: center; }
        .contact h2 { font-size: 2.5rem; margin-bottom: 1.5rem; }
        .contact p { font-size: 1.2rem; margin-bottom: 2rem; }
        .contact-btn { display: inline-block; padding: 15px 40px; background: white; color: {{PRIMARY_COLOR}}; text-decoration: none; border-radius: 50px; font-weight: 600; transition: transform 0.3s; }
        .contact-btn:hover { transform: scale(1.05); }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 30px 0; text-align: center; }

        @media (max-width: 768px) {
            header h1 { font-size: 2rem; }
            nav ul { flex-direction: column; align-items: center; gap: 15px; }
            .projects-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>{{NAME}}</h1>
            <p>{{TAGLINE}}</p>
        </div>
    </header>

    <nav>
        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section id="about" class="about">
        <div class="container">
            <h2>About Me</h2>
            <p>{{ABOUT_TEXT}}</p>
        </div>
    </section>

    <section id="projects" class="projects">
        <div class="container">
            <h2>My Projects</h2>
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-image">🎨</div>
                    <div class="project-content">
                        <h3>{{PROJECT_1_TITLE}}</h3>
                        <p>{{PROJECT_1_DESC}}</p>
                        <a href="#" class="project-link">View Project →</a>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-image">💻</div>
                    <div class="project-content">
                        <h3>{{PROJECT_2_TITLE}}</h3>
                        <p>{{PROJECT_2_DESC}}</p>
                        <a href="#" class="project-link">View Project →</a>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-image">📱</div>
                    <div class="project-content">
                        <h3>{{PROJECT_3_TITLE}}</h3>
                        <p>{{PROJECT_3_DESC}}</p>
                        <a href="#" class="project-link">View Project →</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="contact" class="contact">
        <div class="container">
            <h2>Let's Work Together</h2>
            <p>{{CONTACT_TEXT}}</p>
            <a href="mailto:{{EMAIL}}" class="contact-btn">Get In Touch</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    },

    "saas-landing": {
        "name": "SaaS Product Landing",
        "category": "Landing Page",
        "description": "Modern SaaS landing page with pricing and features",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Navigation */
        nav { background: white; padding: 20px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 100; }
        nav .container { display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 1.5rem; font-weight: 700; color: {{PRIMARY_COLOR}}; }
        nav ul { list-style: none; display: flex; gap: 30px; }
        nav a { color: #333; text-decoration: none; font-weight: 500; }
        .nav-cta { background: {{PRIMARY_COLOR}}; color: white; padding: 10px 25px; border-radius: 25px; }

        /* Hero */
        .hero { padding: 100px 0; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; text-align: center; }
        .hero h1 { font-size: 3.5rem; margin-bottom: 1.5rem; font-weight: 700; }
        .hero p { font-size: 1.3rem; margin-bottom: 2.5rem; opacity: 0.95; }
        .hero-cta { display: inline-block; padding: 18px 45px; background: white; color: {{PRIMARY_COLOR}}; text-decoration: none; border-radius: 50px; font-weight: 600; font-size: 1.1rem; transition: transform 0.3s, box-shadow 0.3s; }
        .hero-cta:hover { transform: translateY(-3px); box-shadow: 0 10px 30px rgba(0,0,0,0.2); }

        /* Features */
        .features { padding: 100px 0; background: #f8f9fa; }
        .features h2 { text-align: center; font-size: 2.8rem; margin-bottom: 4rem; color: #2c3e50; }
        .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; }
        .feature { text-align: center; }
        .feature-icon { width: 80px; height: 80px; margin: 0 auto 25px; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; font-size: 2rem; }
        .feature h3 { font-size: 1.5rem; margin-bottom: 15px; color: #2c3e50; }
        .feature p { color: #666; line-height: 1.7; }

        /* Pricing */
        .pricing { padding: 100px 0; }
        .pricing h2 { text-align: center; font-size: 2.8rem; margin-bottom: 4rem; color: #2c3e50; }
        .pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; max-width: 1000px; margin: 0 auto; }
        .pricing-card { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 5px 30px rgba(0,0,0,0.1); text-align: center; transition: transform 0.3s; }
        .pricing-card:hover { transform: translateY(-10px); }
        .pricing-card.featured { background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; }
        .plan-name { font-size: 1.5rem; font-weight: 600; margin-bottom: 20px; }
        .plan-price { font-size: 3rem; font-weight: 700; margin-bottom: 10px; }
        .plan-period { opacity: 0.7; margin-bottom: 30px; }
        .plan-features { list-style: none; margin-bottom: 30px; }
        .plan-features li { padding: 10px 0; border-bottom: 1px solid rgba(0,0,0,0.1); }
        .pricing-card.featured .plan-features li { border-bottom-color: rgba(255,255,255,0.2); }
        .plan-btn { display: inline-block; padding: 15px 40px; background: {{PRIMARY_COLOR}}; color: white; text-decoration: none; border-radius: 50px; font-weight: 600; transition: transform 0.3s; }
        .pricing-card.featured .plan-btn { background: white; color: {{PRIMARY_COLOR}}; }
        .plan-btn:hover { transform: scale(1.05); }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 50px 0; text-align: center; }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            nav .container { flex-direction: column; gap: 20px; }
            nav ul { flex-direction: column; align-items: center; gap: 15px; }
            .pricing-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <div class="logo">{{LOGO_TEXT}}</div>
            <ul>
                <li><a href="#features">Features</a></li>
                <li><a href="#pricing">Pricing</a></li>
                <li><a href="#" class="nav-cta">Get Started</a></li>
            </ul>
        </div>
    </nav>

    <section class="hero">
        <div class="container">
            <h1>{{HERO_TITLE}}</h1>
            <p>{{HERO_SUBTITLE}}</p>
            <a href="#pricing" class="hero-cta">{{HERO_CTA}}</a>
        </div>
    </section>

    <section id="features" class="features">
        <div class="container">
            <h2>{{FEATURES_TITLE}}</h2>
            <div class="features-grid">
                <div class="feature">
                    <div class="feature-icon">⚡</div>
                    <h3>{{FEATURE_1_TITLE}}</h3>
                    <p>{{FEATURE_1_DESC}}</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">🔒</div>
                    <h3>{{FEATURE_2_TITLE}}</h3>
                    <p>{{FEATURE_2_DESC}}</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">📊</div>
                    <h3>{{FEATURE_3_TITLE}}</h3>
                    <p>{{FEATURE_3_DESC}}</p>
                </div>
            </div>
        </div>
    </section>

    <section id="pricing" class="pricing">
        <div class="container">
            <h2>{{PRICING_TITLE}}</h2>
            <div class="pricing-grid">
                <div class="pricing-card">
                    <div class="plan-name">{{PLAN_1_NAME}}</div>
                    <div class="plan-price">{{PLAN_1_PRICE}}</div>
                    <div class="plan-period">per month</div>
                    <ul class="plan-features">
                        <li>{{PLAN_1_FEATURE_1}}</li>
                        <li>{{PLAN_1_FEATURE_2}}</li>
                        <li>{{PLAN_1_FEATURE_3}}</li>
                    </ul>
                    <a href="#" class="plan-btn">Choose Plan</a>
                </div>
                <div class="pricing-card featured">
                    <div class="plan-name">{{PLAN_2_NAME}}</div>
                    <div class="plan-price">{{PLAN_2_PRICE}}</div>
                    <div class="plan-period">per month</div>
                    <ul class="plan-features">
                        <li>{{PLAN_2_FEATURE_1}}</li>
                        <li>{{PLAN_2_FEATURE_2}}</li>
                        <li>{{PLAN_2_FEATURE_3}}</li>
                    </ul>
                    <a href="#" class="plan-btn">Choose Plan</a>
                </div>
                <div class="pricing-card">
                    <div class="plan-name">{{PLAN_3_NAME}}</div>
                    <div class="plan-price">{{PLAN_3_PRICE}}</div>
                    <div class="plan-period">per month</div>
                    <ul class="plan-features">
                        <li>{{PLAN_3_FEATURE_1}}</li>
                        <li>{{PLAN_3_FEATURE_2}}</li>
                        <li>{{PLAN_3_FEATURE_3}}</li>
                    </ul>
                    <a href="#" class="plan-btn">Choose Plan</a>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    },

    "restaurant": {
        "name": "Restaurant Website",
        "category": "Business",
        "description": "Restaurant website with menu and contact section",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Georgia', serif; line-height: 1.6; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Hero */
        .hero { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; padding: 150px 0; text-align: center; }
        .hero h1 { font-size: 4rem; margin-bottom: 1rem; font-family: 'Georgia', serif; }
        .hero p { font-size: 1.5rem; margin-bottom: 2rem; }
        .hero-btn { display: inline-block; padding: 15px 40px; background: {{PRIMARY_COLOR}}; color: white; text-decoration: none; border-radius: 5px; font-weight: 600; transition: background 0.3s; }
        .hero-btn:hover { background: {{SECONDARY_COLOR}}; }

        /* About */
        .about { padding: 80px 0; background: #f8f9fa; }
        .about-content { display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center; }
        .about-image { width: 100%; height: 400px; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 5rem; }
        .about-text h2 { font-size: 2.5rem; margin-bottom: 1.5rem; color: #2c3e50; }
        .about-text p { font-size: 1.1rem; color: #666; line-height: 1.8; }

        /* Menu */
        .menu { padding: 80px 0; }
        .menu h2 { text-align: center; font-size: 3rem; margin-bottom: 3rem; color: #2c3e50; }
        .menu-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        .menu-item { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 5px 20px rgba(0,0,0,0.1); }
        .menu-item-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
        .menu-item h3 { color: #2c3e50; font-size: 1.3rem; }
        .menu-item-price { color: {{PRIMARY_COLOR}}; font-weight: 700; font-size: 1.2rem; }
        .menu-item p { color: #666; line-height: 1.6; }

        /* Contact */
        .contact { padding: 80px 0; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; text-align: center; }
        .contact h2 { font-size: 3rem; margin-bottom: 2rem; }
        .contact-info { display: flex; justify-content: center; gap: 50px; margin-bottom: 2rem; flex-wrap: wrap; }
        .contact-item { font-size: 1.1rem; }
        .contact-item strong { display: block; margin-bottom: 10px; font-size: 1.3rem; }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 30px 0; text-align: center; }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .about-content { grid-template-columns: 1fr; }
            .menu-grid { grid-template-columns: 1fr; }
            .contact-info { flex-direction: column; gap: 30px; }
        }
    </style>
</head>
<body>
    <section class="hero">
        <div class="container">
            <h1>{{RESTAURANT_NAME}}</h1>
            <p>{{TAGLINE}}</p>
            <a href="#menu" class="hero-btn">View Menu</a>
        </div>
    </section>

    <section class="about">
        <div class="container">
            <div class="about-content">
                <div class="about-image">🍽️</div>
                <div class="about-text">
                    <h2>About Us</h2>
                    <p>{{ABOUT_TEXT}}</p>
                </div>
            </div>
        </div>
    </section>

    <section id="menu" class="menu">
        <div class="container">
            <h2>Our Menu</h2>
            <div class="menu-grid">
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>{{DISH_1_NAME}}</h3>
                        <span class="menu-item-price">{{DISH_1_PRICE}}</span>
                    </div>
                    <p>{{DISH_1_DESC}}</p>
                </div>
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>{{DISH_2_NAME}}</h3>
                        <span class="menu-item-price">{{DISH_2_PRICE}}</span>
                    </div>
                    <p>{{DISH_2_DESC}}</p>
                </div>
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>{{DISH_3_NAME}}</h3>
                        <span class="menu-item-price">{{DISH_3_PRICE}}</span>
                    </div>
                    <p>{{DISH_3_DESC}}</p>
                </div>
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>{{DISH_4_NAME}}</h3>
                        <span class="menu-item-price">{{DISH_4_PRICE}}</span>
                    </div>
                    <p>{{DISH_4_DESC}}</p>
                </div>
            </div>
        </div>
    </section>

    <section class="contact">
        <div class="container">
            <h2>Visit Us</h2>
            <div class="contact-info">
                <div class="contact-item">
                    <strong>📍 Location</strong>
                    <span>{{ADDRESS}}</span>
                </div>
                <div class="contact-item">
                    <strong>📞 Phone</strong>
                    <span>{{PHONE}}</span>
                </div>
                <div class="contact-item">
                    <strong>⏰ Hours</strong>
                    <span>{{HOURS}}</span>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    },

    "blog": {
        "name": "Blog Website",
        "category": "Blog",
        "description": "Clean blog layout with article cards and categories",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; background: #f8f9fa; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Header */
        header { background: white; padding: 30px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        header h1 { font-size: 2.5rem; color: {{PRIMARY_COLOR}}; margin-bottom: 0.5rem; }
        header p { font-size: 1.1rem; color: #666; }

        /* Navigation */
        nav { background: {{PRIMARY_COLOR}}; padding: 15px 0; position: sticky; top: 0; z-index: 100; }
        nav ul { list-style: none; display: flex; justify-content: center; gap: 30px; }
        nav a { color: white; text-decoration: none; font-weight: 500; transition: opacity 0.3s; }
        nav a:hover { opacity: 0.8; }

        /* Main Content */
        main { padding: 60px 0; }
        .blog-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 30px; }

        /* Article Card */
        .article-card { background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 20px rgba(0,0,0,0.1); transition: transform 0.3s, box-shadow 0.3s; }
        .article-card:hover { transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0,0,0,0.15); }
        .article-image { width: 100%; height: 250px; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); display: flex; align-items: center; justify-content: center; font-size: 3rem; }
        .article-content { padding: 25px; }
        .article-meta { display: flex; gap: 15px; margin-bottom: 15px; font-size: 0.9rem; color: #666; }
        .article-category { background: {{PRIMARY_COLOR}}; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; }
        .article-content h2 { font-size: 1.5rem; margin-bottom: 15px; color: #2c3e50; }
        .article-content p { color: #666; margin-bottom: 20px; line-height: 1.7; }
        .read-more { display: inline-block; color: {{PRIMARY_COLOR}}; text-decoration: none; font-weight: 600; transition: transform 0.3s; }
        .read-more:hover { transform: translateX(5px); }

        /* Sidebar */
        .layout { display: grid; grid-template-columns: 1fr 300px; gap: 40px; }
        .sidebar { background: white; padding: 30px; border-radius: 10px; height: fit-content; box-shadow: 0 5px 20px rgba(0,0,0,0.1); }
        .sidebar h3 { margin-bottom: 20px; color: #2c3e50; }
        .sidebar ul { list-style: none; }
        .sidebar li { padding: 10px 0; border-bottom: 1px solid #eee; }
        .sidebar a { color: #666; text-decoration: none; transition: color 0.3s; }
        .sidebar a:hover { color: {{PRIMARY_COLOR}}; }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 40px 0; text-align: center; margin-top: 60px; }

        @media (max-width: 992px) {
            .layout { grid-template-columns: 1fr; }
            .blog-grid { grid-template-columns: 1fr; }
            nav ul { flex-direction: column; align-items: center; gap: 15px; }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>{{BLOG_NAME}}</h1>
            <p>{{BLOG_TAGLINE}}</p>
        </div>
    </header>

    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#tech">Technology</a></li>
            <li><a href="#design">Design</a></li>
            <li><a href="#business">Business</a></li>
            <li><a href="#about">About</a></li>
        </ul>
    </nav>

    <main>
        <div class="container">
            <div class="layout">
                <div class="blog-grid">
                    <article class="article-card">
                        <div class="article-image">📝</div>
                        <div class="article-content">
                            <div class="article-meta">
                                <span class="article-category">{{ARTICLE_1_CATEGORY}}</span>
                                <span>{{ARTICLE_1_DATE}}</span>
                            </div>
                            <h2>{{ARTICLE_1_TITLE}}</h2>
                            <p>{{ARTICLE_1_EXCERPT}}</p>
                            <a href="#" class="read-more">Read More →</a>
                        </div>
                    </article>

                    <article class="article-card">
                        <div class="article-image">💡</div>
                        <div class="article-content">
                            <div class="article-meta">
                                <span class="article-category">{{ARTICLE_2_CATEGORY}}</span>
                                <span>{{ARTICLE_2_DATE}}</span>
                            </div>
                            <h2>{{ARTICLE_2_TITLE}}</h2>
                            <p>{{ARTICLE_2_EXCERPT}}</p>
                            <a href="#" class="read-more">Read More →</a>
                        </div>
                    </article>

                    <article class="article-card">
                        <div class="article-image">🚀</div>
                        <div class="article-content">
                            <div class="article-meta">
                                <span class="article-category">{{ARTICLE_3_CATEGORY}}</span>
                                <span>{{ARTICLE_3_DATE}}</span>
                            </div>
                            <h2>{{ARTICLE_3_TITLE}}</h2>
                            <p>{{ARTICLE_3_EXCERPT}}</p>
                            <a href="#" class="read-more">Read More →</a>
                        </div>
                    </article>
                </div>

                <aside class="sidebar">
                    <h3>Categories</h3>
                    <ul>
                        <li><a href="#tech">Technology</a></li>
                        <li><a href="#design">Design</a></li>
                        <li><a href="#business">Business</a></li>
                        <li><a href="#lifestyle">Lifestyle</a></li>
                    </ul>
                </aside>
            </div>
        </div>
    </main>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    },

    "ecommerce": {
        "name": "E-Commerce Store",
        "category": "E-Commerce",
        "description": "Product showcase with shopping features",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Header */
        header { background: white; padding: 20px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        header .container { display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 1.8rem; font-weight: 700; color: {{PRIMARY_COLOR}}; }
        .cart-icon { font-size: 1.5rem; cursor: pointer; }

        /* Hero Banner */
        .hero-banner { background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; padding: 80px 0; text-align: center; }
        .hero-banner h1 { font-size: 3rem; margin-bottom: 1rem; }
        .hero-banner p { font-size: 1.2rem; margin-bottom: 2rem; }
        .shop-btn { display: inline-block; padding: 15px 40px; background: white; color: {{PRIMARY_COLOR}}; text-decoration: none; border-radius: 50px; font-weight: 600; transition: transform 0.3s; }
        .shop-btn:hover { transform: scale(1.05); }

        /* Products */
        .products { padding: 80px 0; background: #f8f9fa; }
        .products h2 { text-align: center; font-size: 2.5rem; margin-bottom: 3rem; color: #2c3e50; }
        .products-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; }
        .product-card { background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 20px rgba(0,0,0,0.1); transition: transform 0.3s; }
        .product-card:hover { transform: translateY(-10px); }
        .product-image { width: 100%; height: 300px; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); display: flex; align-items: center; justify-content: center; font-size: 4rem; }
        .product-info { padding: 20px; }
        .product-name { font-size: 1.3rem; margin-bottom: 10px; color: #2c3e50; }
        .product-price { font-size: 1.5rem; color: {{PRIMARY_COLOR}}; font-weight: 700; margin-bottom: 15px; }
        .buy-btn { width: 100%; padding: 12px; background: {{PRIMARY_COLOR}}; color: white; border: none; border-radius: 5px; font-weight: 600; cursor: pointer; transition: background 0.3s; }
        .buy-btn:hover { background: {{SECONDARY_COLOR}}; }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 40px 0; text-align: center; }

        @media (max-width: 768px) {
            .hero-banner h1 { font-size: 2rem; }
            .products-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">{{STORE_NAME}}</div>
            <div class="cart-icon">🛒</div>
        </div>
    </header>

    <section class="hero-banner">
        <div class="container">
            <h1>{{HERO_TITLE}}</h1>
            <p>{{HERO_SUBTITLE}}</p>
            <a href="#products" class="shop-btn">Shop Now</a>
        </div>
    </section>

    <section id="products" class="products">
        <div class="container">
            <h2>Featured Products</h2>
            <div class="products-grid">
                <div class="product-card">
                    <div class="product-image">📦</div>
                    <div class="product-info">
                        <div class="product-name">{{PRODUCT_1_NAME}}</div>
                        <div class="product-price">{{PRODUCT_1_PRICE}}</div>
                        <button class="buy-btn">Add to Cart</button>
                    </div>
                </div>
                <div class="product-card">
                    <div class="product-image">🎁</div>
                    <div class="product-info">
                        <div class="product-name">{{PRODUCT_2_NAME}}</div>
                        <div class="product-price">{{PRODUCT_2_PRICE}}</div>
                        <button class="buy-btn">Add to Cart</button>
                    </div>
                </div>
                <div class="product-card">
                    <div class="product-image">⭐</div>
                    <div class="product-info">
                        <div class="product-name">{{PRODUCT_3_NAME}}</div>
                        <div class="product-price">{{PRODUCT_3_PRICE}}</div>
                        <button class="buy-btn">Add to Cart</button>
                    </div>
                </div>
                <div class="product-card">
                    <div class="product-image">💎</div>
                    <div class="product-info">
                        <div class="product-name">{{PRODUCT_4_NAME}}</div>
                        <div class="product-price">{{PRODUCT_4_PRICE}}</div>
                        <button class="buy-btn">Add to Cart</button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    },

    "agency": {
        "name": "Digital Agency",
        "category": "Business",
        "description": "Professional agency website with services and team",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Navigation */
        nav { background: rgba(255,255,255,0.95); padding: 20px 0; position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        nav .container { display: flex; justify-content: space-between; align-items: center; }
        .nav-logo { font-size: 1.5rem; font-weight: 700; color: {{PRIMARY_COLOR}}; }
        nav ul { list-style: none; display: flex; gap: 30px; }
        nav a { color: #333; text-decoration: none; font-weight: 500; transition: color 0.3s; }
        nav a:hover { color: {{PRIMARY_COLOR}}; }

        /* Hero */
        .hero { background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; padding: 120px 0; }
        .hero-content { max-width: 700px; }
        .hero h1 { font-size: 3.5rem; margin-bottom: 1.5rem; line-height: 1.2; }
        .hero p { font-size: 1.3rem; margin-bottom: 2rem; opacity: 0.95; }
        .hero-btn { display: inline-block; padding: 15px 40px; background: white; color: {{PRIMARY_COLOR}}; text-decoration: none; border-radius: 50px; font-weight: 600; transition: transform 0.3s; }
        .hero-btn:hover { transform: translateY(-3px); }

        /* Services */
        .services { padding: 100px 0; background: #f8f9fa; }
        .services h2 { text-align: center; font-size: 2.8rem; margin-bottom: 4rem; color: #2c3e50; }
        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; }
        .service-card { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 5px 30px rgba(0,0,0,0.08); transition: transform 0.3s; }
        .service-card:hover { transform: translateY(-10px); }
        .service-icon { width: 70px; height: 70px; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); border-radius: 15px; display: flex; align-items: center; justify-content: center; font-size: 2rem; margin-bottom: 25px; }
        .service-card h3 { font-size: 1.5rem; margin-bottom: 15px; color: #2c3e50; }
        .service-card p { color: #666; line-height: 1.7; }

        /* CTA */
        .cta { padding: 100px 0; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; text-align: center; }
        .cta h2 { font-size: 3rem; margin-bottom: 1.5rem; }
        .cta p { font-size: 1.3rem; margin-bottom: 2.5rem; }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 50px 0; text-align: center; }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            nav .container { flex-direction: column; gap: 20px; }
            nav ul { flex-direction: column; align-items: center; gap: 15px; }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <div class="nav-logo">{{AGENCY_NAME}}</div>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#work">Work</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <h1>{{HERO_TITLE}}</h1>
                <p>{{HERO_SUBTITLE}}</p>
                <a href="#services" class="hero-btn">{{CTA_TEXT}}</a>
            </div>
        </div>
    </section>

    <section id="services" class="services">
        <div class="container">
            <h2>Our Services</h2>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">🎨</div>
                    <h3>{{SERVICE_1_TITLE}}</h3>
                    <p>{{SERVICE_1_DESC}}</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">💻</div>
                    <h3>{{SERVICE_2_TITLE}}</h3>
                    <p>{{SERVICE_2_DESC}}</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">📱</div>
                    <h3>{{SERVICE_3_TITLE}}</h3>
                    <p>{{SERVICE_3_DESC}}</p>
                </div>
            </div>
        </div>
    </section>

    <section class="cta">
        <div class="container">
            <h2>{{CTA_TITLE}}</h2>
            <p>{{CTA_SUBTITLE}}</p>
            <a href="#contact" class="hero-btn">{{CTA_BUTTON}}</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    },

    "fitness": {
        "name": "Fitness Gym",
        "category": "Health & Fitness",
        "description": "Gym and fitness center website",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Hero */
        .hero { background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; padding: 150px 0; text-align: center; }
        .hero h1 { font-size: 4rem; margin-bottom: 1rem; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; }
        .hero p { font-size: 1.5rem; margin-bottom: 2.5rem; }
        .join-btn { display: inline-block; padding: 18px 50px; background: {{PRIMARY_COLOR}}; color: white; text-decoration: none; border-radius: 5px; font-weight: 700; font-size: 1.1rem; text-transform: uppercase; transition: transform 0.3s; }
        .join-btn:hover { transform: scale(1.05); }

        /* Programs */
        .programs { padding: 100px 0; background: #f8f9fa; }
        .programs h2 { text-align: center; font-size: 3rem; margin-bottom: 3rem; color: #2c3e50; text-transform: uppercase; }
        .programs-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        .program-card { background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 25px rgba(0,0,0,0.1); transition: transform 0.3s; }
        .program-card:hover { transform: translateY(-10px); }
        .program-image { width: 100%; height: 250px; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); display: flex; align-items: center; justify-content: center; font-size: 4rem; }
        .program-content { padding: 30px; }
        .program-content h3 { font-size: 1.5rem; margin-bottom: 15px; color: #2c3e50; text-transform: uppercase; }
        .program-content p { color: #666; line-height: 1.7; margin-bottom: 20px; }
        .learn-more { color: {{PRIMARY_COLOR}}; text-decoration: none; font-weight: 600; }

        /* Stats */
        .stats { padding: 80px 0; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; }
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; text-align: center; }
        .stat-item { font-size: 3rem; font-weight: 900; margin-bottom: 10px; }
        .stat-label { font-size: 1.1rem; opacity: 0.9; }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 40px 0; text-align: center; }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .programs-grid { grid-template-columns: 1fr; }
            .stats-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <section class="hero">
        <div class="container">
            <h1>{{GYM_NAME}}</h1>
            <p>{{TAGLINE}}</p>
            <a href="#programs" class="join-btn">Join Now</a>
        </div>
    </section>

    <section id="programs" class="programs">
        <div class="container">
            <h2>Our Programs</h2>
            <div class="programs-grid">
                <div class="program-card">
                    <div class="program-image">💪</div>
                    <div class="program-content">
                        <h3>{{PROGRAM_1_NAME}}</h3>
                        <p>{{PROGRAM_1_DESC}}</p>
                        <a href="#" class="learn-more">Learn More →</a>
                    </div>
                </div>
                <div class="program-card">
                    <div class="program-image">🏃</div>
                    <div class="program-content">
                        <h3>{{PROGRAM_2_NAME}}</h3>
                        <p>{{PROGRAM_2_DESC}}</p>
                        <a href="#" class="learn-more">Learn More →</a>
                    </div>
                </div>
                <div class="program-card">
                    <div class="program-image">🧘</div>
                    <div class="program-content">
                        <h3>{{PROGRAM_3_NAME}}</h3>
                        <p>{{PROGRAM_3_DESC}}</p>
                        <a href="#" class="learn-more">Learn More →</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="stats">
        <div class="container">
            <div class="stats-grid">
                <div>
                    <div class="stat-item">{{STAT_1_NUMBER}}</div>
                    <div class="stat-label">{{STAT_1_LABEL}}</div>
                </div>
                <div>
                    <div class="stat-item">{{STAT_2_NUMBER}}</div>
                    <div class="stat-label">{{STAT_2_LABEL}}</div>
                </div>
                <div>
                    <div class="stat-item">{{STAT_3_NUMBER}}</div>
                    <div class="stat-label">{{STAT_3_LABEL}}</div>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    },

    "photography": {
        "name": "Photography Studio",
        "category": "Creative",
        "description": "Photography portfolio with gallery",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Georgia', serif; line-height: 1.6; color: #333; }
        .container { max-width: 1400px; margin: 0 auto; padding: 0 20px; }

        /* Header */
        header { background: white; padding: 40px 0; text-align: center; border-bottom: 1px solid #eee; }
        header h1 { font-size: 3rem; margin-bottom: 0.5rem; color: #2c3e50; font-weight: 400; }
        header p { font-size: 1.2rem; color: #666; font-style: italic; }

        /* Navigation */
        nav { background: #f8f9fa; padding: 20px 0; position: sticky; top: 0; z-index: 100; }
        nav ul { list-style: none; display: flex; justify-content: center; gap: 40px; }
        nav a { color: #333; text-decoration: none; font-weight: 500; transition: color 0.3s; }
        nav a:hover { color: {{PRIMARY_COLOR}}; }

        /* Gallery */
        .gallery { padding: 80px 0; }
        .gallery h2 { text-align: center; font-size: 2.5rem; margin-bottom: 3rem; color: #2c3e50; font-weight: 400; }
        .gallery-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(400px, 1fr)); gap: 20px; }
        .gallery-item { position: relative; overflow: hidden; border-radius: 5px; aspect-ratio: 4/3; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); display: flex; align-items: center; justify-content: center; font-size: 3rem; transition: transform 0.3s; cursor: pointer; }
        .gallery-item:hover { transform: scale(1.02); }

        /* About */
        .about { padding: 100px 0; background: #f8f9fa; }
        .about-content { max-width: 800px; margin: 0 auto; text-align: center; }
        .about h2 { font-size: 2.5rem; margin-bottom: 2rem; color: #2c3e50; font-weight: 400; }
        .about p { font-size: 1.2rem; color: #666; line-height: 1.9; margin-bottom: 2rem; }

        /* Contact */
        .contact { padding: 100px 0; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; text-align: center; }
        .contact h2 { font-size: 2.5rem; margin-bottom: 1.5rem; font-weight: 400; }
        .contact p { font-size: 1.2rem; margin-bottom: 2rem; }
        .contact-btn { display: inline-block; padding: 15px 40px; background: white; color: {{PRIMARY_COLOR}}; text-decoration: none; border-radius: 5px; font-weight: 600; transition: transform 0.3s; }
        .contact-btn:hover { transform: scale(1.05); }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 40px 0; text-align: center; }

        @media (max-width: 768px) {
            .gallery-grid { grid-template-columns: 1fr; }
            nav ul { flex-direction: column; align-items: center; gap: 15px; }
            header h1 { font-size: 2rem; }
        }
    </style>
</head>
<body>
    <header>
        <h1>{{PHOTOGRAPHER_NAME}}</h1>
        <p>{{TAGLINE}}</p>
    </header>

    <nav>
        <ul>
            <li><a href="#gallery">Gallery</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section id="gallery" class="gallery">
        <div class="container">
            <h2>Portfolio</h2>
            <div class="gallery-grid">
                <div class="gallery-item">📷</div>
                <div class="gallery-item">🌅</div>
                <div class="gallery-item">🏔️</div>
                <div class="gallery-item">🌃</div>
                <div class="gallery-item">🎭</div>
                <div class="gallery-item">🌺</div>
            </div>
        </div>
    </section>

    <section id="about" class="about">
        <div class="container">
            <div class="about-content">
                <h2>About Me</h2>
                <p>{{ABOUT_TEXT}}</p>
            </div>
        </div>
    </section>

    <section id="contact" class="contact">
        <div class="container">
            <h2>Let's Create Something Beautiful</h2>
            <p>{{CONTACT_TEXT}}</p>
            <a href="mailto:{{EMAIL}}" class="contact-btn">Get In Touch</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    },

    "consulting": {
        "name": "Business Consulting",
        "category": "Business",
        "description": "Professional consulting firm website",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Header */
        header { background: white; padding: 25px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 100; }
        header .container { display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 1.8rem; font-weight: 700; color: {{PRIMARY_COLOR}}; }
        nav ul { list-style: none; display: flex; gap: 35px; }
        nav a { color: #333; text-decoration: none; font-weight: 500; transition: color 0.3s; }
        nav a:hover { color: {{PRIMARY_COLOR}}; }

        /* Hero */
        .hero { background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); color: white; padding: 120px 0; }
        .hero h1 { font-size: 3.5rem; margin-bottom: 1.5rem; line-height: 1.2; }
        .hero p { font-size: 1.3rem; margin-bottom: 2.5rem; opacity: 0.95; max-width: 600px; }
        .hero-btn { display: inline-block; padding: 15px 40px; background: {{PRIMARY_COLOR}}; color: white; text-decoration: none; border-radius: 5px; font-weight: 600; transition: background 0.3s; }
        .hero-btn:hover { background: {{SECONDARY_COLOR}}; }

        /* Services */
        .services { padding: 100px 0; background: #f8f9fa; }
        .services h2 { text-align: center; font-size: 2.8rem; margin-bottom: 4rem; color: #2c3e50; }
        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; }
        .service-card { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 5px 25px rgba(0,0,0,0.08); border-left: 4px solid {{PRIMARY_COLOR}}; }
        .service-card h3 { font-size: 1.5rem; margin-bottom: 15px; color: #2c3e50; }
        .service-card p { color: #666; line-height: 1.7; }

        /* Why Us */
        .why-us { padding: 100px 0; }
        .why-us h2 { text-align: center; font-size: 2.8rem; margin-bottom: 4rem; color: #2c3e50; }
        .why-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; }
        .why-item { text-align: center; padding: 30px; }
        .why-icon { width: 80px; height: 80px; margin: 0 auto 20px; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; color: white; }
        .why-item h3 { margin-bottom: 15px; color: #2c3e50; }
        .why-item p { color: #666; }

        /* CTA */
        .cta { padding: 100px 0; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; text-align: center; }
        .cta h2 { font-size: 3rem; margin-bottom: 1.5rem; }
        .cta p { font-size: 1.3rem; margin-bottom: 2.5rem; }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 50px 0; text-align: center; }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            header .container { flex-direction: column; gap: 20px; }
            nav ul { flex-direction: column; align-items: center; gap: 15px; }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">{{FIRM_NAME}}</div>
            <nav>
                <ul>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#why-us">Why Us</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <h1>{{HERO_TITLE}}</h1>
            <p>{{HERO_SUBTITLE}}</p>
            <a href="#contact" class="hero-btn">{{CTA_TEXT}}</a>
        </div>
    </section>

    <section id="services" class="services">
        <div class="container">
            <h2>Our Services</h2>
            <div class="services-grid">
                <div class="service-card">
                    <h3>{{SERVICE_1_TITLE}}</h3>
                    <p>{{SERVICE_1_DESC}}</p>
                </div>
                <div class="service-card">
                    <h3>{{SERVICE_2_TITLE}}</h3>
                    <p>{{SERVICE_2_DESC}}</p>
                </div>
                <div class="service-card">
                    <h3>{{SERVICE_3_TITLE}}</h3>
                    <p>{{SERVICE_3_DESC}}</p>
                </div>
            </div>
        </div>
    </section>

    <section id="why-us" class="why-us">
        <div class="container">
            <h2>Why Choose Us</h2>
            <div class="why-grid">
                <div class="why-item">
                    <div class="why-icon">⭐</div>
                    <h3>{{WHY_1_TITLE}}</h3>
                    <p>{{WHY_1_DESC}}</p>
                </div>
                <div class="why-item">
                    <div class="why-icon">🎯</div>
                    <h3>{{WHY_2_TITLE}}</h3>
                    <p>{{WHY_2_DESC}}</p>
                </div>
                <div class="why-item">
                    <div class="why-icon">💼</div>
                    <h3>{{WHY_3_TITLE}}</h3>
                    <p>{{WHY_3_DESC}}</p>
                </div>
            </div>
        </div>
    </section>

    <section id="contact" class="cta">
        <div class="container">
            <h2>{{CTA_TITLE}}</h2>
            <p>{{CTA_SUBTITLE}}</p>
            <a href="mailto:{{EMAIL}}" class="hero-btn">{{CTA_BUTTON}}</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    },

    "education": {
        "name": "Online Education",
        "category": "Education",
        "description": "Online learning platform website",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Navigation */
        nav { background: white; padding: 20px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 100; }
        nav .container { display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 1.5rem; font-weight: 700; color: {{PRIMARY_COLOR}}; }
        nav ul { list-style: none; display: flex; gap: 30px; }
        nav a { color: #333; text-decoration: none; font-weight: 500; }
        .enroll-btn { background: {{PRIMARY_COLOR}}; color: white; padding: 10px 25px; border-radius: 25px; }

        /* Hero */
        .hero { background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; padding: 100px 0; text-align: center; }
        .hero h1 { font-size: 3.5rem; margin-bottom: 1.5rem; }
        .hero p { font-size: 1.3rem; margin-bottom: 2.5rem; opacity: 0.95; }
        .hero-btn { display: inline-block; padding: 18px 45px; background: white; color: {{PRIMARY_COLOR}}; text-decoration: none; border-radius: 50px; font-weight: 600; font-size: 1.1rem; transition: transform 0.3s; }
        .hero-btn:hover { transform: scale(1.05); }

        /* Courses */
        .courses { padding: 100px 0; background: #f8f9fa; }
        .courses h2 { text-align: center; font-size: 2.8rem; margin-bottom: 4rem; color: #2c3e50; }
        .courses-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 40px; }
        .course-card { background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 5px 25px rgba(0,0,0,0.1); transition: transform 0.3s; }
        .course-card:hover { transform: translateY(-10px); }
        .course-image { width: 100%; height: 200px; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); display: flex; align-items: center; justify-content: center; font-size: 4rem; }
        .course-content { padding: 30px; }
        .course-content h3 { font-size: 1.5rem; margin-bottom: 15px; color: #2c3e50; }
        .course-content p { color: #666; margin-bottom: 20px; line-height: 1.7; }
        .course-meta { display: flex; justify-content: space-between; margin-bottom: 20px; font-size: 0.9rem; color: #666; }
        .course-btn { display: block; text-align: center; padding: 12px; background: {{PRIMARY_COLOR}}; color: white; text-decoration: none; border-radius: 5px; font-weight: 600; transition: background 0.3s; }
        .course-btn:hover { background: {{SECONDARY_COLOR}}; }

        /* Stats */
        .stats { padding: 80px 0; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; }
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; text-align: center; }
        .stat-number { font-size: 3rem; font-weight: 700; margin-bottom: 10px; }
        .stat-label { font-size: 1.1rem; opacity: 0.95; }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 50px 0; text-align: center; }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            nav .container { flex-direction: column; gap: 20px; }
            nav ul { flex-direction: column; align-items: center; gap: 15px; }
            .courses-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <div class="logo">{{PLATFORM_NAME}}</div>
            <ul>
                <li><a href="#courses">Courses</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#" class="enroll-btn">Enroll Now</a></li>
            </ul>
        </div>
    </nav>

    <section class="hero">
        <div class="container">
            <h1>{{HERO_TITLE}}</h1>
            <p>{{HERO_SUBTITLE}}</p>
            <a href="#courses" class="hero-btn">{{CTA_TEXT}}</a>
        </div>
    </section>

    <section id="courses" class="courses">
        <div class="container">
            <h2>Popular Courses</h2>
            <div class="courses-grid">
                <div class="course-card">
                    <div class="course-image">📚</div>
                    <div class="course-content">
                        <h3>{{COURSE_1_TITLE}}</h3>
                        <p>{{COURSE_1_DESC}}</p>
                        <div class="course-meta">
                            <span>⏱️ {{COURSE_1_DURATION}}</span>
                            <span>👥 {{COURSE_1_STUDENTS}}</span>
                        </div>
                        <a href="#" class="course-btn">Enroll Now</a>
                    </div>
                </div>
                <div class="course-card">
                    <div class="course-image">💻</div>
                    <div class="course-content">
                        <h3>{{COURSE_2_TITLE}}</h3>
                        <p>{{COURSE_2_DESC}}</p>
                        <div class="course-meta">
                            <span>⏱️ {{COURSE_2_DURATION}}</span>
                            <span>👥 {{COURSE_2_STUDENTS}}</span>
                        </div>
                        <a href="#" class="course-btn">Enroll Now</a>
                    </div>
                </div>
                <div class="course-card">
                    <div class="course-image">🎨</div>
                    <div class="course-content">
                        <h3>{{COURSE_3_TITLE}}</h3>
                        <p>{{COURSE_3_DESC}}</p>
                        <div class="course-meta">
                            <span>⏱️ {{COURSE_3_DURATION}}</span>
                            <span>👥 {{COURSE_3_STUDENTS}}</span>
                        </div>
                        <a href="#" class="course-btn">Enroll Now</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="stats">
        <div class="container">
            <div class="stats-grid">
                <div>
                    <div class="stat-number">{{STAT_1_NUMBER}}</div>
                    <div class="stat-label">{{STAT_1_LABEL}}</div>
                </div>
                <div>
                    <div class="stat-number">{{STAT_2_NUMBER}}</div>
                    <div class="stat-label">{{STAT_2_LABEL}}</div>
                </div>
                <div>
                    <div class="stat-number">{{STAT_3_NUMBER}}</div>
                    <div class="stat-label">{{STAT_3_LABEL}}</div>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    },

    "event": {
        "name": "Event Conference",
        "category": "Events",
        "description": "Conference and event website",
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Hero */
        .hero { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; padding: 150px 0; text-align: center; }
        .hero-badge { display: inline-block; background: rgba(255,255,255,0.2); padding: 10px 25px; border-radius: 25px; font-size: 0.9rem; margin-bottom: 2rem; }
        .hero h1 { font-size: 4rem; margin-bottom: 1rem; font-weight: 700; }
        .hero-date { font-size: 1.5rem; margin-bottom: 1rem; opacity: 0.95; }
        .hero-location { font-size: 1.2rem; margin-bottom: 2.5rem; opacity: 0.9; }
        .register-btn { display: inline-block; padding: 18px 50px; background: white; color: {{PRIMARY_COLOR}}; text-decoration: none; border-radius: 50px; font-weight: 700; font-size: 1.1rem; transition: transform 0.3s; }
        .register-btn:hover { transform: scale(1.05); }

        /* Speakers */
        .speakers { padding: 100px 0; background: #f8f9fa; }
        .speakers h2 { text-align: center; font-size: 3rem; margin-bottom: 4rem; color: #2c3e50; }
        .speakers-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; }
        .speaker-card { background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 5px 25px rgba(0,0,0,0.1); text-align: center; transition: transform 0.3s; }
        .speaker-card:hover { transform: translateY(-10px); }
        .speaker-photo { width: 100%; height: 300px; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); display: flex; align-items: center; justify-content: center; font-size: 5rem; }
        .speaker-info { padding: 30px; }
        .speaker-name { font-size: 1.5rem; margin-bottom: 10px; color: #2c3e50; font-weight: 600; }
        .speaker-title { color: {{PRIMARY_COLOR}}; margin-bottom: 15px; }
        .speaker-bio { color: #666; line-height: 1.7; }

        /* Schedule */
        .schedule { padding: 100px 0; }
        .schedule h2 { text-align: center; font-size: 3rem; margin-bottom: 4rem; color: #2c3e50; }
        .schedule-list { max-width: 900px; margin: 0 auto; }
        .schedule-item { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 5px 20px rgba(0,0,0,0.08); margin-bottom: 25px; border-left: 5px solid {{PRIMARY_COLOR}}; }
        .schedule-time { font-size: 1.2rem; color: {{PRIMARY_COLOR}}; font-weight: 700; margin-bottom: 15px; }
        .schedule-title { font-size: 1.5rem; margin-bottom: 10px; color: #2c3e50; }
        .schedule-desc { color: #666; line-height: 1.7; }

        /* Register CTA */
        .cta { padding: 100px 0; background: linear-gradient(135deg, {{PRIMARY_COLOR}} 0%, {{SECONDARY_COLOR}} 100%); color: white; text-align: center; }
        .cta h2 { font-size: 3rem; margin-bottom: 1.5rem; }
        .cta p { font-size: 1.3rem; margin-bottom: 2.5rem; }

        /* Footer */
        footer { background: #2c3e50; color: white; padding: 50px 0; text-align: center; }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .speakers-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <section class="hero">
        <div class="container">
            <div class="hero-badge">{{EVENT_TYPE}}</div>
            <h1>{{EVENT_NAME}}</h1>
            <div class="hero-date">📅 {{EVENT_DATE}}</div>
            <div class="hero-location">📍 {{EVENT_LOCATION}}</div>
            <a href="#register" class="register-btn">Register Now</a>
        </div>
    </section>

    <section class="speakers">
        <div class="container">
            <h2>Featured Speakers</h2>
            <div class="speakers-grid">
                <div class="speaker-card">
                    <div class="speaker-photo">👤</div>
                    <div class="speaker-info">
                        <div class="speaker-name">{{SPEAKER_1_NAME}}</div>
                        <div class="speaker-title">{{SPEAKER_1_TITLE}}</div>
                        <p class="speaker-bio">{{SPEAKER_1_BIO}}</p>
                    </div>
                </div>
                <div class="speaker-card">
                    <div class="speaker-photo">👥</div>
                    <div class="speaker-info">
                        <div class="speaker-name">{{SPEAKER_2_NAME}}</div>
                        <div class="speaker-title">{{SPEAKER_2_TITLE}}</div>
                        <p class="speaker-bio">{{SPEAKER_2_BIO}}</p>
                    </div>
                </div>
                <div class="speaker-card">
                    <div class="speaker-photo">🎤</div>
                    <div class="speaker-info">
                        <div class="speaker-name">{{SPEAKER_3_NAME}}</div>
                        <div class="speaker-title">{{SPEAKER_3_TITLE}}</div>
                        <p class="speaker-bio">{{SPEAKER_3_BIO}}</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="schedule">
        <div class="container">
            <h2>Event Schedule</h2>
            <div class="schedule-list">
                <div class="schedule-item">
                    <div class="schedule-time">{{SESSION_1_TIME}}</div>
                    <div class="schedule-title">{{SESSION_1_TITLE}}</div>
                    <p class="schedule-desc">{{SESSION_1_DESC}}</p>
                </div>
                <div class="schedule-item">
                    <div class="schedule-time">{{SESSION_2_TIME}}</div>
                    <div class="schedule-title">{{SESSION_2_TITLE}}</div>
                    <p class="schedule-desc">{{SESSION_2_DESC}}</p>
                </div>
                <div class="schedule-item">
                    <div class="schedule-time">{{SESSION_3_TIME}}</div>
                    <div class="schedule-title">{{SESSION_3_TITLE}}</div>
                    <p class="schedule-desc">{{SESSION_3_DESC}}</p>
                </div>
            </div>
        </div>
    </section>

    <section id="register" class="cta">
        <div class="container">
            <h2>{{CTA_TITLE}}</h2>
            <p>{{CTA_SUBTITLE}}</p>
            <a href="#" class="register-btn">{{CTA_BUTTON}}</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{{FOOTER_TEXT}}</p>
        </div>
    </footer>
</body>
</html>"""
    }
}

# Default values for template variables
DEFAULT_VALUES = {
    "PRIMARY_COLOR": "#667eea",
    "SECONDARY_COLOR": "#764ba2",
    "TITLE": "My Website",
    "FOOTER_TEXT": "© 2024 All Rights Reserved"
}
