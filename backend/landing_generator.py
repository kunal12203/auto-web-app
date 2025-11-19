"""
Landing Page Template Generator - Generates hero sections, features, CTAs, testimonials
Target: 1,000 landing page templates
"""

import logging
from typing import List
from template_generator_core import (
    BaseTemplateGenerator,
    TemplateSpec,
    VariationConfig,
    sanitize_component_name,
    generate_component_imports
)

logger = logging.getLogger(__name__)


# ============================================================================
# HERO SECTION GENERATOR
# ============================================================================

class HeroGenerator(BaseTemplateGenerator):
    """Generates hero section templates"""

    def get_domain(self) -> str:
        return "landing"

    def get_category(self) -> str:
        return "hero"

    def get_variation_config(self) -> VariationConfig:
        """Define hero variations"""
        return VariationConfig(
            styles=[
                'modern',
                'minimal',
                'gradient',
                'glassmorphism',
                'illustrated',
                'video_background',
                'animated'
            ],
            layouts=[
                'centered',
                'split',
                'asymmetric',
                'fullscreen',
                'with_image',
                'with_video'
            ],
            features=[
                # Basic
                ['headline', 'subheadline', 'cta_primary'],
                ['headline', 'subheadline', 'cta_primary', 'cta_secondary'],

                # With visual
                ['headline', 'subheadline', 'cta_primary', 'hero_image'],
                ['headline', 'subheadline', 'cta_primary', 'hero_video'],

                # With features list
                ['headline', 'subheadline', 'cta_primary', 'feature_list'],
                ['headline', 'subheadline', 'cta_primary', 'feature_list', 'hero_image'],

                # With social proof
                ['headline', 'subheadline', 'cta_primary', 'social_proof'],
                ['headline', 'subheadline', 'cta_primary', 'social_proof', 'testimonial'],

                # With form
                ['headline', 'subheadline', 'email_capture'],
                ['headline', 'subheadline', 'email_capture', 'social_proof'],

                # Full featured
                ['headline', 'subheadline', 'cta_primary', 'cta_secondary', 'hero_image', 'social_proof'],
                ['headline', 'subheadline', 'cta_primary', 'feature_list', 'hero_image', 'trust_badges'],
            ],
            animations=[
                'none',
                'fade_in',
                'slide_up',
                'scale_in',
                'parallax'
            ],
            complexities=['simple', 'standard', 'advanced']
        )

    def generate_code(self, spec: TemplateSpec) -> str:
        """Generate hero section component"""
        component_name = spec.get_name()

        imports = generate_component_imports(spec.features)
        imports += "\nimport { FiCheck, FiPlay } from 'react-icons/fi'"

        # Build state declarations
        state_declarations = []
        if 'email_capture' in spec.features:
            state_declarations.append("const [email, setEmail] = React.useState('');")
        if 'hero_video' in spec.features:
            state_declarations.append("const [isVideoPlaying, setIsVideoPlaying] = React.useState(false);")

        states_code = '\n  '.join(state_declarations) if state_declarations else ''

        # Build email handler
        email_handler = ""
        if 'email_capture' in spec.features:
            email_handler = "const handleEmailSubmit = (e) => { e.preventDefault(); console.log('Email:', email); };"

        code = f'''{imports}

/**
 * {component_name} Component
 *
 * {spec.style.title()} style hero section
 * Layout: {spec.layout}
 *
 * @component
 */
const {component_name} = () => {{
  {states_code}

  {email_handler}

  return (
    <section className="hero {spec.layout}-layout {spec.style}-style {spec.animation}-animation">
      <div className="hero-container">
'''

        if spec.layout == 'split':
            code += self._generate_split_layout(spec)
        elif spec.layout == 'centered':
            code += self._generate_centered_layout(spec)
        elif spec.layout == 'fullscreen':
            code += self._generate_fullscreen_layout(spec)
        else:
            code += self._generate_default_layout(spec)

        code += '''      </div>
    </section>
  );
};

export default {component_name};
'''.format(component_name=component_name)

        return code

    def _generate_split_layout(self, spec: TemplateSpec) -> str:
        """Generate split layout (text left, visual right)"""
        return f'''        <div className="hero-content">
          <div className="hero-text">
            {self._generate_headline(spec)}
            {self._generate_subheadline(spec)}
            {self._generate_feature_list(spec) if 'feature_list' in spec.features else ''}
            {self._generate_cta_buttons(spec)}
            {self._generate_social_proof(spec) if 'social_proof' in spec.features else ''}
          </div>

          <div className="hero-visual">
            {self._generate_visual(spec)}
          </div>
        </div>'''

    def _generate_centered_layout(self, spec: TemplateSpec) -> str:
        """Generate centered layout"""
        return f'''        <div className="hero-centered">
          {self._generate_headline(spec)}
          {self._generate_subheadline(spec)}
          {self._generate_cta_buttons(spec)}
          {self._generate_social_proof(spec) if 'social_proof' in spec.features else ''}
          {self._generate_visual(spec) if 'hero_image' in spec.features or 'hero_video' in spec.features else ''}
        </div>'''

    def _generate_fullscreen_layout(self, spec: TemplateSpec) -> str:
        """Generate fullscreen layout"""
        return f'''        <div className="hero-fullscreen">
          <div className="hero-overlay">
            {self._generate_headline(spec)}
            {self._generate_subheadline(spec)}
            {self._generate_cta_buttons(spec)}
          </div>
          {self._generate_background_visual(spec)}
        </div>'''

    def _generate_default_layout(self, spec: TemplateSpec) -> str:
        """Generate default layout"""
        return self._generate_split_layout(spec)

    def _generate_headline(self, spec: TemplateSpec) -> str:
        """Generate headline"""
        return '''<h1 className="hero-headline">
              Build Amazing Products Faster
            </h1>'''

    def _generate_subheadline(self, spec: TemplateSpec) -> str:
        """Generate subheadline"""
        return '''<p className="hero-subheadline">
              The complete platform for modern teams to design, develop, and deploy exceptional web applications.
            </p>'''

    def _generate_cta_buttons(self, spec: TemplateSpec) -> str:
        """Generate CTA buttons"""
        if 'email_capture' in spec.features:
            return '''<form onSubmit={handleEmailSubmit} className="email-capture">
              <input
                type="email"
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
              <button type="submit" className="btn btn-primary">Get Started</button>
            </form>'''

        secondary = '''<a href="/learn-more" className="btn btn-secondary">
                Learn More
              </a>''' if 'cta_secondary' in spec.features else ''

        return f'''<div className="hero-cta">
              <a href="/signup" className="btn btn-primary">
                Get Started Free
              </a>
              {secondary}
            </div>'''

    def _generate_feature_list(self, spec: TemplateSpec) -> str:
        """Generate feature list"""
        return '''<ul className="hero-features">
              <li><FiCheck /> No credit card required</li>
              <li><FiCheck /> 14-day free trial</li>
              <li><FiCheck /> Cancel anytime</li>
            </ul>'''

    def _generate_social_proof(self, spec: TemplateSpec) -> str:
        """Generate social proof"""
        if 'testimonial' in spec.features:
            return '''<div className="hero-social-proof">
              <div className="testimonial">
                <p>"This product changed how we work. Highly recommended!"</p>
                <div className="author">
                  <img src="/avatar.jpg" alt="John Doe" />
                  <div>
                    <strong>John Doe</strong>
                    <span>CEO, Acme Inc</span>
                  </div>
                </div>
              </div>
            </div>'''

        return '''<div className="hero-social-proof">
              <p className="proof-text">Trusted by 10,000+ companies worldwide</p>
              <div className="company-logos">
                <img src="/company1.svg" alt="Company 1" />
                <img src="/company2.svg" alt="Company 2" />
                <img src="/company3.svg" alt="Company 3" />
              </div>
            </div>'''

    def _generate_visual(self, spec: TemplateSpec) -> str:
        """Generate visual element"""
        if 'hero_video' in spec.features:
            return '''<div className="hero-video">
              <video
                src="/hero-video.mp4"
                poster="/video-poster.jpg"
                controls={isVideoPlaying}
                onClick={() => setIsVideoPlaying(true)}
              />
              {!isVideoPlaying && (
                <button className="play-button" onClick={() => setIsVideoPlaying(true)}>
                  <FiPlay />
                </button>
              )}
            </div>'''

        if 'hero_image' in spec.features:
            return '''<img
              src="/hero-image.png"
              alt="Product preview"
              className="hero-image"
            />'''

        return ''

    def _generate_background_visual(self, spec: TemplateSpec) -> str:
        """Generate background visual for fullscreen"""
        if 'hero_video' in spec.features:
            return '''<video
            className="background-video"
            src="/bg-video.mp4"
            autoPlay
            loop
            muted
          />'''
        return ''


