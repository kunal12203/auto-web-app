# Logging Guide - How to Track and Debug

## 📋 Quick Start

When you run the backend, you'll see detailed logs for every step:

```bash
cd backend
python main.py
```

## 🎯 What You'll See

### 1. **Startup Logs**

```
================================================================================
🚀 AI Website Builder Backend Starting...
================================================================================
✅ Claude API key loaded
✅ Anthropic client initialized
✅ Connection Manager initialized
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**What to check:**
- ✅ "Claude API key loaded" - API key found in .env
- ❌ If you see "ANTHROPIC_API_KEY not found" - check your .env file

---

### 2. **WebSocket Connection Logs**

```
🔌 WebSocket connected (Total: 1)
```

**What this means:**
- Frontend successfully connected to backend
- Number shows total active connections

**If connection fails:**
- Check if backend is running on port 8000
- Check CORS settings in main.py
- Check frontend is using correct WebSocket URL

---

### 3. **Project Generation Logs**

```
============================================================
📨 Received message: generate
============================================================
🎨 Generate request:
   Project Name: my-ecommerce
   Prompt: Create a modern ecommerce site with Stripe...

🔍 Analyzing requirements...
   Payment needed: True
❓ Asking user: I detected you need payment processing. Which gateway would you like?
   Options: ['stripe', 'paypal', 'razorpay', 'none']
⏳ Waiting for user response...
✅ User selected: stripe

📦 Project type detected: fullstack
============================================================
🏗️  Generating FULLSTACK project: my-ecommerce
   Payment Gateway: stripe
   Prompt: Create a modern ecommerce site with Stripe...
============================================================
🚀 Generating Full-Stack project...
   Base full-stack scaffolding created (8 files)
✅ Full-stack project enhanced (15 files)
🐳 Adding Docker configuration...
✅ Docker files added (3 files)
🎉 Project generation complete! Total files: 18

🧠 Creating project memory fingerprint...
   Project: my-ecommerce
   Type: fullstack
   Files: 18
   Detected tech stack: ['react', 'vite', 'fastapi', 'stripe', 'docker']
   Dependencies: 12 found
✅ Memory fingerprint created: a3f9d2e8b1c4
   Active sessions: 1

📤 Sending project to frontend (18 files)...
✅ Project sent successfully!
```

**What to track:**
- Project type detected correctly?
- Tech stack detection accurate?
- File count matches expectations?
- Session ID created (needed for memory)
- All steps completing successfully?

**Common errors to watch for:**
- ❌ "Error generating project" - Check Claude API key/quota
- ❌ "Template customization failed" - May fallback to from-scratch (uses more tokens)
- ⚠️  "Empty prompt received" - Frontend sent blank prompt

---

### 4. **File Update Logs**

```
============================================================
📨 Received message: update_file
============================================================
✏️  Update file request:
   File: frontend/src/App.jsx
   Session ID: a3f9d2e8b1c4
   Modification: Add dark mode toggle...

🧠 Retrieving memory context for update...
📝 Generating update context for: frontend/src/App.jsx
   Session ID: a3f9d2e8b1c4
   Found session: my-ecommerce (fullstack)
✅ Generated update context (847 chars, ~211 tokens)
   Context size: 847 chars
   Calling Claude API for file update (~300 tokens)...
   Received updated content (1523 chars)
✅ File updated with memory context (~300 tokens)

📤 Sending updated file to frontend...
✅ Update sent successfully!
```

**What to track:**
- Session ID found? (If not, using fallback - may hallucinate!)
- Token count reasonable (~300 tokens)
- Update completed successfully?

**Common errors:**
- ⚠️  "Session {id} not found! Using fallback context." - Frontend didn't send session ID
- ❌ "Error updating file" - Check Claude API error

---

### 5. **Console Error Fix Logs**

```
============================================================
📨 Received message: console_error
============================================================
🐛 Console error fix request:
   File: frontend/src/App.jsx
   Session ID: a3f9d2e8b1c4
   Error: Cannot read property 'map' of undefined

