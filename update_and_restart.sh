#!/bin/bash

echo "🔄 Updating Auto Web App to HIGH-QUALITY mode..."
echo "================================================"
echo ""

# Pull latest code
echo "📥 Pulling latest code from git..."
git pull origin claude/local-chat-storage-preview-01TpBp26gL2w7LWQbNawS8Zx

echo ""
echo "🔪 Killing old processes..."
pkill -9 -f uvicorn
pkill -9 -f vite
sleep 2

# Kill port 8000
if lsof -ti:8000 > /dev/null 2>&1; then
    echo "   Killing process on port 8000..."
    kill -9 $(lsof -ti:8000) 2>/dev/null
fi

sleep 1

echo ""
echo "✅ Ready to start!"
echo ""
echo "================================================"
echo "NOW RUN THESE IN SEPARATE TERMINALS:"
echo "================================================"
echo ""
echo "Terminal 1 - Backend:"
echo "  cd $(pwd)/backend"
echo "  uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
echo ""
echo "Terminal 2 - Frontend:"
echo "  cd $(pwd)/frontend"
echo "  npm run dev"
echo ""
echo "Then open: http://localhost:3000"
echo "================================================"
