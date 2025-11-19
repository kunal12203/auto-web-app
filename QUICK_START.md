# 🚀 Quick Start Guide

## Current Status
✅ **Backend is running** on http://localhost:8000
✅ **Frontend needs to be started**
⚠️ **API key required** for AI generation

## Start the Frontend (Required)

```bash
cd /home/user/auto-web-app/frontend
npm run dev
```

Then open: **http://localhost:3000**

## What You'll See

1. **Header** with:
   - ☰ Menu button (opens thread history sidebar)
   - ✨ Aether Builder logo
   - 👁️ Preview button (appears after generating a project)
   - Status badge (shows connection status)

2. **Chat Interface**:
   - Type your website description
   - Click "Send" or press Enter
   - Watch the AI build your project

3. **Thread Management**:
   - Click ☰ to see all your previous chats
   - Click "+ New" to start a fresh conversation
   - Click any thread to load that project
   - Click × to delete old threads

4. **Preview Panel**:
   - Automatically shows after project generation
   - Toggle visibility with 👁️ Preview button
   - View live preview or browse files
   - Export your project as ZIP

## Connection Status

- **🟢 System Online** - Ready to use
- **🟡 Reconnecting...** - Temporary connection issue (will auto-retry)
- **🔴 Connection Failed** - Backend not running or max retries reached

## Add AI Generation (Optional)

To enable actual website generation:

```bash
cd /home/user/auto-web-app/backend
echo "ANTHROPIC_API_KEY=sk-ant-xxxxx" > .env
# Replace sk-ant-xxxxx with your real key from https://console.anthropic.com
```

Then restart the backend:
```bash
pkill -f uvicorn
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Recent Fixes Applied ✅

1. **Fixed import error** - chatStorage module now correctly imported
2. **Fixed WebSocket spam** - Limited to 5 reconnection attempts with exponential backoff
3. **Added Preview toggle** - Easy show/hide button in header
4. **Switched to ChatApp** - Full thread management with sidebar
5. **Better error messages** - Clear connection status feedback

## Troubleshooting

**"WebSocket connection failed" spam?**
- Refresh the page (F5) - reconnections are now limited to 5 attempts
- Backend is running on http://localhost:8000

**Preview not visible?**
- Click the 👁️ Preview button in the header (only appears after generating a project)
- Or click "Open Preview" in the chat message after generation

**Generate button does nothing?**
- Check if "System Online" shows in header
- Open browser console (F12) for connection logs
- Backend must be running first

**Need to restart everything?**
```bash
# Kill all processes
pkill -f uvicorn
pkill -f vite

# Start backend
cd /home/user/auto-web-app/backend && python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload &

# Start frontend
cd /home/user/auto-web-app/frontend && npm run dev
```
