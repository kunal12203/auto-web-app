# 🚀 AI Website Builder

An interactive platform where you can build websites using natural language prompts. Type your idea, and watch as AI generates a complete website in real-time!

## ✨ Features

- **Real-time Generation**: See your website update instantly as you enter prompts
- **AI-Powered**: Uses OpenAI GPT-4 to generate modern, high-end HTML/CSS/JavaScript
- **Live Preview with Navigation**: Interactive preview with browser-like navigation controls
  - Back/Forward buttons for navigation history
  - Refresh button to reload the preview
  - URL bar showing current page/section
  - Full navigation support for generated websites
- **Device Preview Modes**: Test your website on different screen sizes
  - Desktop view (full width)
  - Tablet view (768px)
  - Mobile view (375px)
- **Modern UI/UX**: Premium interface with animations and transitions
  - Gradient backgrounds with animated effects
  - Glassmorphism design elements
  - Smooth hover interactions and micro-animations
  - Responsive design for all screen sizes
- **WebSocket Connection**: Real-time bidirectional communication for instant updates
- **Enhanced AI Prompts**: Optimized for generating modern framework-based websites
- **Example Prompts**: Quick-start templates showcasing advanced features

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

- "A modern landing page for a tech startup with hero section, features, pricing, and contact form with smooth scrolling navigation"
- "A portfolio website for a photographer with animated gallery grid, about section, and contact page using hash navigation"
- "A sleek SaaS product landing page with gradient backgrounds, feature cards, testimonials, and FAQ section"
- "An interactive restaurant website with menu navigation, image gallery, reservation form, and location map"
- "A personal blog homepage with article cards, categories navigation, search functionality, and newsletter signup"

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

## 🎨 New Features

### Navigation Controls
The live preview now includes browser-like navigation controls:
- **Back/Forward**: Navigate through the website's history
- **Refresh**: Reload the current preview
- **URL Display**: See the current page or section

### Device Preview Modes
Switch between different device sizes to test responsiveness:
- **Desktop**: Full-width view
- **Tablet**: 768px width for tablet testing
- **Mobile**: 375px width for mobile testing

### Modern Design
The interface features a premium, modern design:
- Animated gradient backgrounds
- Glassmorphism effects with backdrop blur
- Smooth transitions and micro-interactions
- Hover effects on all interactive elements
- Modern color palette with proper contrast

### Enhanced AI Generation
The AI now generates high-end, modern websites with:
- Modern CSS3 features (gradients, animations, flexbox, grid)
- Proper navigation implementation (hash-based routing)
- Responsive, mobile-first design
- Interactive elements with smooth transitions
- Professional aesthetics and visual hierarchy

## 📈 Future Enhancements

- Save/load projects
- Export generated code to files
- Real-time code editing
- User authentication
- Template library
- Version history with undo/redo
- Custom theme selection
- Collaboration features

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

MIT License - feel free to use this project for learning and development!

---

**Happy Building! 🎉**