# ============================================================================
# FEATURES SECTION GENERATOR
# ============================================================================

class FeaturesGenerator(BaseTemplateGenerator):
    """Generates feature section templates"""

    def get_domain(self) -> str:
        return "landing"

    def get_category(self) -> str:
        return "features"

    def get_variation_config(self) -> VariationConfig:
        """Define feature section variations"""
        return VariationConfig(
            styles=[
                'modern',
                'minimal',
                'cards',
                'illustrated',
                'icons'
            ],
            layouts=[
                'grid',
                'list',
                'alternating',
                'tabs',
                'accordion'
            ],
            features=[
                # Basic
                ['icon', 'title', 'description'],
                ['icon', 'title', 'description', 'link'],

                # With visuals
                ['icon', 'title', 'description', 'image'],
                ['icon', 'title', 'description', 'image', 'cta'],

                # Interactive
                ['icon', 'title', 'description', 'hover_effect'],
                ['icon', 'title', 'description', 'expandable'],

                # Rich content
                ['icon', 'title', 'description', 'stats'],
                ['icon', 'title', 'description', 'testimonial'],
            ],
            animations=['none', 'fade', 'slide', 'scale'],
            complexities=['simple', 'standard']
        )

    def generate_code(self, spec: TemplateSpec) -> str:
        """Generate features section"""
        component_name = spec.get_name()

        # Build link element
        link_element = '<a href="#">Learn more →</a>' if 'link' in spec.features else ''

        code = f'''import React from 'react'
import {{ FiZap, FiShield, FiTrendingUp, FiUsers }} from 'react-icons/fi'

const {component_name} = () => {{
  const features = [
    {{
      icon: <FiZap />,
      title: "Lightning Fast",
      description: "Blazing fast performance that scales with your business"
    }},
    {{
      icon: <FiShield />,
      title: "Secure & Reliable",
      description: "Enterprise-grade security with 99.9% uptime"
    }},
    {{
      icon: <FiTrendingUp />,
      title: "Scale with Ease",
      description: "Grow from startup to enterprise seamlessly"
    }},
    {{
      icon: <FiUsers />,
      title: "Team Collaboration",
      description: "Built for teams of all sizes"
    }}
  ];

  return (
    <section className="features {spec.layout}-layout {spec.style}-style">
      <div className="container">
        <div className="section-header">
          <h2>Powerful Features</h2>
          <p>Everything you need to build amazing products</p>
        </div>

        <div className="features-{spec.layout}">
          {{features.map((feature, index) => (
            <div key={{index}} className="feature-item">
              <div className="feature-icon">{{feature.icon}}</div>
              <h3>{{feature.title}}</h3>
              <p>{{feature.description}}</p>
              {link_element}
            </div>
          ))}}
        </div>
      </div>
    </section>
  );
}};

export default {component_name};
'''
        return code


