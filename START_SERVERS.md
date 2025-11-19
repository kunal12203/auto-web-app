# How to Start the Application

## Prerequisites

1. **Install Dependencies**
   ```bash
   # Backend dependencies
   pip install -r backend/requirements.txt

   # Frontend dependencies
   cd frontend && npm install
   ```

2. **Set up API Key (Optional but recommended)**
   ```bash
   cd backend
   echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
   ```
   Get your API key from: https://console.anthropic.com/settings/keys

## Starting the Servers

### Option 1: Start Both Servers (Recommended)

Open **two separate terminal windows**:

**Terminal 1 - Backend:**
```bash
cd /home/user/auto-web-app/backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**Terminal 2 - Frontend:**
```bash
cd /home/user/auto-web-app/frontend
npm run dev
```

### Option 2: One-Line Background Start

```bash
# Start backend in background
cd /home/user/auto-web-app/backend && python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload > /tmp/backend.log 2>&1 &

# Start frontend (this will open in current terminal)
cd /home/user/auto-web-app/frontend && npm run dev
```

## Access the Application

Once both servers are running:

- **Frontend UI**: http://localhost:3000 (or the port shown by Vite)
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Features Available

✅ **Thread Management**: Click the hamburger menu (☰) to view/manage chat threads
✅ **Chat History**: All conversations are saved in browser localStorage
✅ **Create New Thread**: Click the "+ New" button in the sidebar
✅ **Live Preview**: See your generated website in real-time
✅ **Export**: Download your project as a ZIP file

## Troubleshooting

### Backend not connecting?
- Check if backend is running: `curl http://localhost:8000`
- Check backend logs: `tail -f /tmp/backend.log`
- Verify port 8000 is not in use: `lsof -i :8000` or `ss -tlnp | grep 8000`

### Frontend shows "Disconnected"?
- Ensure backend is running first
- Check browser console (F12) for WebSocket errors
- Verify WebSocket endpoint: ws://localhost:8000/ws

### No AI generation?
- You need to add ANTHROPIC_API_KEY to backend/.env
- Without it, the app will connect but won't generate websites
