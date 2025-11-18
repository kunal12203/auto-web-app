"""
AI Prompt System - Optimized for Template-Based Generation
Leverages 2,200+ templates (1,502 React, 665 Backend, 33 Database)
Supports multi-turn refinement with clear file structure output
"""

# ============================================================================
# MASTER PROJECT GENERATION PROMPT
# ============================================================================

MASTER_GENERATION_PROMPT = """You are an expert full-stack web developer with access to a massive template library of 2,200+ production-ready components.

🎯 YOUR TASK:
Analyze the user's request and create a COMPLETE file structure leveraging our template library.

📚 AVAILABLE TEMPLATES:
- 1,502 React Components: UI primitives, forms, layouts, data displays, animations, e-commerce, admin dashboards
- 665 Backend Templates: REST/GraphQL APIs, auth, databases, caching, messaging, real-time, microservices
- 33 Database Templates: Schemas, migrations, queries for PostgreSQL, MongoDB, MySQL

🔍 ANALYSIS STEPS:
1. Identify website/app type: {website_types}
2. Determine project type: simple HTML, React SPA, or full-stack
3. List all components needed: Header, Hero, Features, CTA, Form, etc.
4. Identify backend needs: Auth, API endpoints, database, real-time features
5. Map to existing templates where possible

📋 OUTPUT FORMAT:
Return a clear file structure in this EXACT format:

```json
{{
  "projectType": "react|fullstack|simple",
  "websiteType": "saas|ecommerce|portfolio|restaurant|fitness|business|general",
  "fileStructure": {{
    "frontend": {{
      "src/App.jsx": {{
        "template": "App skeleton with routing",
        "dependencies": ["Header", "Hero", "Features", "CTA", "Footer"]
      }},
      "src/components/Header.jsx": {{
        "template": "HeaderWithCTA|HeaderMinimal|HeaderEcommerce",
        "customize": {{"logo": "{{{{LOGO_TEXT}}}}", "primaryColor": "{{{{PRIMARY_COLOR}}}}"}}
      }},
      "src/components/Hero.jsx": {{
        "template": "HeroGradient|HeroImage|HeroVideo",
        "customize": {{"title": "{{{{HERO_TITLE}}}}", "subtitle": "{{{{HERO_SUBTITLE}}}}"}}
      }}
    }},
    "backend": {{
      "server.js": {{
        "template": "Express server with middleware",
        "features": ["cors", "helmet", "rate-limiting"]
      }},
      "routes/auth.js": {{
        "template": "JWT authentication with refresh tokens",
        "database": "users table required"
      }},
      "routes/api.js": {{
        "template": "RESTful API with validation",
        "endpoints": ["/users", "/products", "/orders"]
      }}
    }},
    "database": {{
      "schema.sql": {{
        "template": "PostgreSQL schema",
        "tables": ["users", "products", "orders"]
      }}
    }}
  }},
  "placeholders": {{
    "LOGO_TEXT": "extracted from user prompt or default",
    "PRIMARY_COLOR": "extracted from user prompt or #3B82F6",
    "SECONDARY_COLOR": "extracted from user prompt or #8B5CF6",
    "HERO_TITLE": "extracted from user prompt",
    "HERO_SUBTITLE": "extracted from user prompt"
  }},
  "customComponents": [
    {{
      "name": "CustomPricingTable",
      "reason": "User requested unique 3-tier pricing with toggle",
      "requirements": ["Monthly/Annual toggle", "3 tiers", "Feature comparison"]
    }}
  ]
}}
```

⚡ TEMPLATE MATCHING RULES:
- Use existing templates whenever 70%+ match
- Generate custom components only for unique requirements
- Prefer composition: combine simple templates vs generating complex ones
- Default to modern, responsive, accessible patterns

🎨 CUSTOMIZATION:
- Extract brand colors, fonts, text from user prompt
- Use placeholders: {{{{VARIABLE}}}} for AI customization
- Provide sensible defaults for missing info

✅ REQUIREMENTS:
- COMPLETE file structure (don't omit files)
- Specific template names from our library
- Clear justification for custom components
- All imports/dependencies listed
- Database schemas if backend needed

User Request: {user_prompt}

Return ONLY the JSON structure above. No explanations, no markdown.
"""

# ============================================================================
# MULTI-TURN UPDATE PROMPT
# ============================================================================

