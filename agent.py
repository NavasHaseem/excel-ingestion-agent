#!/usr/bin/env python
"""
Excel Ingestion Agent - Direct Python API
Use this for programmatic access to the agent
"""

from src.agent import ExcelIngestionAgent
from src.parser import ExcelParser
from src.normalizer import TestCaseNormalizer
from src.models import TestCase, TestStep, PriorityEnum, StatusEnum
import json


def process_excel_file(file_path: str, output_dir: str = 'output') -> dict:
    """
    Process an Excel file and return the result.
    
    Args:
        file_path: Path to the Excel file
        output_dir: Directory to save JSON output
        
    Returns:
        Dictionary with status, message, and test cases
        
    Example:
        result = process_excel_file('test_cases.xlsx')
        if result['status'] == 'success':
            print(f"Processed {result['test_cases_count']} test cases")
            print(json.dumps(result['test_cases'], indent=2))
    """
    agent = ExcelIngestionAgent(output_dir=output_dir)
    return agent.process_file(file_path)


def get_test_cases(file_path: str) -> list:
    """
    Get parsed test cases from Excel file.
    
    Args:
        file_path: Path to the Excel file
        
    Returns:
        List of TestCase objects
    """
    parser = ExcelParser(file_path)
    parsed_data = parser.parse()
    
    normalizer = TestCaseNormalizer()
    return normalizer.normalize(parsed_data)


if __name__ == '__main__':
    # Example usage
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agent.py <excel_file> [output_dir]")
        print("\nExample:")
        print("  python agent.py test_cases.xlsx")
        print("  python agent.py test_cases.xlsx ./results")
        sys.exit(1)
    
    excel_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else 'output'
    
    result = process_excel_file(excel_file, output_dir)
    
    print(json.dumps(result, indent=2, default=str))
