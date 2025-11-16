# 🎨 Figma Integration Guide

This guide explains different approaches to integrate Figma with the AI Website Builder for enhanced design workflows.

## Overview

Figma integration can significantly improve the quality and accuracy of generated websites by providing visual design references to the AI. There are several approaches depending on your needs.

---

## Approach 1: Design-to-Prompt Method (Easiest - No Code)

**Best for:** Quick prototyping, inspiration-based generation

### Steps:
1. **Create your design in Figma**
   - Design your website mockup in Figma
   - Use modern UI patterns, proper spacing, color schemes

2. **Export design as images**
   - Select frames/sections
   - Export as PNG (2x or 3x for quality)
   - File → Export → PNG

3. **Describe the design in your prompt**
   - Reference colors: "Use color scheme: #667eea (primary), #764ba2 (secondary)"
   - Describe layout: "Three-column grid with card components"
   - Mention specific elements: "Glassmorphic header with backdrop blur"

### Example Prompt:
```
Create a landing page based on this design:
- Header: Glassmorphic nav bar with logo left, menu right (Home, Features, Pricing, Contact)
- Hero: Full-width section with gradient background (#667eea to #764ba2), centered heading and CTA button
- Features: Three-column grid with icon cards, each with icon, title, description
- Footer: Dark background (#1a1a1a) with social links
- Colors: Primary #667eea, Secondary #764ba2, Text #333, Light #f5f5f5
- Typography: Inter for headings, System UI for body
- Spacing: 64px section padding, 24px card padding
```

---

## Approach 2: Figma API Integration (Moderate - Requires Backend)

**Best for:** Automated design import, team workflows

### Implementation:

#### 1. Get Figma API Token
```bash
# Go to Figma → Account Settings → Personal Access Tokens
# Generate new token and save it securely
```

#### 2. Add Figma API to Backend

**Install dependencies:**
```bash
cd backend
pip install requests
```

**Add to `backend/main.py`:**
```python
import requests

FIGMA_API_TOKEN = os.getenv("FIGMA_API_TOKEN")

def fetch_figma_design(file_key: str, node_ids: list = None):
    """Fetch design data from Figma API"""
    headers = {"X-Figma-Token": FIGMA_API_TOKEN}
    url = f"https://api.figma.com/v1/files/{file_key}"

    if node_ids:
        url += f"?ids={','.join(node_ids)}"

    response = requests.get(url, headers=headers)
    return response.json()

def figma_to_prompt(figma_data: dict) -> str:
    """Convert Figma design data to detailed prompt"""
    prompt_parts = []

    # Extract colors
    if 'styles' in figma_data:
        colors = extract_colors(figma_data['styles'])
        prompt_parts.append(f"Colors: {colors}")

    # Extract layout structure
    if 'document' in figma_data:
        layout = analyze_layout(figma_data['document'])
        prompt_parts.append(f"Layout: {layout}")

    # Extract typography
    text_styles = extract_typography(figma_data)
    prompt_parts.append(f"Typography: {text_styles}")

    return "\n".join(prompt_parts)

@app.post("/generate-from-figma")
async def generate_from_figma(file_key: str, node_ids: list = None):
    """Generate website from Figma design"""
    figma_data = fetch_figma_design(file_key, node_ids)
    design_prompt = figma_to_prompt(figma_data)
    html_code = generate_website_code(design_prompt)
    return {"html": html_code}
```

#### 3. Update Frontend to Support Figma URLs

**Add to `PromptInput.jsx`:**
```jsx
const [figmaUrl, setFigmaUrl] = useState('')

const handleFigmaImport = async () => {
  // Extract file key from Figma URL
  // Format: https://www.figma.com/file/{file_key}/...
  const match = figmaUrl.match(/figma\.com\/file\/([^\/]+)/)
  if (!match) {
    alert('Invalid Figma URL')
    return
  }

  const fileKey = match[1]
  // Call backend endpoint
  const response = await fetch('/generate-from-figma', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ file_key: fileKey })
  })

  const data = await response.json()
  onGenerate(data.html)
}

// Add UI input for Figma URL
<input
  type="text"
  placeholder="Paste Figma file URL..."
  value={figmaUrl}
  onChange={(e) => setFigmaUrl(e.target.value)}
/>
<button onClick={handleFigmaImport}>Import from Figma</button>
```

#### 4. Environment Setup

Add to `backend/.env`:
```env
FIGMA_API_TOKEN=your_figma_token_here
```

---

## Approach 3: Figma Plugin (Advanced - Best Integration)

**Best for:** Seamless workflow, direct export to builder

### Create Figma Plugin:

#### 1. Plugin Structure
```
figma-to-website-builder/
├── manifest.json
├── code.ts
└── ui.html
```

#### 2. `manifest.json`
```json
{
  "name": "AI Website Builder Export",
  "id": "website-builder-export",
  "api": "1.0.0",
  "main": "code.js",
  "ui": "ui.html",
  "capabilities": ["export"],
  "permissions": ["currentpage"]
}
```

