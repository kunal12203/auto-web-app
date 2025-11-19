"""
Test Database Provisioner with real examples
Shows different provisioning strategies and setup guides
"""

import logging
from database_provisioner import (
    DatabaseProvisioner,
    ProvisioningStrategy,
    DatabaseProvider,
    SetupGuide,
    print_recommendations
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_free_tier_recommendations():
    """Test recommendations for free tier"""
    print("\n")
    print("🆓" * 40)
    print("EXAMPLE 1: FREE TIER RECOMMENDATIONS")
    print("🆓" * 40)
    print()

    provisioner = DatabaseProvisioner()

    # Test case 1: Few websites
    print("Scenario 1: Starting out with 3 websites")
    strategy, provider = provisioner.recommend_setup(
        num_websites=3,
        use_free_tier=True,
        needs_isolation=False
    )
    print(f"  ✅ Recommended Strategy: {strategy.value}")
    print(f"  ✅ Recommended Provider: {provider.value}")
    print(f"  💡 Each website gets its own database (within free tier)")
    print()

    # Test case 2: Many websites
    print("Scenario 2: Growing with 20 websites")
    strategy, provider = provisioner.recommend_setup(
        num_websites=20,
        use_free_tier=True,
        needs_isolation=False
    )
    print(f"  ✅ Recommended Strategy: {strategy.value}")
    print(f"  ✅ Recommended Provider: {provider.value}")
    print(f"  💡 One database with prefixed tables (fits in free tier)")
    print()


def test_gym_website_provisioning():
    """Test provisioning for gym website example"""
    print("\n")
    print("🏋️" * 40)
    print("EXAMPLE 2: GYM WEBSITE PROVISIONING")
    print("🏋️" * 40)
    print()

    provisioner = DatabaseProvisioner(
        default_strategy=ProvisioningStrategy.TABLE_PREFIX,
        default_provider=DatabaseProvider.SUPABASE
    )

    # Provision database for gym website
    print("Provisioning database for: 'Gym Website'")
    print()

    config = provisioner.provision_database(
        website_name="gym_website",
        strategy=ProvisioningStrategy.TABLE_PREFIX
    )

    print("✅ DATABASE PROVISIONED:")
    print(f"  Website ID: {config.website_id}")
    print(f"  Strategy: {config.strategy.value}")
    print(f"  Provider: {config.provider.value}")
    print(f"  Database: {config.database_name}")
    print(f"  Table Prefix: {config.table_prefix}_")
    print()

    print("Example tables that will be created:")
    print(f"  - {config.table_prefix}_users")
    print(f"  - {config.table_prefix}_products")
    print(f"  - {config.table_prefix}_orders")
    print(f"  - {config.table_prefix}_order_items")
    print()

    print("Connection string (for .env file):")
    print(f"  DATABASE_URL=\"{config.connection_string}\"")
    print(f"  TABLE_PREFIX=\"{config.table_prefix}\"")
    print()

    # Generate schema
    print("Generating SQL schema...")
    schema = provisioner.generate_schema(
        config,
        tables=['users', 'products', 'orders']
    )
    print("\nSQL Schema Preview:")
    print("=" * 60)
    print(schema[:500] + "...")
    print("=" * 60)
    print()


def test_multiple_websites_table_prefix():
    """Test multiple websites with table prefix strategy"""
    print("\n")
    print("🌐" * 40)
    print("EXAMPLE 3: MULTIPLE WEBSITES (TABLE PREFIX)")
    print("🌐" * 40)
    print()

    provisioner = DatabaseProvisioner(
        default_strategy=ProvisioningStrategy.TABLE_PREFIX,
        default_provider=DatabaseProvider.SUPABASE
    )

    websites = [
        "gym_website",
        "jewelry_store",
        "portfolio_site",
        "restaurant_menu"
    ]

    print("Provisioning 4 websites with TABLE_PREFIX strategy:")
    print("(All using one Supabase free tier database)")
    print()

    configs = []
    for site_name in websites:
        config = provisioner.provision_database(site_name)
        configs.append(config)

        print(f"✅ {site_name}")
        print(f"   Table prefix: {config.table_prefix}_")
        print(f"   Tables: {config.table_prefix}_users, {config.table_prefix}_products, ...")
        print()

    print("=" * 80)
    print("RESULT:")
    print(f"  ✅ All 4 websites in ONE Supabase database")
    print(f"  ✅ Each has unique table prefix for isolation")
    print(f"  ✅ Estimated DB size: ~50-100MB (well within 500MB free tier)")
    print(f"  ✅ Can add ~20-30 more websites before hitting limits")
    print()


def test_multi_tenant_strategy():
    """Test multi-tenant strategy for SaaS"""
    print("\n")
    print("🏢" * 40)
    print("EXAMPLE 4: MULTI-TENANT (SAAS PLATFORM)")
    print("🏢" * 40)
    print()

    provisioner = DatabaseProvisioner(
        default_strategy=ProvisioningStrategy.MULTI_TENANT,
        default_provider=DatabaseProvider.NEON
    )

    print("Provisioning for SaaS platform with many customers:")
    print()

    # Provision 3 sites
    sites = ["gym_a", "gym_b", "gym_c"]
    for site in sites:
        config = provisioner.provision_database(
            site,
            strategy=ProvisioningStrategy.MULTI_TENANT
        )
        print(f"✅ {site}")
        print(f"   Tenant ID: {config.tenant_id}")
        print()

    print("Schema structure (shared tables):")
    print("  users:")
    print("    - tenant_id (to separate gym_a, gym_b, gym_c)")
    print("    - email")
    print("    - password_hash")
    print()
    print("  products:")
    print("    - tenant_id")
    print("    - name")
    print("    - price")
    print()
    print("Example query:")
    print("  SELECT * FROM users WHERE tenant_id = 'gym_a_tenant_id'")
    print()


def test_separate_database_production():
    """Test separate database strategy for production"""
    print("\n")
    print("🚀" * 40)
    print("EXAMPLE 5: SEPARATE DATABASES (PRODUCTION)")
    print("🚀" * 40)
    print()

    provisioner = DatabaseProvisioner(
        default_strategy=ProvisioningStrategy.SEPARATE_DATABASE,
        default_provider=DatabaseProvider.AWS_RDS
    )

    print("Provisioning for production with dedicated databases:")
    print()

    config = provisioner.provision_database(
        "enterprise_gym",
        strategy=ProvisioningStrategy.SEPARATE_DATABASE
    )

    print(f"✅ DATABASE: {config.database_name}")
    print(f"  Provider: {config.provider.value}")
    print(f"  Strategy: {config.strategy.value}")
    print()
    print("Benefits:")
    print("  ✅ Completely isolated from other sites")
    print("  ✅ Can scale independently")
    print("  ✅ Easier backup/restore")
    print("  ✅ Production-grade reliability")
    print()


def test_setup_guides():
    """Show setup guides for free tier services"""
    print("\n")
    print("📚" * 40)
    print("SETUP GUIDES")
    print("📚" * 40)

    print(SetupGuide.supabase_guide())
    print()
    print(SetupGuide.planetscale_guide())
    print()
    print(SetupGuide.neon_guide())
    print()


def test_schema_generation():
    """Test SQL schema generation for different strategies"""
    print("\n")
    print("🗄️" * 40)
    print("EXAMPLE 6: SCHEMA GENERATION")
    print("🗄️" * 40)
    print()

    provisioner = DatabaseProvisioner()

    # Test 1: Standard schema
    print("1. STANDARD SCHEMA (Separate database):")
    print("-" * 60)
    config1 = provisioner.provision_database(
        "test_site_1",
        strategy=ProvisioningStrategy.SEPARATE_DATABASE
    )
    schema1 = provisioner.generate_schema(config1, ['users', 'products'])
    print(schema1)
    print()

    # Test 2: Prefixed schema
    print("2. PREFIXED SCHEMA (Table prefix):")
    print("-" * 60)
    config2 = provisioner.provision_database(
        "test_site_2",
        strategy=ProvisioningStrategy.TABLE_PREFIX
    )
    schema2 = provisioner.generate_schema(config2, ['users', 'products'])
    print(schema2)
    print()

    # Test 3: Multi-tenant schema
    print("3. MULTI-TENANT SCHEMA (Shared with tenant_id):")
    print("-" * 60)
    config3 = provisioner.provision_database(
        "test_site_3",
        strategy=ProvisioningStrategy.MULTI_TENANT
    )
    schema3 = provisioner.generate_schema(config3, ['users', 'products'])
    print(schema3)
    print()


def run_all_tests():
    """Run all provisioning tests"""
    print("\n")
    print("🧪" * 40)
    print("DATABASE PROVISIONER TEST SUITE")
    print("🧪" * 40)

    # Show recommendations first
    print_recommendations()

    # Test 1: Free tier recommendations
    test_free_tier_recommendations()

    # Test 2: Gym website example
    test_gym_website_provisioning()

    # Test 3: Multiple websites with table prefix
    test_multiple_websites_table_prefix()

    # Test 4: Multi-tenant
    test_multi_tenant_strategy()

    # Test 5: Production separate databases
    test_separate_database_production()

    # Test 6: Schema generation
    test_schema_generation()

    # Show setup guides
    test_setup_guides()

    print("\n")
    print("=" * 80)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 80)
    print()
    print("Key Takeaways:")
    print()
    print("  1. ✅ TABLE_PREFIX strategy is best for free tier")
    print("  2. ✅ Can handle 20-50 websites in Supabase 500MB free tier")
    print("  3. ✅ Each website gets isolated tables with unique prefix")
    print("  4. ✅ Easy migration path to SEPARATE_DATABASE later")
    print("  5. ✅ Automatic schema generation based on requirements")
    print()
    print("Next Steps:")
    print("  1. Set up Supabase account (see setup guide above)")
    print("  2. Set environment variables (SUPABASE_HOST, etc.)")
    print("  3. Use provisioner.provision_database() for each new site")
    print("  4. Run generated SQL schema to create tables")
    print()


if __name__ == "__main__":
    run_all_tests()
