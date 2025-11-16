# 🚀 AI Website Builder V2

**Build production-ready websites in seconds with AI!**

Transform natural language prompts into complete, deployable projects with Docker configurations, payment integrations, and beautiful responsive designs.

## ✨ Key Features

- 🎨 **Beautiful Modern UI** - Animated gradients, smooth transitions, responsive design
- 🏗️ **3 Project Types** - Simple HTML, React+Vite, Full-Stack
- 💳 **Payment Integration** - Stripe, PayPal, Razorpay auto-configured
- 🐳 **Docker Ready** - Complete containerization for all projects
- 🔧 **AI Error Fixing** - Console errors fixed automatically
- 📦 **ZIP Export** - Download complete projects with all files
- 🌳 **File Browser** - Explore generated project structure
- 📱 **Live Preview** - See your site in desktop/tablet/mobile views

## 🚦 Quick Start

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
echo "ANTHROPIC_API_KEY=your_key" > .env
python main.py
```

### Frontend Setup  
```bash
cd frontend
npm install
npm run dev
```

Visit: http://localhost:3000

## 📖 Usage Examples

**Simple Landing Page:**
```
Create a modern landing page for a tech startup with hero section,
features, pricing, and contact form
```

**React E-commerce:**
```
Build an e-commerce product page with React, image gallery,
add to cart, and Stripe checkout
```

**Full-Stack SaaS:**
```
Create a SaaS dashboard with user auth, subscription management,
and Stripe billing integration
```

## 🏗️ Generated Projects

### Simple HTML
- index.html, styles.css, script.js
- Dockerfile + nginx config
- README with deployment steps

### React + Vite
- Complete React scaffolding
- Vite for fast builds
- Multi-stage Docker build
- Production optimized

### Full-Stack
- React frontend
- FastAPI backend
- Payment gateway integration
- docker-compose orchestration
- PostgreSQL ready

## 🎯 Features

✅ Auto-template selection based on prompt  
✅ AI generates production-ready code  
✅ Console error detection & auto-fix  
✅ Payment gateway auto-detection  
✅ Beautiful building animations  
✅ File tree browser (VS Code style)  
✅ Live preview with device modes  
✅ ZIP export with Docker files  
✅ Responsive design  
✅ Modern, catchy UI  

## 🐛 Troubleshooting

**Backend won't start:**
- Check Python 3.9+ installed
- Verify ANTHROPIC_API_KEY in .env
- Run `pip install -r requirements.txt`

**Frontend errors:**
- Ensure backend running on port 8000
- Check WebSocket connection
- Run `npm install`

## 📚 Documentation

See `IMPLEMENTATION_STATUS.md` for complete architecture details.

## 🚀 Built With

- **Claude 4.5 Sonnet** - AI code generation
- **React + Vite** - Frontend framework
- **FastAPI** - Backend API
- **Docker** - Containerization
- **JSZip** - Project export

---

**Made with ❤️ using AI**  
Transform ideas into code in seconds! 🎉
