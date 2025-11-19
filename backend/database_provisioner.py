"""
Database Provisioning System
Handles database creation and management for generated websites
Supports free-tier services and multiple provisioning strategies
"""

import os
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import hashlib

logger = logging.getLogger(__name__)


# ============================================================================
# PROVISIONING STRATEGIES
# ============================================================================

class ProvisioningStrategy(Enum):
    """How to provision databases for websites"""

    # One database per website (best isolation, production-ready)
    SEPARATE_DATABASE = "separate_database"

    # One database, tables prefixed by site (good for free tier)
    TABLE_PREFIX = "table_prefix"

    # Shared tables with tenant_id column (most efficient)
    MULTI_TENANT = "multi_tenant"

    # SQLite per site (simple, file-based)
    SQLITE_PER_SITE = "sqlite_per_site"


class DatabaseProvider(Enum):
    """Supported database providers"""

    # Free tier options
    SUPABASE = "supabase"          # PostgreSQL, 500MB free
    PLANETSCALE = "planetscale"    # MySQL, 5GB free
    NEON = "neon"                  # PostgreSQL, 3GB free
    RAILWAY = "railway"            # PostgreSQL, 500MB free

    # Self-hosted options
    POSTGRESQL_LOCAL = "postgresql_local"
    MYSQL_LOCAL = "mysql_local"
    SQLITE = "sqlite"

    # Production options
    AWS_RDS = "aws_rds"
    GOOGLE_CLOUD_SQL = "google_cloud_sql"
    AZURE_DATABASE = "azure_database"


@dataclass
class DatabaseConfig:
    """Database configuration for a website"""

    # Identity
    website_id: str
    website_name: str

    # Strategy
    strategy: ProvisioningStrategy
    provider: DatabaseProvider

    # Connection details
    host: str
    port: int
    database_name: str
    username: str
    password: str

    # For table prefix strategy
    table_prefix: Optional[str] = None

    # For multi-tenant strategy
    tenant_id: Optional[str] = None

    # SSL/TLS
    ssl_required: bool = True

    # Connection string
    connection_string: str = ""

    def __post_init__(self):
        """Generate connection string"""
        if not self.connection_string:
            self.connection_string = self._build_connection_string()

    def _build_connection_string(self) -> str:
        """Build database connection string"""

        if self.provider == DatabaseProvider.SQLITE:
            return f"sqlite:///{self.database_name}.db"

        # PostgreSQL format
        if self.provider in [DatabaseProvider.SUPABASE, DatabaseProvider.NEON,
                            DatabaseProvider.RAILWAY, DatabaseProvider.POSTGRESQL_LOCAL]:
            ssl_param = "?sslmode=require" if self.ssl_required else ""
            return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database_name}{ssl_param}"

        # MySQL format
        if self.provider in [DatabaseProvider.PLANETSCALE, DatabaseProvider.MYSQL_LOCAL]:
            ssl_param = "?ssl-mode=REQUIRED" if self.ssl_required else ""
            return f"mysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database_name}{ssl_param}"

        return ""


# ============================================================================
# DATABASE PROVISIONER
# ============================================================================