#### 3. `code.ts`
```typescript
figma.showUI(__html__, { width: 400, height: 500 });

figma.ui.onmessage = async (msg) => {
  if (msg.type === 'export-design') {
    const selection = figma.currentPage.selection;

    if (selection.length === 0) {
      figma.ui.postMessage({
        type: 'error',
        message: 'Please select frames to export'
      });
      return;
    }

    // Extract design tokens
    const designData = {
      colors: extractColors(selection),
      typography: extractTypography(selection),
      spacing: extractSpacing(selection),
      layout: extractLayout(selection),
      components: extractComponents(selection)
    };

    // Send to your website builder
    figma.ui.postMessage({
      type: 'design-data',
      data: designData
    });
  }
};

function extractColors(nodes) {
  const colors = new Set();
  nodes.forEach(node => {
    if ('fills' in node && Array.isArray(node.fills)) {
      node.fills.forEach(fill => {
        if (fill.type === 'SOLID') {
          colors.add(rgbToHex(fill.color));
        }
      });
    }
  });
  return Array.from(colors);
}

function extractTypography(nodes) {
  const textStyles = [];
  nodes.forEach(node => {
    if (node.type === 'TEXT') {
      textStyles.push({
        fontFamily: node.fontName.family,
        fontSize: node.fontSize,
        fontWeight: node.fontName.style,
        lineHeight: node.lineHeight,
        letterSpacing: node.letterSpacing
      });
    }
  });
  return textStyles;
}

// ... implement other extraction functions
```

#### 4. `ui.html`
```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: Inter, sans-serif; padding: 20px; }
    button { padding: 10px 20px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer; }
    button:hover { background: #5568d3; }
  </style>
</head>
<body>
  <h2>Export to Website Builder</h2>
  <p>Select frames and click export</p>
  <button id="export">Export Design</button>
  <div id="status"></div>

  <script>
    document.getElementById('export').onclick = () => {
      parent.postMessage({ pluginMessage: { type: 'export-design' } }, '*');
    };

    window.onmessage = (event) => {
      const msg = event.data.pluginMessage;
      if (msg.type === 'design-data') {
        // Send to your website builder API
        fetch('http://localhost:8000/import-figma-design', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(msg.data)
        }).then(() => {
          document.getElementById('status').textContent = 'Design exported successfully!';
        });
      }
    };
  </script>
</body>
</html>
```

---

## Approach 4: Image-to-Code AI (Future Enhancement)

**Best for:** Maximum automation, visual-first workflow

### Concept:
Use AI vision models (like GPT-4 Vision) to analyze Figma screenshots and generate code.

### Implementation Outline:

```python
import base64
from openai import OpenAI

def image_to_website(image_path: str) -> str:
    """Generate website from Figma screenshot using GPT-4 Vision"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Read and encode image
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Analyze this Figma design and generate a complete, responsive HTML/CSS/JS website that matches it exactly. Include all colors, typography, spacing, and layout."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=4000
    )

    return response.choices[0].message.content
```

---

## Recommended Workflow

### For Quick Projects:
1. Design in Figma
2. Note down colors, fonts, spacing
3. Use **Approach 1** (Design-to-Prompt)

### For Team/Production:
1. Design in Figma
2. Set up **Approach 2** (Figma API)
3. Automate with design tokens
4. Iterate with modification prompts

### For Agency/Scale:
1. Build **Approach 3** (Figma Plugin)
2. Integrate with your builder
3. One-click export from Figma

---

## Design Tokens Export

### Recommended Figma Plugins:
- **Design Tokens**: Export colors, typography, spacing
- **Style Dictionary**: Convert tokens to CSS variables
- **Figma to Code**: Generate base HTML/CSS

### Manual Token Export:
```css
/* Export from Figma and use in prompts */
:root {
  /* Colors */
  --primary: #667eea;
  --secondary: #764ba2;
  --text-primary: #1a1a1a;
  --text-secondary: #666666;
  --background: #ffffff;

  /* Typography */
  --font-heading: 'Inter', sans-serif;
  --font-body: system-ui, sans-serif;
  --font-size-base: 16px;

  /* Spacing */
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  --spacing-md: 24px;
  --spacing-lg: 32px;
  --spacing-xl: 64px;

  /* Borders */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
}
```

---

## Tips for Best Results

1. **Use Figma Auto Layout**: Helps AI understand structure
2. **Consistent Naming**: Name layers descriptively (hero-section, nav-bar, etc.)
3. **Style System**: Use Figma styles for colors and typography
4. **Components**: Create reusable components
5. **Responsive Frames**: Design for mobile, tablet, desktop
6. **Export Guidelines**: Include spacing/padding annotations
7. **Design System**: Maintain a shared library

---

## Common Issues & Solutions

### Issue: Colors don't match exactly
**Solution**: Extract exact hex codes from Figma and include in prompt

### Issue: Layout not responsive
**Solution**: Specify breakpoints and behavior in prompt

### Issue: Fonts not loading
**Solution**: Use Google Fonts or system fonts, specify in prompt

### Issue: Spacing inconsistent
**Solution**: Define spacing system (8px grid) in prompt

---

## Next Steps

1. Choose approach based on your needs
2. Start with Approach 1 for immediate results
3. Implement Approach 2/3 for production
4. Consider Approach 4 for future enhancement

For questions or issues, refer to the main README.md
