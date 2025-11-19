## Database Provisioning System

### **Problem Solved**

**BEFORE:** Manual database setup for each website
- ❌ Create database manually → Time consuming
- ❌ Configure credentials → Error prone
- ❌ Hit free tier limits → Can't scale
- ❌ No systematic approach → Inconsistent

**AFTER:** Automated database provisioning
- ✅ Automatic database setup
- ✅ Smart strategy selection
- ✅ Free tier optimization
- ✅ 20-50 websites in one free database
- ✅ Automatic schema generation

---

## 🎯 What It Does

The Database Provisioning System automatically handles database setup for generated websites:

1. **Recommends best strategy** based on your constraints (free tier, number of sites, isolation needs)
2. **Provisions databases** with appropriate configuration
3. **Generates SQL schemas** tailored to each strategy
4. **Manages credentials** via environment variables
5. **Optimizes for free tier** to minimize costs

---

## 📊 Provisioning Strategies

### **1. TABLE_PREFIX (Recommended for Free Tier)**

**How it works:**
- ONE database shared by multiple websites
- Each website gets UNIQUE table prefix
- Example:
  ```
  gym_abc123_users
  gym_abc123_products
  gym_abc123_orders

  jewelry_def456_users
  jewelry_def456_products
  jewelry_def456_orders
  ```

**Advantages:**
- ✅ Works perfectly with free tier (500MB Supabase)
- ✅ Can handle 20-50 websites in one database
- ✅ Good isolation (separate tables per site)
- ✅ Easy to backup/restore individual sites
- ✅ Simple migration path to separate databases later

**Best for:**
- Development and testing
- Free tier usage
- 10-100 websites
- **YOUR CURRENT USE CASE** ⭐

---

### **2. SEPARATE_DATABASE**

**How it works:**
- ONE database PER website
- Example:
  ```
  gym_website_db (has users, products, orders)
  jewelry_store_db (has users, products, orders)
  portfolio_site_db (has users, products, orders)
  ```

**Advantages:**
- ✅ Best isolation
- ✅ Independent scaling
- ✅ Easier per-site backups
- ✅ Production-grade

**Disadvantages:**
- ❌ May hit free tier limits (Supabase free = 2 projects max)
- ❌ More complex credential management
- ❌ Higher costs at scale

**Best for:**
- Production deployments
- Paying customers
- High-isolation requirements

---

### **3. MULTI_TENANT**

**How it works:**
- ONE database with SHARED tables
- Every table has `tenant_id` column
- Example:
  ```sql
  -- users table (shared by all sites)
  id | tenant_id        | email
  1  | gym_abc123      | user@gym.com
  2  | jewelry_def456  | user@jewelry.com

  -- products table (shared by all sites)
  id | tenant_id        | name
  1  | gym_abc123      | Protein Powder
  2  | jewelry_def456  | Gold Ring
  ```

**Advantages:**
- ✅ Most efficient resource usage
- ✅ Can handle 100+ websites easily
- ✅ Standard SaaS pattern
- ✅ Simplest to manage

**Disadvantages:**
- ❌ Requires careful row-level security
- ❌ All sites affected if DB goes down
- ❌ More complex queries (always filter by tenant_id)

**Best for:**
- SaaS platforms
- 100+ websites
- When efficiency > isolation

---

### **4. SQLITE_PER_SITE**

**How it works:**
- Each website gets a SQLite file
- Example:
  ```
  gym_website.db
  jewelry_store.db
  portfolio_site.db
  ```

**Advantages:**
- ✅ No server needed
- ✅ Simple deployment
- ✅ Good for static sites

**Disadvantages:**
- ❌ Limited concurrent writes
- ❌ Not suitable for high traffic
- ❌ File-based (harder to manage)

**Best for:**
- Simple sites
- Low traffic
- Local development

---

## 🆓 Free Tier Providers

### **Supabase (Recommended) ⭐**

```
Database: PostgreSQL
Free Tier:
  - 500MB database size
  - Unlimited API requests
  - Unlimited auth users
  - 2GB file storage
  - 2 projects max

Best for: TABLE_PREFIX strategy with 20-50 websites
```

**Setup:**
1. Go to https://supabase.com
2. Sign up / Log in
3. Create new project
4. Copy connection details from Settings → Database
5. Set environment variables:
   ```bash
   export SUPABASE_HOST="db.xxx.supabase.co"
   export SUPABASE_PORT="5432"
   export SUPABASE_DB="postgres"
   export SUPABASE_USER="postgres"
   export SUPABASE_PASSWORD="your-password"
   ```

---

### **Neon**

```
Database: PostgreSQL
Free Tier:
  - 3GB storage (6x more than Supabase!)
  - Autoscaling
  - Instant branching

Best for: Growing to 100+ websites
```