class DatabaseProvisioner:
    """
    Provisions databases for generated websites
    Recommends best strategy based on requirements
    """

    def __init__(
        self,
        default_strategy: ProvisioningStrategy = ProvisioningStrategy.TABLE_PREFIX,
        default_provider: DatabaseProvider = DatabaseProvider.SUPABASE
    ):
        """
        Args:
            default_strategy: Default provisioning strategy
            default_provider: Default database provider
        """
        self.default_strategy = default_strategy
        self.default_provider = default_provider

    def recommend_setup(
        self,
        num_websites: int,
        use_free_tier: bool,
        needs_isolation: bool
    ) -> Tuple[ProvisioningStrategy, DatabaseProvider]:
        """
        Recommend best setup based on requirements

        Args:
            num_websites: Expected number of websites
            use_free_tier: Must use free tier
            needs_isolation: Need strong isolation between sites

        Returns:
            (strategy, provider)
        """
        # If needs strong isolation and not worried about cost
        if needs_isolation and not use_free_tier:
            return (
                ProvisioningStrategy.SEPARATE_DATABASE,
                DatabaseProvider.AWS_RDS
            )

        # If free tier and few websites
        if use_free_tier and num_websites <= 5:
            return (
                ProvisioningStrategy.SEPARATE_DATABASE,
                DatabaseProvider.SUPABASE  # Free tier allows multiple projects
            )

        # If free tier and many websites
        if use_free_tier and num_websites > 5:
            return (
                ProvisioningStrategy.TABLE_PREFIX,
                DatabaseProvider.SUPABASE  # 500MB free, shared DB
            )

        # Default for medium scale
        return (
            ProvisioningStrategy.TABLE_PREFIX,
            DatabaseProvider.NEON
        )

    def provision_database(
        self,
        website_name: str,
        strategy: Optional[ProvisioningStrategy] = None,
        provider: Optional[DatabaseProvider] = None
    ) -> DatabaseConfig:
        """
        Provision a database for a website

        Args:
            website_name: Name of the website
            strategy: Provisioning strategy (uses default if None)
            provider: Database provider (uses default if None)

        Returns:
            DatabaseConfig with connection details
        """
        strategy = strategy or self.default_strategy
        provider = provider or self.default_provider

        # Generate website ID
        website_id = self._generate_website_id(website_name)

        # Get provider credentials from environment
        creds = self._get_provider_credentials(provider)

        if strategy == ProvisioningStrategy.SEPARATE_DATABASE:
            return self._provision_separate_database(
                website_id, website_name, provider, creds
            )

        elif strategy == ProvisioningStrategy.TABLE_PREFIX:
            return self._provision_table_prefix(
                website_id, website_name, provider, creds
            )

        elif strategy == ProvisioningStrategy.MULTI_TENANT:
            return self._provision_multi_tenant(
                website_id, website_name, provider, creds
            )

        elif strategy == ProvisioningStrategy.SQLITE_PER_SITE:
            return self._provision_sqlite(website_id, website_name)

        raise ValueError(f"Unknown strategy: {strategy}")

    def _provision_separate_database(
        self,
        website_id: str,
        website_name: str,
        provider: DatabaseProvider,
        creds: Dict
    ) -> DatabaseConfig:
        """Provision separate database for website"""

        # Generate unique database name
        db_name = self._sanitize_db_name(f"{website_name}_{website_id[:8]}")

        logger.info(f"Provisioning separate database: {db_name}")

        config = DatabaseConfig(
            website_id=website_id,
            website_name=website_name,
            strategy=ProvisioningStrategy.SEPARATE_DATABASE,
            provider=provider,
            host=creds['host'],
            port=creds['port'],
            database_name=db_name,
            username=creds['username'],
            password=creds['password'],
            ssl_required=creds.get('ssl_required', True)
        )

        # Note: Actual database creation would happen here via provider API
        logger.info(f"Database config created: {db_name}")
        logger.warning("⚠️  Manual step: Create database via provider dashboard")
        logger.warning(f"   Database name: {db_name}")

        return config

    def _provision_table_prefix(
        self,
        website_id: str,
        website_name: str,
        provider: DatabaseProvider,
        creds: Dict
    ) -> DatabaseConfig:
        """Provision with table prefix strategy"""

        # Use shared database
        db_name = creds.get('database', 'shared_db')

        # Generate table prefix
        prefix = self._sanitize_table_prefix(website_name, website_id)

        logger.info(f"Provisioning with table prefix: {prefix}_")

        config = DatabaseConfig(
            website_id=website_id,
            website_name=website_name,
            strategy=ProvisioningStrategy.TABLE_PREFIX,
            provider=provider,
            host=creds['host'],
            port=creds['port'],
            database_name=db_name,
            username=creds['username'],
            password=creds['password'],
            table_prefix=prefix,
            ssl_required=creds.get('ssl_required', True)
        )

        logger.info(f"Table prefix config created: {prefix}_")
        return config

    def _provision_multi_tenant(
        self,
        website_id: str,
        website_name: str,
        provider: DatabaseProvider,
        creds: Dict
    ) -> DatabaseConfig:
        """Provision with multi-tenant strategy"""

        # Use shared database
        db_name = creds.get('database', 'multitenant_db')

        logger.info(f"Provisioning multi-tenant for: {website_name}")

        config = DatabaseConfig(
            website_id=website_id,
            website_name=website_name,
            strategy=ProvisioningStrategy.MULTI_TENANT,
            provider=provider,
            host=creds['host'],
            port=creds['port'],
            database_name=db_name,
            username=creds['username'],
            password=creds['password'],
            tenant_id=website_id,
            ssl_required=creds.get('ssl_required', True)
        )

        logger.info(f"Multi-tenant config created with tenant_id: {website_id}")
        return config

    def _provision_sqlite(
        self,
        website_id: str,
        website_name: str
    ) -> DatabaseConfig:
        """Provision SQLite database"""

        db_name = self._sanitize_db_name(f"{website_name}_{website_id[:8]}")

        logger.info(f"Provisioning SQLite database: {db_name}.db")

        config = DatabaseConfig(
            website_id=website_id,
            website_name=website_name,
            strategy=ProvisioningStrategy.SQLITE_PER_SITE,
            provider=DatabaseProvider.SQLITE,
            host="localhost",
            port=0,
            database_name=db_name,
            username="",
            password="",
            ssl_required=False
        )

        return config

    def _get_provider_credentials(self, provider: DatabaseProvider) -> Dict:
        """Get credentials from environment variables"""

        if provider == DatabaseProvider.SUPABASE:
            return {
                'host': os.getenv('SUPABASE_HOST', 'db.xxx.supabase.co'),
                'port': int(os.getenv('SUPABASE_PORT', '5432')),
                'database': os.getenv('SUPABASE_DB', 'postgres'),
                'username': os.getenv('SUPABASE_USER', 'postgres'),
                'password': os.getenv('SUPABASE_PASSWORD', ''),
                'ssl_required': True
            }

        elif provider == DatabaseProvider.PLANETSCALE:
            return {
                'host': os.getenv('PLANETSCALE_HOST', ''),
                'port': int(os.getenv('PLANETSCALE_PORT', '3306')),
                'database': os.getenv('PLANETSCALE_DB', ''),
                'username': os.getenv('PLANETSCALE_USER', ''),
                'password': os.getenv('PLANETSCALE_PASSWORD', ''),
                'ssl_required': True
            }

        elif provider == DatabaseProvider.NEON:
            return {
                'host': os.getenv('NEON_HOST', ''),
                'port': int(os.getenv('NEON_PORT', '5432')),
                'database': os.getenv('NEON_DB', 'neondb'),
                'username': os.getenv('NEON_USER', ''),
                'password': os.getenv('NEON_PASSWORD', ''),
                'ssl_required': True
            }

        elif provider == DatabaseProvider.POSTGRESQL_LOCAL:
            return {
                'host': os.getenv('POSTGRES_HOST', 'localhost'),
                'port': int(os.getenv('POSTGRES_PORT', '5432')),
                'database': os.getenv('POSTGRES_DB', 'websites_db'),
                'username': os.getenv('POSTGRES_USER', 'postgres'),
                'password': os.getenv('POSTGRES_PASSWORD', 'postgres'),
                'ssl_required': False
            }

        elif provider == DatabaseProvider.MYSQL_LOCAL:
            return {
                'host': os.getenv('MYSQL_HOST', 'localhost'),
                'port': int(os.getenv('MYSQL_PORT', '3306')),
                'database': os.getenv('MYSQL_DB', 'websites_db'),
                'username': os.getenv('MYSQL_USER', 'root'),
                'password': os.getenv('MYSQL_PASSWORD', 'password'),
                'ssl_required': False
            }

        elif provider == DatabaseProvider.AWS_RDS:
            return {
                'host': os.getenv('AWS_RDS_HOST', ''),
                'port': int(os.getenv('AWS_RDS_PORT', '5432')),
                'database': os.getenv('AWS_RDS_DB', 'websites'),
                'username': os.getenv('AWS_RDS_USER', 'admin'),
                'password': os.getenv('AWS_RDS_PASSWORD', ''),
                'ssl_required': True
            }

        elif provider == DatabaseProvider.GOOGLE_CLOUD_SQL:
            return {
                'host': os.getenv('GCP_SQL_HOST', ''),
                'port': int(os.getenv('GCP_SQL_PORT', '5432')),
                'database': os.getenv('GCP_SQL_DB', 'websites'),
                'username': os.getenv('GCP_SQL_USER', 'postgres'),
                'password': os.getenv('GCP_SQL_PASSWORD', ''),
                'ssl_required': True
            }

        elif provider == DatabaseProvider.AZURE_DATABASE:
            return {
                'host': os.getenv('AZURE_DB_HOST', ''),
                'port': int(os.getenv('AZURE_DB_PORT', '5432')),
                'database': os.getenv('AZURE_DB_NAME', 'websites'),
                'username': os.getenv('AZURE_DB_USER', 'azureuser'),
                'password': os.getenv('AZURE_DB_PASSWORD', ''),
                'ssl_required': True
            }

        raise ValueError(f"Unknown provider: {provider}")

    def _generate_website_id(self, website_name: str) -> str:
        """Generate unique website ID"""
        # Use hash of name + timestamp for uniqueness
        import time
        content = f"{website_name}_{time.time()}"
        return hashlib.md5(content.encode()).hexdigest()

    def _sanitize_db_name(self, name: str) -> str:
        """Sanitize database name"""
        # Remove special characters, convert to lowercase
        import re
        sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name).lower()
        # Limit length
        return sanitized[:63]  # PostgreSQL limit

    def _sanitize_table_prefix(self, name: str, website_id: str) -> str:
        """Generate safe table prefix"""
        import re
        # Use first part of name + first 6 chars of ID
        sanitized = re.sub(r'[^a-zA-Z0-9]', '', name).lower()
        short_id = website_id[:6]
        prefix = f"{sanitized[:10]}_{short_id}"
        return prefix

    def generate_schema(
        self,
        config: DatabaseConfig,
        tables: List[str]
    ) -> str:
        """
        Generate SQL schema based on strategy

        Args:
            config: Database configuration
            tables: List of table names needed

        Returns:
            SQL schema string
        """
        if config.strategy == ProvisioningStrategy.TABLE_PREFIX:
            return self._generate_prefixed_schema(config, tables)
        elif config.strategy == ProvisioningStrategy.MULTI_TENANT:
            return self._generate_multitenant_schema(config, tables)
        else:
            return self._generate_standard_schema(config, tables)

    def _generate_standard_schema(
        self,
        config: DatabaseConfig,
        tables: List[str]
    ) -> str:
        """Generate standard schema"""

        sql_parts = []

        if 'users' in tables:
            sql_parts.append("""
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
""")

        if 'products' in tables:
            sql_parts.append("""
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    image_url VARCHAR(500),
    stock INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_products_name ON products(name);
""")

        if 'orders' in tables:
            sql_parts.append("""
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    total DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    stripe_payment_id VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
""")

        return "\n".join(sql_parts)

    def _generate_prefixed_schema(
        self,
        config: DatabaseConfig,
        tables: List[str]
    ) -> str:
        """Generate schema with table prefixes"""

        prefix = config.table_prefix

        sql_parts = []

        if 'users' in tables:
            sql_parts.append(f"""
CREATE TABLE {prefix}_users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

        if 'products' in tables:
            sql_parts.append(f"""
CREATE TABLE {prefix}_products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INTEGER DEFAULT 0
);
""")

        if 'orders' in tables:
            sql_parts.append(f"""