# ============================================================================
# CTA SECTION GENERATOR
# ============================================================================

class CTAGenerator(BaseTemplateGenerator):
    """Generates CTA (Call-to-Action) section templates"""

    def get_domain(self) -> str:
        return "landing"

    def get_category(self) -> str:
        return "cta"

    def get_variation_config(self) -> VariationConfig:
        """Define CTA variations"""
        return VariationConfig(
            styles=[
                'modern',
                'minimal',
                'gradient',
                'bold',
                'subtle'
            ],
            layouts=[
                'centered',
                'split',
                'banner',
                'popup',
                'sticky_bar'
            ],
            features=[
                # Basic
                ['headline', 'button'],
                ['headline', 'description', 'button'],
                ['headline', 'description', 'button_primary', 'button_secondary'],

                # With form
                ['headline', 'email_input', 'button'],
                ['headline', 'description', 'email_input', 'button'],

                # With urgency
                ['headline', 'countdown', 'button'],
                ['headline', 'limited_offer', 'button'],

                # With social proof
                ['headline', 'button', 'testimonial'],
                ['headline', 'button', 'trust_badges'],
            ],
            animations=['none', 'fade', 'slide'],
            complexities=['simple', 'standard']
        )

    def generate_code(self, spec: TemplateSpec) -> str:
        """Generate CTA section"""
        component_name = spec.get_name()

        # Build conditional elements
        email_state = "const [email, setEmail] = React.useState('');" if 'email_input' in spec.features else ''
        description = '<p>Join thousands of happy customers today</p>' if 'description' in spec.features else ''
        email_input = '<input type="email" placeholder="Enter your email" value={email} onChange={(e) => setEmail(e.target.value)} />' if 'email_input' in spec.features else ''
        secondary_btn = '<button className="btn btn-secondary">Learn More</button>' if 'button_secondary' in spec.features else ''
        trust_note = '<p className="cta-note">No credit card required • 14-day free trial</p>' if 'trust_badges' in spec.features else ''

        code = f'''import React from 'react'

const {component_name} = () => {{
  {email_state}

  return (
    <section className="cta {spec.layout}-layout {spec.style}-style">
      <div className="cta-container">
        <h2>Ready to Get Started?</h2>
        {description}

        <div className="cta-actions">
          {email_input}
          <button className="btn btn-primary">Get Started Free</button>
          {secondary_btn}
        </div>

        {trust_note}
      </div>
    </section>
  );
}};

export default {component_name};
'''
        return code


