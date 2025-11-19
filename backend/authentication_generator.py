"""
Authentication Template Generator - Generates login, signup, password management templates
Target: 1,000 authentication templates
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
# AUTHENTICATION TEMPLATE GENERATOR
# ============================================================================

class AuthenticationGenerator(BaseTemplateGenerator):
    """
    Generates comprehensive authentication templates

    Categories:
    - Login forms (300 templates)
    - Signup/Registration (300 templates)
    - Password management (200 templates)
    - 2FA/MFA (100 templates)
    - Social auth (100 templates)
    """

    def get_domain(self) -> str:
        return "authentication"

    def get_category(self) -> str:
        return "login"  # Will be overridden per variant

    def get_variation_config(self) -> VariationConfig:
        """
        Define all possible variations for authentication
        """
        return VariationConfig(
            styles=[
                'modern',
                'minimal',
                'glassmorphism',
                'neumorphism',
                'gradient',
                'flat',
                'material',
                'corporate'
            ],
            layouts=[
                'centered',
                'split',
                'card',
                'fullscreen',
                'sidebar',
                'floating'
            ],
            features=[
                # Basic features
                ['email_input', 'password_input'],
                ['email_input', 'password_input', 'remember_me'],
                ['email_input', 'password_input', 'forgot_password'],
                ['email_input', 'password_input', 'remember_me', 'forgot_password'],

                # Social auth
                ['email_input', 'password_input', 'social_google'],
                ['email_input', 'password_input', 'social_google', 'social_facebook'],
                ['email_input', 'password_input', 'social_google', 'social_facebook', 'social_github'],

                # Advanced features
                ['email_input', 'password_input', 'show_password'],
                ['email_input', 'password_input', 'show_password', 'remember_me'],
                ['email_input', 'password_input', 'show_password', 'validation'],

                # 2FA
                ['email_input', 'password_input', '2fa'],
                ['email_input', 'password_input', '2fa', 'remember_device'],

                # Magic link
                ['email_input', 'magic_link'],

                # Phone auth
                ['phone_input', 'otp'],
                ['phone_input', 'otp', 'country_selector']
            ],
            animations=[
                'none',
                'fade',
                'slide',
                'scale',
                'bounce'
            ],
            complexities=[
                'simple',
                'standard',
                'advanced'
            ]
        )

    def generate_code(self, spec: TemplateSpec) -> str:
        """
        Generate React component code for authentication template
        """
        component_name = spec.get_name()

        # Generate imports
        imports = generate_component_imports(spec.features)

        # Add additional imports based on features
        if 'social_google' in spec.features or 'social_facebook' in spec.features:
            imports += "\nimport { FcGoogle } from 'react-icons/fc'"
            imports += "\nimport { FaFacebook, FaGithub } from 'react-icons/fa'"

        # Build state declarations
        state_declarations = [
            "const [email, setEmail] = React.useState('');",
            "const [password, setPassword] = React.useState('');",
            "const [rememberMe, setRememberMe] = React.useState(false);"
        ]

        if 'show_password' in spec.features:
            state_declarations.append("const [showPassword, setShowPassword] = React.useState(false);")

        if 'otp' in spec.features or '2fa' in spec.features:
            state_declarations.append("const [otp, setOtp] = React.useState('');")

        states_code = '\n  '.join(state_declarations)

        # Generate component
        code = f'''{imports}

/**
 * {component_name} Component
 *
 * {spec.style.title()} style authentication component
 * Layout: {spec.layout}
 * Features: {', '.join(spec.features)}
 *
 * @component
 */
const {component_name} = () => {{
  {states_code}

  const handleSubmit = (e) => {{
    e.preventDefault();
    console.log('Login:', {{ email, password, rememberMe }});
  }};
'''

        # Add social login handler if needed
        if any(f.startswith('social_') for f in spec.features):
            code += '''
  const handleSocialLogin = (provider) => {
    console.log(`Social login: ${provider}`);
  };
'''

        code += f'''
  return (
    <div className="{spec.layout}-layout {spec.style}-style {component_name.lower()}">
'''

        # Add container structure based on layout
        if spec.layout == 'split':
            code += self._generate_split_layout(spec, component_name)
        elif spec.layout == 'centered':
            code += self._generate_centered_layout(spec, component_name)
        elif spec.layout == 'card':
            code += self._generate_card_layout(spec, component_name)
        elif spec.layout == 'fullscreen':
            code += self._generate_fullscreen_layout(spec, component_name)
        else:
            code += self._generate_default_layout(spec, component_name)

        code += '''
    </div>
  );
};

export default {component_name};
'''.format(component_name=component_name)

        return code

    def _generate_default_layout(self, spec: TemplateSpec, name: str) -> str:
        """Generate default layout structure"""
        return f'''      <div className="auth-container">
        <div className="auth-header">
          <h2>Welcome Back</h2>
          <p>Sign in to your account</p>
        </div>

        <form onSubmit={{handleSubmit}} className="auth-form">
          {self._generate_form_fields(spec)}

          {self._generate_action_buttons(spec)}
        </form>

        {self._generate_footer_links(spec)}
      </div>'''

    def _generate_centered_layout(self, spec: TemplateSpec, name: str) -> str:
        """Generate centered layout"""
        return f'''      <div className="centered-container">
        <div className="auth-box">
          <div className="logo-section">
            <img src="/logo.svg" alt="Logo" />
          </div>

          <h1>Sign In</h1>

          {self._generate_social_buttons(spec) if any(f.startswith('social_') for f in spec.features) else ''}

          {('<div className="divider"><span>or</span></div>' if any(f.startswith('social_') for f in spec.features) else '')}

          <form onSubmit={{handleSubmit}}>
            {self._generate_form_fields(spec)}
            {self._generate_action_buttons(spec)}
          </form>

          {self._generate_footer_links(spec)}
        </div>
      </div>'''

    def _generate_split_layout(self, spec: TemplateSpec, name: str) -> str:
        """Generate split screen layout"""
        return f'''      <div className="split-container">
        <div className="split-left">
          <div className="brand-section">
            <h1>Welcome to Our Platform</h1>
            <p>Build amazing things with our tools</p>
            <ul className="features-list">
              <li>✓ Fast and secure authentication</li>
              <li>✓ Multiple login options</li>
              <li>✓ Protected user data</li>
            </ul>
          </div>
        </div>

        <div className="split-right">
          <div className="auth-panel">
            <h2>Sign In</h2>

            {self._generate_social_buttons(spec) if any(f.startswith('social_') for f in spec.features) else ''}

            <form onSubmit={{handleSubmit}}>
              {self._generate_form_fields(spec)}
              {self._generate_action_buttons(spec)}
            </form>

            {self._generate_footer_links(spec)}
          </div>
        </div>
      </div>'''

    def _generate_card_layout(self, spec: TemplateSpec, name: str) -> str:
        """Generate card layout"""
        return f'''      <div className="card-container">
        <div className="auth-card">
          <div className="card-header">
            <h2>Login</h2>
          </div>

          <div className="card-body">
            {self._generate_social_buttons(spec) if any(f.startswith('social_') for f in spec.features) else ''}

            <form onSubmit={{handleSubmit}}>
              {self._generate_form_fields(spec)}
              {self._generate_action_buttons(spec)}
            </form>
          </div>

          <div className="card-footer">
            {self._generate_footer_links(spec)}
          </div>
        </div>
      </div>'''

    def _generate_fullscreen_layout(self, spec: TemplateSpec, name: str) -> str:
        """Generate fullscreen layout"""
        return f'''      <div className="fullscreen-auth">
        <div className="auth-content">
          <div className="brand-header">
            <img src="/logo.svg" alt="Logo" />
            <h1>Sign In</h1>
          </div>

          {self._generate_social_buttons(spec) if any(f.startswith('social_') for f in spec.features) else ''}

          <form onSubmit={{handleSubmit}} className="fullscreen-form">
            {self._generate_form_fields(spec)}
            {self._generate_action_buttons(spec)}
          </form>

          {self._generate_footer_links(spec)}
        </div>
      </div>'''

    def _generate_form_fields(self, spec: TemplateSpec) -> str:
        """Generate form input fields based on features"""
        fields = []

        if 'email_input' in spec.features:
            fields.append('''
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Enter your email"
                required
              />
            </div>''')

        if 'phone_input' in spec.features:
            fields.append('''
            <div className="form-group">
              <label htmlFor="phone">Phone Number</label>
              <input
                type="tel"
                id="phone"
                placeholder="+1 (555) 000-0000"
                required
              />
            </div>''')

        if 'password_input' in spec.features:
            show_toggle = '''
              <button
                type="button"
                className="show-password-btn"
                onClick={() => setShowPassword(!showPassword)}
              >
                {showPassword ? 'Hide' : 'Show'}
              </button>''' if 'show_password' in spec.features else ''

            fields.append(f'''
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <div className="password-input-wrapper">
                <input
                  type={{showPassword ? 'text' : 'password'}}
                  id="password"
                  value={{password}}
                  onChange={{(e) => setPassword(e.target.value)}}
                  placeholder="Enter your password"
                  required
                />{show_toggle}
              </div>
            </div>''')

        if 'otp' in spec.features or '2fa' in spec.features:
            fields.append('''
            <div className="form-group">
              <label htmlFor="otp">One-Time Password</label>
              <input
                type="text"
                id="otp"
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
                placeholder="Enter 6-digit code"
                maxLength="6"
                required
              />
            </div>''')

        if 'remember_me' in spec.features:
            fields.append('''
            <div className="form-group checkbox-group">
              <label>
                <input
                  type="checkbox"
                  checked={rememberMe}
                  onChange={(e) => setRememberMe(e.target.checked)}
                />
                <span>Remember me</span>
              </label>
            </div>''')

        return '\n'.join(fields)

    def _generate_social_buttons(self, spec: TemplateSpec) -> str:
        """Generate social login buttons"""
        buttons = ['<div className="social-login">']

        if 'social_google' in spec.features:
            buttons.append('''
              <button type="button" className="social-btn google-btn" onClick={() => handleSocialLogin('google')}>
                <FcGoogle /> Continue with Google
              </button>''')

        if 'social_facebook' in spec.features:
            buttons.append('''
              <button type="button" className="social-btn facebook-btn" onClick={() => handleSocialLogin('facebook')}>
                <FaFacebook /> Continue with Facebook
              </button>''')

        if 'social_github' in spec.features:
            buttons.append('''
              <button type="button" className="social-btn github-btn" onClick={() => handleSocialLogin('github')}>
                <FaGithub /> Continue with GitHub
              </button>''')

        buttons.append('</div>')
        return '\n'.join(buttons)

    def _generate_action_buttons(self, spec: TemplateSpec) -> str:
        """Generate action buttons"""
        forgot_link = '''
              <a href="/forgot-password" className="forgot-password-link">
                Forgot password?
              </a>''' if 'forgot_password' in spec.features else ''

        return f'''
          <div className="form-actions">
            <button type="submit" className="btn btn-primary">
              Sign In
            </button>{forgot_link}
          </div>'''

    def _generate_footer_links(self, spec: TemplateSpec) -> str:
        """Generate footer links"""
        return '''
          <div className="auth-footer">
            <p>Don't have an account? <a href="/signup">Sign up</a></p>
          </div>'''

    def _infer_variant(self, features: List[str]) -> str:
        """Infer variant from features"""
        if '2fa' in features or 'otp' in features:
            return 'two_factor'
        elif any(f.startswith('social_') for f in features):
            if len([f for f in features if f.startswith('social_')]) >= 3:
                return 'social_multi'
            else:
                return 'social'
        elif 'magic_link' in features:
            return 'magic_link'
        elif 'phone_input' in features:
            return 'phone'
        elif len(features) <= 2:
            return 'simple'
        else:
            return 'standard'

    def _is_valid_combination(self, spec: TemplateSpec) -> bool:
        """Check if combination is valid"""
        # Call parent validation
        if not super()._is_valid_combination(spec):
            return False

        # Authentication-specific validation

        # Must have either email or phone input
        if 'email_input' not in spec.features and 'phone_input' not in spec.features:
            return False

        # If has password, it's standard auth
        # If no password, must have magic_link or otp
        if 'password_input' not in spec.features:
            if 'magic_link' not in spec.features and 'otp' not in spec.features:
                return False

        # 2FA requires base auth
        if '2fa' in spec.features or 'otp' in spec.features:
            if 'password_input' not in spec.features and 'magic_link' not in spec.features:
                return False

        # Phone input requires OTP
        if 'phone_input' in spec.features and 'otp' not in spec.features:
            return False

        return True

    def _infer_use_cases(self, spec: TemplateSpec) -> List[str]:
        """Infer use cases from spec"""
        use_cases = ['authentication', 'user_management']

        if any(f.startswith('social_') for f in spec.features):
            use_cases.extend(['saas', 'social_network'])

        if '2fa' in spec.features:
            use_cases.extend(['enterprise', 'fintech', 'security'])

        if spec.style in ['minimal', 'modern']:
            use_cases.append('startup')

        if spec.style in ['corporate', 'professional']:
            use_cases.append('enterprise')

        return use_cases


# ============================================================================
# SIGNUP/REGISTRATION GENERATOR
# ============================================================================

class SignupGenerator(AuthenticationGenerator):
    """Generates signup/registration templates"""

    def get_category(self) -> str:
        return "signup"

    def get_variation_config(self) -> VariationConfig:
        """Signup-specific variations"""
        config = super().get_variation_config()

        # Signup-specific features
        config.features = [
            # Basic
            ['email_input', 'password_input', 'confirm_password'],
            ['email_input', 'password_input', 'confirm_password', 'name_input'],
            ['email_input', 'password_input', 'confirm_password', 'terms_checkbox'],

            # Full registration
            ['email_input', 'password_input', 'confirm_password', 'name_input', 'terms_checkbox'],
            ['email_input', 'password_input', 'confirm_password', 'name_input', 'phone_input', 'terms_checkbox'],

            # Social signup
            ['email_input', 'password_input', 'social_google'],
            ['email_input', 'password_input', 'social_google', 'social_facebook'],

            # With validation
            ['email_input', 'password_input', 'confirm_password', 'password_strength'],
            ['email_input', 'password_input', 'confirm_password', 'password_strength', 'validation'],

            # Multi-step
            ['email_input', 'multi_step'],
            ['email_input', 'password_input', 'multi_step', 'progress_indicator'],
        ]

        return config

    def _generate_form_fields(self, spec: TemplateSpec) -> str:
        """Override to add signup-specific fields"""
        fields = []

        if 'name_input' in spec.features:
            fields.append('''
            <div className="form-group">
              <label htmlFor="name">Full Name</label>
              <input
                type="text"
                id="name"
                placeholder="Enter your full name"
                required
              />
            </div>''')

        # Get base fields
        fields.append(super()._generate_form_fields(spec))

        if 'confirm_password' in spec.features:
            fields.append('''
            <div className="form-group">
              <label htmlFor="confirmPassword">Confirm Password</label>
              <input
                type="password"
                id="confirmPassword"
                placeholder="Confirm your password"
                required
              />
            </div>''')

        if 'password_strength' in spec.features:
            fields.append('''
            <div className="password-strength">
              <div className="strength-meter">
                <div className="strength-bar"></div>
              </div>
              <span className="strength-text">Password strength: Weak</span>
            </div>''')

        if 'terms_checkbox' in spec.features:
            fields.append('''
            <div className="form-group checkbox-group">
              <label>
                <input type="checkbox" required />
                <span>I agree to the <a href="/terms">Terms of Service</a> and <a href="/privacy">Privacy Policy</a></span>
              </label>
            </div>''')

        return '\n'.join(fields)

    def _generate_footer_links(self, spec: TemplateSpec) -> str:
        """Override footer for signup"""
        return '''
          <div className="auth-footer">
            <p>Already have an account? <a href="/login">Sign in</a></p>
          </div>'''


# ============================================================================
# PASSWORD MANAGEMENT GENERATOR
# ============================================================================

class PasswordManagementGenerator(AuthenticationGenerator):
    """Generates password reset, change password templates"""

    def get_category(self) -> str:
        return "password_management"

    def get_variation_config(self) -> VariationConfig:
        """Password management variations"""
        config = super().get_variation_config()

        config.features = [
            # Forgot password
            ['email_input', 'reset_link'],
            ['email_input', 'reset_link', 'back_to_login'],

            # Reset password
            ['password_input', 'confirm_password', 'reset_token'],
            ['password_input', 'confirm_password', 'reset_token', 'password_strength'],

            # Change password
            ['current_password', 'password_input', 'confirm_password'],
            ['current_password', 'password_input', 'confirm_password', 'password_strength'],
        ]

        return config