CREATE TABLE {prefix}_orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES {prefix}_users(id),
    total DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending'
);
""")

        return "\n".join(sql_parts)

    def _generate_multitenant_schema(
        self,
        config: DatabaseConfig,
        tables: List[str]
    ) -> str:
        """Generate multi-tenant schema with tenant_id"""

        sql_parts = []

        if 'users' in tables:
            sql_parts.append("""
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    tenant_id VARCHAR(32) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, email)
);

CREATE INDEX idx_users_tenant ON users(tenant_id);
""")

        if 'products' in tables:
            sql_parts.append("""
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    tenant_id VARCHAR(32) NOT NULL,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INTEGER DEFAULT 0
);

CREATE INDEX idx_products_tenant ON products(tenant_id);
""")

        if 'orders' in tables:
            sql_parts.append("""
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    tenant_id VARCHAR(32) NOT NULL,
    user_id INTEGER REFERENCES users(id),
    total DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending'
);

CREATE INDEX idx_orders_tenant ON orders(tenant_id);
""")

        return "\n".join(sql_parts)


# ============================================================================
# FREE TIER SETUP GUIDES
# ============================================================================

class SetupGuide:
    """Provides setup guides for free-tier services"""

    @staticmethod
    def supabase_guide() -> str:
        """Guide for Supabase setup"""
        return """