MULTI_TURN_UPDATE_PROMPT = """You are updating an existing project. The user wants to modify: {modification_request}

📁 CURRENT PROJECT CONTEXT:
Project Type: {project_type}
Session ID: {session_id}
Files Count: {file_count}

🎯 YOUR TASK:
1. Identify which files need modification
2. Determine if new files are needed
3. Leverage existing templates for new components
4. Maintain consistency with existing code style

📋 OUTPUT FORMAT:
```json
{{
  "modificationType": "update|add|delete|refactor",
  "filesToModify": [
    {{
      "path": "src/components/Header.jsx",
      "changes": "Add mobile menu toggle, update navigation items",
      "template": "use existing or HeaderWithMobileMenu"
    }}
  ],
  "filesToAdd": [
    {{
      "path": "src/components/MobileMenu.jsx",
      "template": "MobileMenuSlideOut",
      "reason": "User requested mobile navigation"
    }}
  ],
  "filesToDelete": [
    "src/components/OldComponent.jsx"
  ],
  "dependencies": {{
    "add": ["framer-motion"],
    "remove": []
  }}
}}
```

🔍 PROJECT MEMORY:
{project_memory}

✅ REQUIREMENTS:
- Minimal changes (don't recreate entire files)
- Use templates for new components
- Maintain existing patterns
- Update imports/dependencies as needed

Return ONLY the JSON structure. No explanations.
"""

# ============================================================================
# COMPONENT GENERATION PROMPT
# ============================================================================

COMPONENT_GENERATION_PROMPT = """Generate COMPLETE React component: {component_name}

📋 CONTEXT:
User Request: {user_prompt}
Website Type: {website_type}
Component Purpose: {component_purpose}

✅ REQUIREMENTS:
- Functional component with hooks (useState, useEffect as needed)
- Responsive design (mobile-first, Tailwind or CSS-in-JS)
- Modern styling with className
- MUST BE COMPLETE - no truncation, no cutoffs, no placeholders
- Include ALL necessary imports (React, icons, etc.)
- Props with TypeScript-style JSDoc comments
- Export default

🎨 STYLE GUIDE:
- Primary Color: {primary_color}
- Secondary Color: {secondary_color}
- Design System: Modern, clean, accessible
- Animations: Subtle, smooth (use CSS transitions)

📦 PATTERNS TO FOLLOW:
{code_patterns}

Return COMPLETE {component_name}.jsx code ONLY. No markdown, no explanations.
{retry_note}
"""

# ============================================================================
# BACKEND TEMPLATE SELECTION PROMPT
# ============================================================================

BACKEND_TEMPLATE_SELECTION_PROMPT = """Select BEST backend template for: {requirement}

📚 AVAILABLE CATEGORIES (665 templates):
REST APIs: rest-advanced, graphql-advanced, microservices (65 templates)
Authentication: auth-advanced, authorization, security-advanced, encryption, audit (100 templates)
Database: orm, query-optimization, replication, sharding, migrations-advanced (80 templates)
Caching: cache-patterns, distributed-cache, cache-invalidation (50 templates)
Messaging: message-queues, event-sourcing, pubsub, cqrs (60 templates)
Processing: image-processing, video-processing, document-processing (40 templates)
Search: search-engine, faceted-search, autosuggest (42 templates)
Real-time: websockets, sse, realtime-sync, streaming (68 templates)
And 160 more...

🔍 ANALYSIS:
Requirement Type: {requirement_type}
Complexity: {complexity}
Scale Needs: {scale_needs}

Return ONLY the template path: "category/TemplateName"
Example: "auth-advanced/JWT-Refresh-Token-Auth"
"""

# ============================================================================
# FILE STRUCTURE EXTRACTION PROMPT
# ============================================================================

FILE_STRUCTURE_EXTRACTION_PROMPT = """Extract clear file structure from this project request:

"{user_prompt}"

🎯 IDENTIFY:
1. Frontend files needed (HTML, React components, CSS)
2. Backend files needed (API routes, middleware, services)
3. Database files needed (schemas, migrations, seeds)
4. Config files needed (package.json, .env, vite.config)
5. Assets needed (images, fonts, icons)

📋 OUTPUT FORMAT:
```
📁 project-root/
├── 📁 frontend/
│   ├── 📁 src/
│   │   ├── App.jsx (Main app with routing)
│   │   ├── 📁 components/
│   │   │   ├── Header.jsx (Navigation with logo)
│   │   │   ├── Hero.jsx (Hero section with CTA)
│   │   │   └── Features.jsx (Feature grid)
│   │   ├── 📁 pages/
│   │   │   ├── Home.jsx
│   │   │   └── About.jsx
│   │   └── App.css (Global styles)
│   ├── package.json
│   └── vite.config.js
├── 📁 backend/
│   ├── server.js (Express server setup)
│   ├── 📁 routes/
│   │   ├── auth.js (Login, register, logout)
│   │   └── api.js (CRUD endpoints)
│   ├── 📁 middleware/
│   │   ├── auth.js (JWT verification)
│   │   └── validation.js (Request validation)
│   └── package.json
├── 📁 database/
│   ├── schema.sql (Database tables)
│   └── seed.sql (Sample data)
└── .env.example (Environment variables)
```

Return ONLY the tree structure with brief descriptions. Be specific and complete.
"""

# ============================================================================
# TEMPLATE CUSTOMIZATION PROMPT
# ============================================================================

