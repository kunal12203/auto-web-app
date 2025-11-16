# 🚀 AI Website Builder

An interactive platform where you can build websites using natural language prompts. Type your idea, and watch as AI generates a complete website in real-time!

## ✨ Features

### Core Features
- **Real-time Generation**: See your website update instantly as you enter prompts
- **AI-Powered**: Uses OpenAI GPT-4 to generate modern, high-end, fully responsive HTML/CSS/JavaScript
- **Thread-Based Conversations**: Maintain context for each website project
  - Iterative improvements with conversation history
  - Modify existing websites with natural language
  - Session-based project management
- **Code Export**: Download generated HTML files locally
  - One-click export to save your work
  - Unique filename per session
  - Ready-to-deploy code

### Live Preview Features
- **Browser-Like Navigation Controls**:
  - Back/Forward buttons for navigation history
  - Refresh button to reload the preview
  - URL bar showing current page/section
  - Full navigation support for generated websites
- **Device Preview Modes**: Test responsive design on different screen sizes
  - Desktop view (full width)
  - Tablet view (768px)
  - Mobile view (375px)
  - Smooth transitions between modes

### Modern UI/UX
- **Premium Interface** with animations and transitions
  - Gradient backgrounds with animated effects
  - Glassmorphism design elements
  - Smooth hover interactions and micro-interactions
  - Responsive design for all screen sizes
- **WebSocket Connection**: Real-time bidirectional communication for instant updates

### Enhanced AI Generation
- **Critical Responsive Design**: Mobile-first approach with proper breakpoints
- **Modern CSS3**: Gradients, animations, transitions, flexbox, grid
- **Multi-Page Support**: Hash-based routing for complex websites
- **JavaScript Interactivity**: Scroll animations, form validation, components
- **Accessibility**: Semantic HTML, ARIA labels, keyboard navigation
- **Professional Typography**: Google Fonts integration, proper hierarchy

### Figma Integration
- **Multiple Integration Methods**: Design-to-prompt, API, plugins
- **Design Token Support**: Import colors, typography, spacing from Figma
- See `FIGMA_INTEGRATION_GUIDE.md` for detailed instructions

## 🏗️ Architecture

- **Frontend**: React + Vite
- **Backend**: FastAPI (Python)
- **Real-time**: WebSocket for live updates
- **AI**: OpenAI GPT-4 API

## 📋 Prerequisites

- Node.js (v18 or higher)
- Python 3.8+
- OpenAI API Key

## 🚀 Quick Start

### 1. Clone the Repository

```bash
cd auto-web-app
```

### 2. Set Up Backend

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=your_api_key_here
```

**Important**: Get your OpenAI API key from https://platform.openai.com/api-keys

### 3. Set Up Frontend

```bash
# Open a new terminal
cd frontend

# Install dependencies
npm install
```

### 4. Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python main.py
```

The backend will start on http://localhost:8000

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

The frontend will start on http://localhost:3000

### 5. Start Building!

1. Open your browser to http://localhost:3000
2. Wait for the "Ready to build!" status
3. Enter a prompt describing your website
4. Click "Generate Website" or press Enter
5. Watch your website appear in real-time!

## 📝 Example Prompts

### Initial Generation
- "A modern landing page for a tech startup with hero section, features, pricing, and contact form with smooth scrolling navigation"
- "A portfolio website for a photographer with animated gallery grid, about section, and contact page using hash navigation"
- "A sleek SaaS product landing page with gradient backgrounds, feature cards, testimonials, and FAQ section"
- "An interactive restaurant website with menu navigation, image gallery, reservation form, and location map"
- "A personal blog homepage with article cards, categories navigation, search functionality, and newsletter signup"

### Modification Prompts (After generating a website)
- "Change the color scheme to ocean blue (#0ea5e9 primary, #0284c7 secondary)"
- "Add a testimonials section with customer quotes and star ratings"
- "Make the navigation bar sticky and add a subtle shadow"
- "Replace the hero image with a gradient background"
- "Add smooth scroll animations that trigger when sections come into view"
- "Create a mobile hamburger menu with smooth animation"
- "Add a dark mode toggle button"

## 🎯 How It Works

1. **User Input**: You type a description of the website you want
2. **WebSocket Connection**: Your prompt is sent to the backend via WebSocket
3. **AI Generation**: FastAPI backend calls OpenAI GPT-4 to generate HTML/CSS/JS
4. **Real-time Update**: Generated code is sent back through WebSocket
5. **Live Preview**: React frontend renders the code in an iframe instantly

## 🛠️ Technology Stack

### Frontend
- **React 18**: UI library
- **Vite**: Fast build tool and dev server
- **WebSocket API**: Real-time communication
- **CSS3**: Modern styling with gradients and animations

### Backend
- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI server with WebSocket support
- **OpenAI API**: GPT-4 for code generation
- **Python-dotenv**: Environment variable management

## 📁 Project Structure