---

### **PlanetScale**

```
Database: MySQL
Free Tier:
  - 5GB storage
  - 1 billion row reads/month
  - 10 million row writes/month

Best for: MySQL users, larger databases
```

---

## 🚀 Usage Examples

### **Example 1: Quick Start (Free Tier)**

```python
from database_provisioner import DatabaseProvisioner, ProvisioningStrategy

# Create provisioner with defaults
provisioner = DatabaseProvisioner(
    default_strategy=ProvisioningStrategy.TABLE_PREFIX,
    default_provider=DatabaseProvider.SUPABASE
)

# Provision database for gym website
config = provisioner.provision_database("gym_website")

# Print results
print(f"Database: {config.database_name}")
print(f"Table prefix: {config.table_prefix}_")
print(f"Connection: {config.connection_string}")

# Tables will be:
# - gym_abc123_users
# - gym_abc123_products
# - gym_abc123_orders
```

**Output:**
```
Database: postgres
Table prefix: gymwebsite_a1b2c3_
Connection: postgresql://postgres:***@db.xxx.supabase.co:5432/postgres?sslmode=require
```

---

### **Example 2: Get Recommendation**

```python
provisioner = DatabaseProvisioner()

# Get recommendation based on requirements
strategy, provider = provisioner.recommend_setup(
    num_websites=25,        # Planning to create 25 sites
    use_free_tier=True,     # Must use free tier
    needs_isolation=False   # Don't need complete isolation
)

print(f"Strategy: {strategy.value}")  # TABLE_PREFIX
print(f"Provider: {provider.value}")  # SUPABASE
```

---

### **Example 3: Generate Schema**

```python
# Provision database
config = provisioner.provision_database(
    "gym_website",
    strategy=ProvisioningStrategy.TABLE_PREFIX
)

# Generate SQL schema
schema = provisioner.generate_schema(
    config,
    tables=['users', 'products', 'orders']
)

# Save to file
with open('schema.sql', 'w') as f:
    f.write(schema)

# Run on Supabase via SQL Editor
```

**Generated schema.sql:**
```sql
CREATE TABLE gymwebsite_a1b2c3_users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE gymwebsite_a1b2c3_products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INTEGER DEFAULT 0
);

CREATE TABLE gymwebsite_a1b2c3_orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES gymwebsite_a1b2c3_users(id),
    total DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending'
);
```

---

### **Example 4: Integration with Project Planner**

```python
from project_planner import ProjectPlanner
from database_provisioner import DatabaseProvisioner, ProvisioningStrategy

# User's prompt
user_prompt = "i want to build a gym website to showcase my gym and sell accessories"

# Step 1: Create project plan
planner = ProjectPlanner()
plan = planner.create_plan(user_prompt)

# Step 2: Provision database if needed
if plan.requirements.has_database:
    provisioner = DatabaseProvisioner()

    db_config = provisioner.provision_database(
        website_name=plan.project_name,
        strategy=ProvisioningStrategy.TABLE_PREFIX
    )

    # Step 3: Generate schema based on requirements
    tables = []
    if plan.requirements.has_authentication:
        tables.append('users')
    if plan.requirements.has_product_catalog:
        tables.append('products')
    if plan.requirements.has_shopping_cart:
        tables.extend(['orders', 'order_items'])

    schema = provisioner.generate_schema(db_config, tables)

    # Step 4: Save to project
    plan.database_config = db_config
    plan.database_schema = schema
```

---

## 💰 Cost Comparison

### **Free Tier (Supabase with TABLE_PREFIX)**

```
Setup:
  - 1 Supabase project (free)
  - 1 database (500MB)

Websites supported: ~20-50
Tables: ~100-250 (5 tables per site × 50 sites)
Cost: $0/month

Example:
  gym_abc123_users, gym_abc123_products, gym_abc123_orders
  jewelry_def456_users, jewelry_def456_products, jewelry_def456_orders
  ...
  (20-50 websites × 5 tables each = 100-250 tables)
```

---

### **Paid (Separate Databases)**

```
Setup:
  - AWS RDS PostgreSQL (db.t3.micro)
  - One database per website

Cost per website: ~$15/month
20 websites = $300/month

Better for: Production, high traffic, paying customers
```

---

## 🎯 Recommendation for Your Use Case

Based on your requirements:
- ✅ Free tier
- ✅ Creating multiple websites
- ✅ Need for payment/e-commerce features

**I recommend:**

### **Setup:**
```
Strategy: TABLE_PREFIX
Provider: Supabase (PostgreSQL)
Cost: $0/month
Capacity: 20-50 websites
```

