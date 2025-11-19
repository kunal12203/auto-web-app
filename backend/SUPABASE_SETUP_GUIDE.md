# Supabase Setup Guide (5 minutes)

## Quick Answer
**No, Supabase is NOT automatically attached.** You need to create a free account and configure credentials.

---

## Step-by-Step Setup

### **Step 1: Create Supabase Account (2 minutes)**

1. Go to https://supabase.com
2. Click **"Start your project"**
3. Sign up with GitHub or email (100% FREE, no credit card)
4. Click **"New Project"**
5. Fill in:
   ```
   Name: my-websites
   Database Password: [Generate strong password - SAVE THIS!]
   Region: [Choose closest to you]
   ```
6. Click **"Create new project"**
7. Wait ~2 minutes while Supabase provisions your database

---

### **Step 2: Get Connection Details (1 minute)**

1. After project is ready, click **Settings** (⚙️ icon on left sidebar)
2. Click **Database** in settings menu
3. Scroll down to **"Connection string"** section
4. You'll see these details:
   ```
   Host:     db.xxxxxxxxxxxxx.supabase.co
   Port:     5432
   Database: postgres
   User:     postgres
   Password: [The password you created]
   ```
5. **Copy these values** - you'll need them in the next step

---

### **Step 3: Configure Environment Variables (2 minutes)**

1. Go to your project directory:
   ```bash
   cd /home/user/auto-web-app/backend
   ```

2. Copy the example file to create your `.env`:
   ```bash
   cp .env.example .env
   ```

3. Open `.env` in your editor:
   ```bash
   nano .env
   # or
   vim .env
   # or use your preferred editor
   ```

4. Fill in your Supabase credentials:
   ```bash
   # Anthropic API Key
   ANTHROPIC_API_KEY=your_api_key_here

   # Supabase Database Configuration
   SUPABASE_HOST=db.xxxxxxxxxxxxx.supabase.co    # ← Replace with YOUR host
   SUPABASE_PORT=5432                             # ← Keep as 5432
   SUPABASE_DB=postgres                           # ← Keep as postgres
   SUPABASE_USER=postgres                         # ← Keep as postgres
   SUPABASE_PASSWORD=your_actual_password_here    # ← Replace with YOUR password
   ```

5. Save and close the file

---

### **Step 4: Verify Connection (30 seconds)**

Run this test to verify Supabase is connected:

```bash
cd /home/user/auto-web-app/backend
python3 << 'EOF'
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if Supabase credentials are set
host = os.getenv('SUPABASE_HOST')
password = os.getenv('SUPABASE_PASSWORD')

if host and host != 'db.xxxxxxxxxxxxx.supabase.co':
    print("✅ Supabase HOST configured!")
else:
    print("❌ Supabase HOST not configured - still using default")

if password and password != 'your_supabase_password_here':
    print("✅ Supabase PASSWORD configured!")
else:
    print("❌ Supabase PASSWORD not configured - still using default")

if host and password:
    print("\n✅ Supabase is ready to use!")
    print(f"   Host: {host}")
else:
    print("\n❌ Please update your .env file with real Supabase credentials")
EOF
```

---

### **Step 5: Test Database Provisioning**

Once configured, test the system:

```bash
cd /home/user/auto-web-app/backend
python3 << 'EOF'
from database_provisioner import DatabaseProvisioner, ProvisioningStrategy

# Create provisioner
provisioner = DatabaseProvisioner(
    default_strategy=ProvisioningStrategy.TABLE_PREFIX
)

# Provision database for test website
config = provisioner.provision_database("test_website")

print("\n✅ DATABASE PROVISIONED!")
print(f"  Database: {config.database_name}")
print(f"  Table Prefix: {config.table_prefix}_")
print(f"  Connection: {config.connection_string[:50]}...")
print("\nTables will be named:")
print(f"  - {config.table_prefix}_users")
print(f"  - {config.table_prefix}_products")
print(f"  - {config.table_prefix}_orders")
EOF
```

---

## What You Get (Free Tier)

```
✅ 500MB PostgreSQL database
✅ Unlimited API requests
✅ Unlimited authentication users
✅ 2GB file storage
✅ Automatic backups
✅ SSL/TLS encryption
✅ No credit card required
✅ Never expires
```

---

## How It Works

Once configured, your system will:

1. **Automatically provision databases** for each new website
2. **Use TABLE_PREFIX strategy** - one database, multiple websites
3. **Create unique table prefixes** like:
   - `gym_abc123_users`
   - `jewelry_def456_products`
   - `portfolio_xyz789_orders`
4. **Generate SQL schemas** automatically
5. **Support 20-50 websites** in one free Supabase database

---

## Troubleshooting

### Issue: "Connection refused"
**Solution:** Check your firewall, or verify the host is correct

### Issue: "Authentication failed"
**Solution:** Double-check your password in Supabase dashboard

### Issue: "Database does not exist"
**Solution:** Use `postgres` as the database name (default)

### Issue: Environment variables not loading
**Solution:** Make sure you're running from `/home/user/auto-web-app/backend` directory

---

## Alternative: Use Local PostgreSQL (No Signup)

If you don't want to use Supabase yet, you can use local PostgreSQL:

```bash
# Install PostgreSQL locally
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# Update .env to use local
SUPABASE_HOST=localhost
SUPABASE_PORT=5432
SUPABASE_DB=websites_db
SUPABASE_USER=postgres
SUPABASE_PASSWORD=postgres
```

But **Supabase is recommended** because:
- Free forever
- No installation needed
- Accessible from anywhere
- Automatic backups
- Better for production

---

## Summary

**Current Status:** 🔴 Supabase NOT configured yet

**Next Steps:**
1. Create Supabase account (2 min)
2. Create `.env` file from `.env.example`
3. Add your Supabase credentials
4. Test with the verification script above

**After Setup:** 🟢 Can generate unlimited websites with free database!

---

## Quick Copy-Paste

Once you have your Supabase credentials, just run:

```bash
cd /home/user/auto-web-app/backend
cp .env.example .env
nano .env  # Edit and save your credentials
```

That's it! Your system will now provision databases automatically for every website you generate.