🟢 SUPABASE SETUP (PostgreSQL - FREE TIER)

1. Go to https://supabase.com
2. Sign up / Log in
3. Click "New Project"
4. Fill in:
   - Project name: your-website-name
   - Database password: (generate strong password)
   - Region: Choose closest to you
5. Wait for project to provision (~2 minutes)
6. Go to Settings → Database
7. Copy connection details:
   - Host: db.xxx.supabase.co
   - Port: 5432
   - Database: postgres
   - User: postgres
   - Password: (your password)

8. Set environment variables:
   export SUPABASE_HOST="db.xxx.supabase.co"
   export SUPABASE_PORT="5432"
   export SUPABASE_DB="postgres"
   export SUPABASE_USER="postgres"
   export SUPABASE_PASSWORD="your-password"

Free Tier Limits:
- 500MB database size
- Unlimited API requests
- Unlimited Auth users
- 2GB file storage

RECOMMENDED FOR: Development, small sites, up to 5 separate databases
"""

    @staticmethod
    def planetscale_guide() -> str:
        """Guide for PlanetScale setup"""
        return """
🟠 PLANETSCALE SETUP (MySQL - FREE TIER)

1. Go to https://planetscale.com
2. Sign up with GitHub
3. Create new database
4. Click "Connect"
5. Select "General" or "Prisma"
6. Copy connection string