### **Why this works:**

1. **Free tier optimized**
   - Single Supabase project (free)
   - 500MB database (enough for 20-50 sites)
   - No recurring costs

2. **Good isolation**
   - Each website has unique table prefix
   - Can't accidentally query another site's data
   - Easy to backup/restore per site

3. **Scalable**
   - Start with free tier
   - Upgrade to Neon (3GB) when needed
   - Eventually move to separate databases

4. **Simple migration**
   - When a site outgrows shared DB
   - Export tables with prefix
   - Move to dedicated database
   - No code changes needed

---

## 📋 Step-by-Step Implementation

### **Step 1: Set up Supabase**

1. Go to https://supabase.com
2. Create account
3. Create new project: "my-websites"
4. Wait 2 minutes for provisioning
5. Go to Settings → Database
6. Copy connection details

### **Step 2: Set Environment Variables**

Create `.env` file:
```bash
SUPABASE_HOST="db.xxx.supabase.co"
SUPABASE_PORT="5432"
SUPABASE_DB="postgres"
SUPABASE_USER="postgres"
SUPABASE_PASSWORD="your-secure-password"
```

### **Step 3: Provision First Website**

```python
from database_provisioner import DatabaseProvisioner, ProvisioningStrategy

provisioner = DatabaseProvisioner(
    default_strategy=ProvisioningStrategy.TABLE_PREFIX
)

# Create database config
config = provisioner.provision_database("gym_website")

# Generate schema
schema = provisioner.generate_schema(
    config,
    tables=['users', 'products', 'orders']
)

# Save schema
with open('gym_website_schema.sql', 'w') as f:
    f.write(schema)

# Save config to .env for website
with open('gym_website.env', 'w') as f:
    f.write(f'DATABASE_URL="{config.connection_string}"\n')
    f.write(f'TABLE_PREFIX="{config.table_prefix}"\n')
```

### **Step 4: Run Schema in Supabase**

1. Go to Supabase SQL Editor
2. Paste contents of `gym_website_schema.sql`
3. Click Run
4. Tables created with prefix!

### **Step 5: Use in Generated Code**

Your generated website code will use:
```javascript
// In backend/config/database.js
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

// In queries, use table prefix
const TABLE_PREFIX = process.env.TABLE_PREFIX || '';

async function getUsers() {
  const result = await pool.query(
    `SELECT * FROM ${TABLE_PREFIX}_users`
  );
  return result.rows;
}
```

---

## 🔄 Complete Workflow

```
User Input
  ↓
[Prompt Enhancer] → Enhanced specification
  ↓
[Project Planner] → Detects database requirement
  ↓
[Database Provisioner] → Recommends TABLE_PREFIX + Supabase
  ↓
provision_database("gym_website")
  ↓
generate_schema(['users', 'products', 'orders'])
  ↓
Save schema.sql + database config
  ↓
[Template Generator] → Uses database config
  ↓
Generate code with:
  - DATABASE_URL in .env
  - TABLE_PREFIX in queries
  - Schema migration file
  ↓
✅ Deployed website with database!
```

---

## 📈 Scaling Path

### **Phase 1: Starting (Free Tier)**
```
Strategy: TABLE_PREFIX
Provider: Supabase (500MB free)
Websites: 0-20
Cost: $0/month
```

### **Phase 2: Growing (Still Free)**
```
Strategy: TABLE_PREFIX
Provider: Neon (3GB free)
Websites: 20-100
Cost: $0/month
```

### **Phase 3: Production (Paid)**
```
Strategy: SEPARATE_DATABASE
Provider: Supabase Pro or AWS RDS
Websites: Unlimited
Cost: ~$25/month (Supabase Pro) or pay per DB
```

---

## ✅ Summary

**The Database Provisioning System:**

✅ **Automatically provisions databases** for generated websites
✅ **Optimizes for free tier** (20-50 sites in 500MB)
✅ **Generates SQL schemas** based on requirements
✅ **Manages credentials** via environment variables
✅ **Provides migration path** to production
✅ **Integrates with Project Planner** for seamless workflow

**For your gym website example:**
- Strategy: TABLE_PREFIX
- Provider: Supabase (free)
- Tables: `gym_abc123_users`, `gym_abc123_products`, `gym_abc123_orders`
- Cost: $0
- Can add 19+ more websites to same database

---

## 🚀 Next Steps

1. **Set up Supabase account** (5 minutes)
2. **Set environment variables** in `.env`
3. **Run test:** `python test_database_provisioner.py`
4. **Integrate with planner:** Database provisioning happens automatically
5. **Generate first website:** Database gets provisioned and schema created

**You're ready to generate unlimited websites with free-tier databases!** 🎯