🧠 Retrieving memory context for error fix...
🔧 Generating error fix context for: frontend/src/App.jsx
   Session ID: a3f9d2e8b1c4
   Error: Cannot read property 'map' of undefined
   Found session: my-ecommerce (fullstack)
✅ Generated error fix context (623 chars, ~155 tokens)
   Context size: 623 chars
   Calling Claude API for error fix (~300 tokens)...
   Received fixed content (1489 chars)
✅ Console error fixed with memory context (~300 tokens)

📤 Sending fixed file to frontend...
✅ Fix sent successfully!
```

**What to track:**
- Error message captured correctly?
- Session found (prevents hallucination)?
- Fix completed successfully?

**Common errors:**
- ❌ "Error fixing console error" - Claude API issue or invalid error format

---

### 6. **Template Selection Logs** (Simple HTML projects)

```
🎨 Generating HTML with Claude...
   STEP 1: Trying template-based generation (~200 tokens)...

🎯 Auto-selecting best template...
   Available templates: ['modern-landing', 'portfolio', 'blog', 'ecommerce']
   Calling Claude API (~50 tokens)...
   Claude selected: modern-landing
✅ Template selected: modern-landing

✏️  Customizing template 'modern-landing' with AI...
   Found 12 variables: ['TITLE', 'HERO_TEXT', 'CTA_BUTTON', ...]
   Calling Claude API (~150 tokens)...
   Received response (856 chars)
   Parsing JSON response...
   Parsed 12 variables
   Filling in default values for missing variables...
   Replacing variables in template...
✅ Template customized successfully! (4523 chars)

✅ Template-based generation successful! (~200 tokens used)
```

**What to track:**
- Template selection appropriate for prompt?
- All variables filled?
- Total ~200 tokens (95% savings!)

**Fallback scenario:**
```
⚠️  Template customization failed, falling back to from-scratch generation...
   STEP 2: From-scratch generation (~4000 tokens)...
   Calling Claude API with from-scratch prompt...
   Received HTML (5234 chars)
✅ From-scratch generation complete (~4000 tokens used)
```

**If you see fallback:**
- Not a critical error, but uses more tokens
- Check Claude API response in debug logs

---

### 7. **Error Logs** (What to Watch For)

#### API Key Missing
```
❌ ANTHROPIC_API_KEY not found in environment variables!
ValueError: ANTHROPIC_API_KEY is required
```
**Fix:** Add ANTHROPIC_API_KEY to backend/.env

#### Claude API Error
```
❌ Error generating HTML: Error code: 401 - Invalid API key
```
**Fix:** Check API key is correct and has credits

#### WebSocket Disconnect
```
🔌 Client disconnected normally
🔌 WebSocket disconnected (Total: 0)
```
**Normal:** User closed browser or refreshed page

#### General WebSocket Error
```
❌ WebSocket error: 'NoneType' object has no attribute 'get'
Traceback (most recent call last):
  File "/path/to/main.py", line 623, in websocket_endpoint
    file_path = message.get("filePath")
AttributeError: 'NoneType' object has no attribute 'get'
```
**Fix:** Check frontend is sending correct message format

---

## 🔍 Debugging Tips

### 1. **Enable DEBUG level logging**

Edit `backend/main.py`:

```python
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
```

**You'll see MORE details:**
- Full Claude API prompts
- Response content lengths
- Context generation details
- Variable replacements
- JSON parsing steps

### 2. **Track Token Usage**

Look for lines like:
```
~50 tokens
~150 tokens
~200 tokens
~300 tokens
~4000 tokens
```

**Expected token usage:**
- Simple HTML (template): ~200 tokens
- Simple HTML (from-scratch): ~4,000 tokens
- React project: ~500 tokens
- Full-stack project: ~700 tokens
- File update (with memory): ~300 tokens
- Error fix (with memory): ~300 tokens

**If you see high numbers:**
- Fallback to from-scratch generation
- No memory session (hallucination risk!)

### 3. **Check Session IDs**

Every project should have:
```
✅ Project memory created: a3f9d2e8b1c4
```

Every update/fix should show:
```
   Session ID: a3f9d2e8b1c4
   Found session: my-ecommerce (fullstack)
