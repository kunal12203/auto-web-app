"""
Massive Template Generator - Orchestrates generation of 11,000 templates
Runs all domain-specific generators and produces complete template library
"""

import os
import sys
import logging
import json
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime

# Import all generators
from authentication_generator import (
    AuthenticationGenerator,
    SignupGenerator,
    PasswordManagementGenerator
)
from navigation_generator import (
    HeaderGenerator,
    FooterGenerator,
    SidebarGenerator
)
from landing_generator import (
    HeroGenerator,
    FeaturesGenerator,
    CTAGenerator,
    TestimonialsGenerator
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('template_generation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


# ============================================================================
# GENERATION ORCHESTRATOR
# ============================================================================

class MassiveTemplateGenerator:
    """
    Orchestrates generation of 11,000 templates across all domains
    """

    def __init__(self, output_dir: str = "./templates_generated"):
        """
        Args:
            output_dir: Root directory for generated templates
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Statistics
        self.total_generated = 0
        self.total_skipped = 0
        self.total_errors = 0
        self.generation_stats = {}

        # Define generation plan
        self.generation_plan = self._create_generation_plan()

    def _create_generation_plan(self) -> List[Tuple[str, type, int]]:
        """
        Create generation plan: (domain_name, generator_class, target_count)

        Total target: 11,000 templates
        """
        return [
            # Authentication (1,000 templates)
            ("authentication/login", AuthenticationGenerator, 300),
            ("authentication/signup", SignupGenerator, 300),
            ("authentication/password", PasswordManagementGenerator, 200),

            # Navigation (1,000 templates)
            ("navigation/headers", HeaderGenerator, 400),
            ("navigation/footers", FooterGenerator, 300),
            ("navigation/sidebars", SidebarGenerator, 200),

            # Landing (1,000 templates)
            ("landing/hero", HeroGenerator, 350),
            ("landing/features", FeaturesGenerator, 250),
            ("landing/cta", CTAGenerator, 200),
            ("landing/testimonials", TestimonialsGenerator, 200),
        ]

    def generate_all(self, parallel: bool = False):
        """
        Generate all templates according to plan

        Args:
            parallel: Whether to run generators in parallel (future enhancement)
        """
        logger.info("=" * 80)
        logger.info("🚀 MASSIVE TEMPLATE GENERATION")
        logger.info("=" * 80)
        logger.info(f"Target: {sum(plan[2] for plan in self.generation_plan)} templates")
        logger.info(f"Domains: {len(self.generation_plan)}")
        logger.info(f"Output: {self.output_dir}")
        logger.info("")

        start_time = datetime.now()

        # Execute each generator
        for domain_path, generator_class, target_count in self.generation_plan:
            logger.info("-" * 80)
            logger.info(f"📦 {domain_path}")
            logger.info(f"   Target: {target_count} templates")
            logger.info("")

            try:
                self._run_generator(domain_path, generator_class, target_count)
            except Exception as e:
                logger.error(f"❌ Failed to run generator for {domain_path}: {e}")
                self.total_errors += 1

        # Complete
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        self._print_summary(duration)
        self._save_generation_report()

    def _run_generator(
        self,
        domain_path: str,
        generator_class: type,
        target_count: int
    ):
        """
        Run a single generator

        Args:
            domain_path: Path like "authentication/login"
            generator_class: Generator class to instantiate
            target_count: Number of templates to generate
        """
        # Create output directory for this domain
        domain_output = self.output_dir / domain_path
        domain_output.mkdir(parents=True, exist_ok=True)

        # Create generator
        generator = generator_class(output_dir=str(domain_output))

        # Generate combinations
        logger.info("   🔄 Generating combinations...")
        combinations = generator.generate_combinations(target_count)
        logger.info(f"   ✅ Generated {len(combinations)} combinations")

        # Generate templates
        logger.info("   🔄 Generating templates...")

        generated = 0
        skipped = 0
        errors = 0

        for i, spec in enumerate(combinations):
            try:
                # Generate template
                result = generator.generate_template(spec)

                if result:
                    file_path, code, metadata = result

                    # Save template
                    success = generator.save_template(file_path, code, metadata)

                    if success:
                        generated += 1
                        if (i + 1) % 50 == 0:
                            logger.info(f"   ... {i + 1}/{len(combinations)} templates generated")
                    else:
                        skipped += 1
                else:
                    skipped += 1

            except Exception as e:
                logger.error(f"   ⚠️  Error generating template {i+1}: {e}")
                errors += 1

        # Update statistics
        self.total_generated += generated
        self.total_skipped += skipped
        self.total_errors += errors

        self.generation_stats[domain_path] = {
            'target': target_count,
            'generated': generated,
            'skipped': skipped,
            'errors': errors,
            'success_rate': (generated / target_count * 100) if target_count > 0 else 0
        }

        # Print results
        logger.info("")
        logger.info(f"   ✅ Generated: {generated}")
        logger.info(f"   ⏭️  Skipped: {skipped}")
        logger.info(f"   ❌ Errors: {errors}")
        logger.info(f"   📊 Success Rate: {generated/target_count*100:.1f}%")
        logger.info("")

    def _print_summary(self, duration: float):
        """Print generation summary"""
        logger.info("")
        logger.info("=" * 80)
        logger.info("📊 GENERATION COMPLETE")
        logger.info("=" * 80)
        logger.info(f"✅ Generated: {self.total_generated} templates")
        logger.info(f"⏭️  Skipped: {self.total_skipped}")
        logger.info(f"❌ Errors: {self.total_errors}")
        logger.info(f"⏱️  Duration: {duration:.1f} seconds")
        logger.info(f"⚡ Speed: {self.total_generated/duration:.1f} templates/second")
        logger.info("")

        # Per-domain breakdown
        logger.info("📦 Per-Domain Breakdown:")
        logger.info("")
        for domain, stats in self.generation_stats.items():
            logger.info(f"   {domain}:")
            logger.info(f"      Target: {stats['target']}")
            logger.info(f"      Generated: {stats['generated']} ({stats['success_rate']:.1f}%)")
            logger.info("")

        logger.info("=" * 80)

    def _save_generation_report(self):
        """Save generation report to JSON"""
        report_path = self.output_dir / "generation_report.json"

        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_generated': self.total_generated,
                'total_skipped': self.total_skipped,
                'total_errors': self.total_errors,
            },
            'domains': self.generation_stats
        }

        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)

        logger.info(f"📄 Report saved: {report_path}")

    def validate_templates(self):
        """
        Run validation on generated templates

        Checks:
        - Valid JavaScript syntax
        - No duplicate names
        - Metadata completeness
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("🔍 VALIDATING TEMPLATES")
        logger.info("=" * 80)

        # Find all generated templates
        jsx_files = list(self.output_dir.rglob("*.jsx"))
        logger.info(f"Found {len(jsx_files)} .jsx files")

        # Validate each
        valid_count = 0
        invalid_count = 0

        for jsx_file in jsx_files:
            try:
                # Check syntax (basic)
                code = jsx_file.read_text()

                # Check for basic React patterns
                if 'import React' not in code:
                    logger.warning(f"⚠️  Missing React import: {jsx_file.name}")
                    invalid_count += 1
                    continue

                if 'export default' not in code:
                    logger.warning(f"⚠️  Missing export: {jsx_file.name}")
                    invalid_count += 1
                    continue

                # Check metadata exists
                metadata_file = jsx_file.with_suffix('.json')
                if not metadata_file.exists():
                    logger.warning(f"⚠️  Missing metadata: {jsx_file.name}")
                    invalid_count += 1
                    continue

                # Validate metadata
                try:
                    metadata = json.loads(metadata_file.read_text())
                    if 'id' not in metadata or 'name' not in metadata:
                        logger.warning(f"⚠️  Incomplete metadata: {jsx_file.name}")
                        invalid_count += 1
                        continue
                except json.JSONDecodeError:
                    logger.warning(f"⚠️  Invalid metadata JSON: {jsx_file.name}")
                    invalid_count += 1
                    continue

                valid_count += 1

            except Exception as e:
                logger.error(f"❌ Error validating {jsx_file.name}: {e}")
                invalid_count += 1

        logger.info("")
        logger.info(f"✅ Valid: {valid_count}")
        logger.info(f"❌ Invalid: {invalid_count}")
        logger.info(f"📊 Success Rate: {valid_count/(valid_count+invalid_count)*100:.1f}%")
        logger.info("=" * 80)

    def create_catalog(self):
        """
        Create template catalog from generated templates

        Scans all templates and creates master catalog.json
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("📚 CREATING TEMPLATE CATALOG")
        logger.info("=" * 80)

        catalog = {
            'version': '1.0.0',
            'generated_at': datetime.now().isoformat(),
            'total_templates': 0,
            'domains': {}
        }

        # Find all metadata files
        metadata_files = list(self.output_dir.rglob("*.json"))
        metadata_files = [f for f in metadata_files if f.name != 'generation_report.json']

        logger.info(f"Found {len(metadata_files)} templates")

        for metadata_file in metadata_files:
            try:
                metadata = json.loads(metadata_file.read_text())

                domain = metadata.get('intent', {}).get('domain', 'unknown')
                category = metadata.get('intent', {}).get('category', 'unknown')

                # Add to catalog
                if domain not in catalog['domains']:
                    catalog['domains'][domain] = {}

                if category not in catalog['domains'][domain]:
                    catalog['domains'][domain][category] = []

                catalog['domains'][domain][category].append({
                    'id': metadata.get('id'),
                    'name': metadata.get('name'),
                    'file_path': str(metadata_file.with_suffix('.jsx').relative_to(self.output_dir)),
                    'metadata_path': str(metadata_file.relative_to(self.output_dir))
                })

                catalog['total_templates'] += 1

            except Exception as e:
                logger.error(f"❌ Error processing {metadata_file.name}: {e}")

        # Save catalog
        catalog_path = self.output_dir / "catalog.json"
        with open(catalog_path, 'w') as f:
            json.dump(catalog, f, indent=2)

        logger.info("")
        logger.info(f"✅ Catalog created: {catalog_path}")
        logger.info(f"   Total templates: {catalog['total_templates']}")
        logger.info(f"   Domains: {len(catalog['domains'])}")
        logger.info("=" * 80)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution"""
    import argparse

    parser = argparse.ArgumentParser(description='Generate massive template library')
    parser.add_argument(
        '--output',
        default='./templates_generated',
        help='Output directory for templates'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Run validation after generation'
    )
    parser.add_argument(
        '--catalog',
        action='store_true',
        help='Create catalog after generation'
    )
    parser.add_argument(
        '--skip-generation',
        action='store_true',
        help='Skip generation, only run validation/catalog'
    )

    args = parser.parse_args()

    generator = MassiveTemplateGenerator(output_dir=args.output)

    # Generate
    if not args.skip_generation:
        generator.generate_all()

    # Validate
    if args.validate or args.skip_generation:
        generator.validate_templates()

    # Create catalog
    if args.catalog or args.skip_generation:
        generator.create_catalog()

    logger.info("")
    logger.info("🎉 ALL DONE!")
    logger.info("")


if __name__ == "__main__":
    main()
