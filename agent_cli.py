#!/usr/bin/env python
"""
Excel Ingestion Agent - Standalone CLI Tool
Processes Excel files and generates canonical test case JSON
"""

import sys
import argparse
import json
from pathlib import Path

from src.agent import ExcelIngestionAgent


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Excel Ingestion Agent - Parse Excel files and normalize test cases to JSON',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python agent_cli.py input.xlsx
  python agent_cli.py input.xlsx -o ./results
  python agent_cli.py input.xlsx --output ./results --pretty
        """
    )
    
    parser.add_argument(
        'excel_file',
        help='Path to the Excel file to process'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='output',
        help='Output directory for JSON files (default: output)'
    )
    
    parser.add_argument(
        '-p', '--pretty',
        action='store_true',
        help='Pretty print JSON output'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    # Validate input file
    excel_file = Path(args.excel_file)
    if not excel_file.exists():
        print(f"ERROR: File not found: {args.excel_file}", file=sys.stderr)
        sys.exit(1)
    
    if not excel_file.suffix.lower() in ['.xlsx', '.xls']:
        print(f"ERROR: File must be .xlsx or .xls format", file=sys.stderr)
        sys.exit(1)
    
    # Create agent
    agent = ExcelIngestionAgent(output_dir=args.output)
    
    # Process file
    if args.verbose:
        print(f"Processing: {excel_file}")
    
    result = agent.process_file(str(excel_file))
    
    # Handle result
    if result['status'] == 'success':
        print(f"\n✓ SUCCESS")
        print(f"  Message: {result['message']}")
        print(f"  Output file: {result['output_file']}")
        print(f"  Test cases: {result['test_cases_count']}")
        
        # Print JSON if requested
        if args.pretty:
            print(f"\n  JSON Output:")
            test_cases = result.get('test_cases', [])
            print(json.dumps(test_cases, indent=2))
        
        sys.exit(0)
    else:
        print(f"✗ ERROR: {result['message']}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