# ============================================================================
# TESTIMONIALS GENERATOR
# ============================================================================

class TestimonialsGenerator(BaseTemplateGenerator):
    """Generates testimonial section templates"""

    def get_domain(self) -> str:
        return "landing"

    def get_category(self) -> str:
        return "testimonials"

    def get_variation_config(self) -> VariationConfig:
        """Define testimonial variations"""
        return VariationConfig(
            styles=[
                'modern',
                'minimal',
                'cards',
                'quotes'
            ],
            layouts=[
                'grid',
                'carousel',
                'masonry',
                'single_large'
            ],
            features=[
                ['avatar', 'name', 'role', 'quote'],
                ['avatar', 'name', 'role', 'company', 'quote'],
                ['avatar', 'name', 'role', 'company', 'quote', 'rating'],
                ['avatar', 'name', 'role', 'company', 'quote', 'rating', 'company_logo'],
            ],
            animations=['none', 'fade', 'slide'],
            complexities=['simple', 'standard']
        )

    def generate_code(self, spec: TemplateSpec) -> str:
        """Generate testimonials section"""
        component_name = spec.get_name()

        code = f'''import React from 'react'
import {{ FaStar }} from 'react-icons/fa'

const {component_name} = () => {{
  const testimonials = [
    {{
      name: "Sarah Johnson",
      role: "CEO",
      company: "Tech Corp",
      quote: "This product has transformed how our team works. Highly recommended!",
      avatar: "/avatar1.jpg",
      rating: 5
    }},
    // More testimonials...
  ];

  return (
    <section className="testimonials {spec.layout}-layout {spec.style}-style">
      <div className="container">
        <h2>What Our Customers Say</h2>

        <div className="testimonials-{spec.layout}">
          {{testimonials.map((t, i) => (
            <div key={{i}} className="testimonial-card">
              {'<div className="rating">{Array(t.rating).fill().map((_, i) => <FaStar key={i} />)}</div>' if 'rating' in spec.features else ''}
              <p className="quote">{{t.quote}}</p>
              <div className="author">
                <img src={{t.avatar}} alt={{t.name}} />
                <div>
                  <strong>{{t.name}}</strong>
                  <span>{{t.role}} at {{t.company}}</span>
                </div>
              </div>
            </div>
          ))}}
        </div>
      </div>
    </section>
  );
}};

export default {component_name};
'''
        return code