TEMPLATE_CUSTOMIZATION_PROMPT = """Customize template: {template_name}

📋 USER REQUEST: {user_prompt}

🎨 PLACEHOLDERS TO FILL:
{placeholders}

✅ CUSTOMIZATION RULES:
- Extract text/colors/styles from user prompt
- Use sensible defaults for missing values
- Maintain template structure
- Keep responsive design
- Preserve accessibility features

📦 OUTPUT:
Return ONLY valid JSON with placeholder values:
```json
{{
  "LOGO_TEXT": "value from prompt or 'MyBrand'",
  "PRIMARY_COLOR": "value from prompt or '#3B82F6'",
  "HERO_TITLE": "value from prompt or default",
  ...
}}
```

Extract values intelligently. Return ONLY JSON.
"""

# ============================================================================
# ERROR FIX PROMPT
# ============================================================================

ERROR_FIX_PROMPT = """Fix error in: {file_path}

❌ ERROR:
{error_message}

📋 CURRENT CODE (first 1500 chars):
{code_preview}

🎯 FIX REQUIREMENTS:
- Identify root cause
- Fix the specific error
- Don't change unrelated code
- Maintain code style
- Keep all functionality

Return CORRECTED complete file content. No markdown, no explanations.
"""

# ============================================================================
# WEBSITE TYPE PATTERNS
# ============================================================================

WEBSITE_TYPES = [
    "saas",
    "ecommerce",
    "portfolio",
    "restaurant",
    "fitness",
    "business",
    "blog",
    "landing-page",
    "dashboard",
    "general"
]

# ============================================================================
# CODE PATTERNS FOR CONSISTENCY
# ============================================================================

CODE_PATTERNS = {
    "react_component": """
import { useState, useEffect } from 'react'

export default function ComponentName({ prop1, prop2, ...props }) {
  const [state, setState] = useState(null)

  useEffect(() => {
    // Side effects
  }, [dependencies])

  return (
    <div className="component-name" {...props}>
      {/* Content */}
    </div>
  )
}
""",
    "api_route": """
import express from 'express'
const router = express.Router()

router.get('/endpoint', async (req, res, next) => {
  try {
    const result = await service.method(req.query)
    res.json({ success: true, data: result })
  } catch (error) {
    next(error)
  }
})

export default router
""",
    "database_schema": """
CREATE TABLE table_name (
  id SERIAL PRIMARY KEY,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_table_field ON table_name(field);
"""
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def format_master_prompt(user_prompt: str) -> str:
    """Format the master generation prompt with user input"""
    return MASTER_GENERATION_PROMPT.format(
        website_types=", ".join(WEBSITE_TYPES),
        user_prompt=user_prompt
    )

def format_update_prompt(
    modification_request: str,
    project_type: str,
    session_id: str,
    file_count: int,
    project_memory: str
) -> str:
    """Format the multi-turn update prompt"""
    return MULTI_TURN_UPDATE_PROMPT.format(
        modification_request=modification_request,
        project_type=project_type,
        session_id=session_id,
        file_count=file_count,
        project_memory=project_memory
    )

def format_component_prompt(
    component_name: str,
    user_prompt: str,
    website_type: str,
    component_purpose: str = "",
    primary_color: str = "#3B82F6",
    secondary_color: str = "#8B5CF6",
    retry_note: str = ""
) -> str:
    """Format component generation prompt"""
    return COMPONENT_GENERATION_PROMPT.format(
        component_name=component_name,
        user_prompt=user_prompt,
        website_type=website_type,
        component_purpose=component_purpose or f"Component for {component_name}",
        primary_color=primary_color,
        secondary_color=secondary_color,
        code_patterns=CODE_PATTERNS["react_component"],
        retry_note=retry_note
    )

def format_backend_selection_prompt(
    requirement: str,
    requirement_type: str = "api",
    complexity: str = "medium",
    scale_needs: str = "small-medium"
) -> str:
    """Format backend template selection prompt"""
    return BACKEND_TEMPLATE_SELECTION_PROMPT.format(
        requirement=requirement,
        requirement_type=requirement_type,
        complexity=complexity,
        scale_needs=scale_needs
    )

def format_file_structure_prompt(user_prompt: str) -> str:
    """Format file structure extraction prompt"""
    return FILE_STRUCTURE_EXTRACTION_PROMPT.format(
        user_prompt=user_prompt
    )

def format_customization_prompt(
    template_name: str,
    user_prompt: str,
    placeholders: dict
) -> str:
    """Format template customization prompt"""
    placeholders_str = "\n".join([f"- {{{{{key}}}}}: {desc}" for key, desc in placeholders.items()])
    return TEMPLATE_CUSTOMIZATION_PROMPT.format(
        template_name=template_name,
        user_prompt=user_prompt,
        placeholders=placeholders_str
    )

def format_error_fix_prompt(
    file_path: str,
    error_message: str,
    code_preview: str
) -> str:
    """Format error fix prompt"""
    return ERROR_FIX_PROMPT.format(
        file_path=file_path,
        error_message=error_message,
        code_preview=code_preview[:1500]
    )