```
auto-web-app/
├── backend/
│   ├── main.py              # FastAPI application with WebSocket
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example        # Environment variables template
│   └── .env                # Your API keys (create this)
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── PromptInput.jsx    # Prompt input component
│   │   │   ├── PromptInput.css
│   │   │   ├── Preview.jsx        # Live preview component
│   │   │   ├── Preview.css
│   │   │   ├── StatusBar.jsx      # Connection status
│   │   │   └── StatusBar.css
│   │   ├── App.jsx          # Main application
│   │   ├── App.css
│   │   ├── main.jsx         # Entry point
│   │   └── index.css        # Global styles
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## 🔧 Configuration

### Backend (.env)
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Frontend
The frontend is configured to connect to `ws://localhost:8000/ws`. If you change the backend port, update the WebSocket URL in `frontend/src/App.jsx`.

## 🚨 Troubleshooting

### Connection Issues
- **"Disconnected. Retrying..."**: Make sure the backend is running on port 8000
- Check that both frontend and backend are running
- Verify your OpenAI API key is correctly set in `.env`

### API Errors
- **"Error Generating Website"**: Check your OpenAI API key and account credits
- Ensure you have access to GPT-4 model
- Check backend console for detailed error messages

### Port Conflicts
- Backend uses port 8000, Frontend uses port 3000
- If ports are in use, modify:
  - Backend: Change port in `backend/main.py`
  - Frontend: Change port in `frontend/vite.config.js`

## 💡 Tips

- Be specific in your prompts for better results
- Include details about colors, layout, and functionality
- Try the example prompts to see what's possible
- The AI works best with complete website descriptions

## 🔒 Security Notes

- Never commit your `.env` file with API keys
- The preview iframe has sandbox restrictions for security
- API keys should be kept secret and not shared

## 🎨 Key Features Explained

### Thread-Based Workflow
Create a website and iterate on it with conversation:
1. **Generate** initial website with a detailed prompt
2. **Modify** the website with natural language changes
   - "Change the color scheme to blue"
   - "Add a testimonials section"
   - "Make the header sticky"
3. **Track** iteration history (shows "Iteration #2", "#3", etc.)
4. **Export** your final code when ready
5. **Start New** to begin a fresh project

### Responsive Design Excellence
The AI generates websites with:
- **Mobile-first approach** with proper viewport settings
- **Responsive breakpoints**: < 640px (mobile), 640-1024px (tablet), > 1024px (desktop)
- **Flexible layouts** using CSS Grid and Flexbox
- **Touch-friendly elements** (minimum 44x44px tap targets)
- **Responsive images** with proper sizing
- **Readable typography** on all screens

### Multi-Page Navigation
Generated websites support multiple pages:
- **Hash-based routing** (#home, #about, #contact)
- **JavaScript router** to show/hide sections
- **Browser back/forward** support
- **Active state indicators** in navigation
- **Smooth page transitions**
- **Mobile hamburger menus**

### Code Export
Save your generated websites locally:
- Click **"Export Code"** button
- Downloads as `website-{sessionId}.html`
- Complete, self-contained HTML file
- Ready to deploy or further customize

### Figma Integration
Multiple ways to integrate with Figma designs:
1. **Design-to-Prompt**: Describe Figma design in prompt
2. **API Integration**: Automated design import (see guide)
3. **Plugin Method**: Direct export from Figma (advanced)
4. **Image-to-Code**: Vision AI analysis (future)

See **FIGMA_INTEGRATION_GUIDE.md** for complete instructions

## 🗂️ Project Structure

```
auto-web-app/
├── backend/
│   ├── main.py                    # FastAPI app with WebSocket & conversation support
│   ├── requirements.txt           # Python dependencies
│   ├── .env.example              # Environment variables template
│   └── .env                      # Your API keys (create this)
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── PromptInput.jsx   # Prompt input with modify mode
│   │   │   ├── PromptInput.css
│   │   │   ├── Preview.jsx       # Live preview with navigation
│   │   │   ├── Preview.css
│   │   │   ├── StatusBar.jsx     # Connection status
│   │   │   └── StatusBar.css
│   │   ├── App.jsx               # Main app with thread management
│   │   ├── App.css
│   │   ├── main.jsx
│   │   └── index.css
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── FIGMA_INTEGRATION_GUIDE.md    # Comprehensive Figma guide
└── README.md
```

## 📈 Future Enhancements

- ✅ Thread-based conversations (Completed)
- ✅ Code export functionality (Completed)
- ✅ Iterative modifications (Completed)
- ✅ Multi-page support (Completed)
- ✅ Figma integration guide (Completed)
- 🔄 Save/load projects to database
- 🔄 Real-time code editor with live updates
- 🔄 User authentication and project management
- 🔄 Template library with pre-built designs
- 🔄 Version history with undo/redo
- 🔄 Team collaboration features
- 🔄 Direct Figma API integration
- 🔄 AI-powered design suggestions

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

MIT License - feel free to use this project for learning and development!

---

**Happy Building! 🎉**