Free Tier Limits:
- 5GB storage
- 1 billion row reads/month
- 10 million row writes/month
- Branching support

RECOMMENDED FOR: MySQL users, larger free tier
"""

    @staticmethod
    def neon_guide() -> str:
        """Guide for Neon setup"""
        return """
🟣 NEON SETUP (PostgreSQL - FREE TIER)

1. Go to https://neon.tech
2. Sign up
3. Create new project
4. Copy connection string from dashboard

Free Tier Limits:
- 3GB storage (larger than Supabase!)
- Autoscaling
- Instant branching

RECOMMENDED FOR: PostgreSQL users who need more storage
"""


# ============================================================================
# RECOMMENDATIONS
# ============================================================================

def print_recommendations():
    """Print database strategy recommendations"""

    print("=" * 80)
    print("DATABASE STRATEGY RECOMMENDATIONS")
    print("=" * 80)
    print()

    print("📊 STRATEGY COMPARISON:")
    print()
    print("1. SEPARATE DATABASE (One DB per website)")
    print("   ✅ Pros:")
    print("      - Best isolation")
    print("      - Can scale each site independently")
    print("      - Easier to backup/restore individual sites")
    print("   ❌ Cons:")
    print("      - May hit free tier limits quickly")
    print("      - More complex management")
    print("      - Each DB needs separate credentials")
    print("   💰 Best for: Production, paying customers")
    print()

    print("2. TABLE PREFIX (One DB, prefixed tables)")
    print("   ✅ Pros:")
    print("      - Good isolation")
    print("      - Works great with free tier")
    print("      - Can handle many websites in one DB")
    print("   ❌ Cons:")
    print("      - Slightly more complex queries")
    print("      - All sites affected if DB goes down")
    print("   💰 Best for: Free tier, development, 10-100 sites")
    print()

    print("3. MULTI-TENANT (Shared tables with tenant_id)")
    print("   ✅ Pros:")
    print("      - Most efficient use of resources")
    print("      - Standard SaaS pattern")
    print("      - Easiest to manage")
    print("   ❌ Cons:")
    print("      - Need careful security (row-level)")
    print("      - All sites in same tables")
    print("   💰 Best for: SaaS platforms, 100+ sites")
    print()

    print("=" * 80)
    print()

    print("🎯 RECOMMENDATION FOR YOUR USE CASE:")
    print()
    print("Starting out (Free tier):")
    print("  → Strategy: TABLE_PREFIX")
    print("  → Provider: Supabase (500MB free)")
    print("  → Can handle: ~20-50 websites")
    print()
    print("Growing (Still free):")
    print("  → Strategy: TABLE_PREFIX")
    print("  → Provider: Neon (3GB free)")
    print("  → Can handle: ~100+ websites")
    print()
    print("Production (Paid):")
    print("  → Strategy: SEPARATE_DATABASE")
    print("  → Provider: AWS RDS or Supabase Pro")
    print("  → Unlimited websites")
    print()