```

**If you see:**
```
⚠️  Session a3f9d2e8b1c4 not found! Using fallback context.
```
**Problem:** Frontend not sending session ID or session expired

### 4. **Monitor Active Sessions**

```
   Active sessions: 3
```

Shows how many projects are in memory. Useful for:
- Tracking multiple concurrent users
- Memory usage estimation
- Session cleanup debugging

---

## 📊 Log Categories with Emojis

| Emoji | Meaning |
|-------|---------|
| 🚀 | Startup / Initialization |
| 🔌 | WebSocket connection |
| 📨 | Message received |
| 🎨 | HTML generation |
| 🏗️  | Project generation |
| 🧠 | Memory operations |
| 📝 | Update context |
| 🔧 | Error fix context |
| ✏️  | File update |
| 🐛 | Console error |
| 💳 | Payment gateway |
| 📦 | Project type detection |
| 🎯 | Template selection |
| 🐳 | Docker files |
| ⚛️  | React project |
| 📄 | Simple HTML |
| 🚀 | Full-stack project |
| ❓ | User question |
| 📤 | Sending to frontend |
| ✅ | Success |
| ❌ | Error |
| ⚠️  | Warning |

---

## 🎯 Common Scenarios

### **Scenario 1: First-time user generates project**

Expected log flow:
1. 🚀 Startup banner
2. 🔌 WebSocket connected
3. 📨 Received message: generate
4. 🔍 Analyzing requirements
5. 📦 Project type detected
6. 🏗️  Generating project
7. 🧠 Creating memory fingerprint
8. ✅ Project sent successfully

**No errors = Happy path! ✅**

---

### **Scenario 2: User updates file after generation**

Expected log flow:
1. 📨 Received message: update_file
2. ✏️  Update file request (shows session ID)
3. 🧠 Retrieving memory context
4. 📝 Generating update context (session found!)
5. ✅ File updated (~300 tokens)
6. ✅ Update sent successfully

**Key check: Session found? If not, may hallucinate!**

---

### **Scenario 3: Console error detected in preview**

Expected log flow:
1. 📨 Received message: console_error
2. 🐛 Console error fix request (shows error)
3. 🧠 Retrieving memory context
4. 🔧 Generating error fix context (session found!)
5. ✅ Console error fixed (~300 tokens)
6. ✅ Fix sent successfully

**Key check: Session found for accurate fix?**

---

## 💡 Pro Tips

1. **Save logs for debugging:**
   ```bash
   python main.py 2>&1 | tee backend.log
   ```

2. **Filter logs by type:**
   ```bash
   # Only errors
   python main.py 2>&1 | grep ERROR

   # Only memory operations
   python main.py 2>&1 | grep "🧠"

   # Only WebSocket messages
   python main.py 2>&1 | grep "📨"
   ```

3. **Watch token usage:**
   ```bash
   python main.py 2>&1 | grep "tokens"
   ```

4. **Monitor sessions:**
   ```bash
   python main.py 2>&1 | grep "session"
   ```

---

## 🚨 Critical Errors to Watch

### ❌ **API Key Issues**
```
❌ ANTHROPIC_API_KEY not found in environment variables!
```
**Fix:** Create `.env` file with `ANTHROPIC_API_KEY=sk-...`

### ❌ **Memory Session Not Found**
```
⚠️  Session a3f9d2e8b1c4 not found! Using fallback context.
```
**Impact:** Updates may hallucinate (create wrong files, switch frameworks)
**Fix:** Ensure frontend sends `sessionId` with all update/error requests

### ❌ **WebSocket Send Failed**
```
❌ Error sending message: Connection closed
```
**Impact:** Frontend won't receive response
**Fix:** Check WebSocket connection is stable

### ❌ **Project Generation Failed**
```
❌ Error generating project: API connection error
```
**Impact:** No project created
**Fix:** Check network, API key, Claude API status

---

## ✅ Summary

**Logging gives you:**
- 👀 Full visibility into every operation
- 🐛 Easy error debugging with stack traces
- 💰 Token usage tracking
- 🧠 Memory system verification
- 🔌 WebSocket health monitoring
- ⚡ Performance insights (file counts, sizes)

**Start backend and watch the magic! 🚀**
