"""Main agent for orchestrating Excel parsing and test case normalization."""
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

from src.parser import ExcelParser
from src.normalizer import TestCaseNormalizer
from src.models import TestCase


class ExcelIngestionAgent:
    """Main agent for processing Excel files and generating canonical test case JSON."""
    
    def __init__(self, output_dir: str = "output"):
        """Initialize the agent."""
        self.parser = None
        self.normalizer = TestCaseNormalizer()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def process_file(self, file_path: str) -> Dict[str, Any]:
        """
        Process Excel file and generate canonical test case JSON.
        
        Args:
            file_path: Path to the Excel file to process
            
        Returns:
            Dictionary containing processing results
        """
        try:
            # Parse Excel file
            self.parser = ExcelParser(file_path)
            parsed_data = self.parser.parse()
            
            if not parsed_data:
                return {
                    'status': 'error',
                    'message': 'No valid test cases found in Excel file'
                }
            
            # Normalize to canonical format
            normalized_cases = self.normalizer.normalize(parsed_data)
            
            if not normalized_cases:
                return {
                    'status': 'error',
                    'message': 'Failed to normalize test cases'
                }
            
            # Generate output JSON
            output_file = self._save_to_json(normalized_cases, file_path)
            
            return {
                'status': 'success',
                'message': f'Successfully processed {len(normalized_cases)} test cases',
                'test_cases_count': len(normalized_cases),
                'output_file': str(output_file),
                'test_cases': [tc.to_dict() for tc in normalized_cases]
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Error processing file: {str(e)}'
            }
    
    def _save_to_json(self, test_cases: List[TestCase], source_file: str) -> Path:
        """Save normalized test cases to JSON file."""
        # Generate output filename
        source_name = Path(source_file).stem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{source_name}_canonical_{timestamp}.json"
        output_path = self.output_dir / output_filename
        
        # Prepare JSON data
        output_data = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'source_file': source_file,
                'test_cases_count': len(test_cases)
            },
            'test_cases': [tc.to_dict() for tc in test_cases]
        }
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        return output_path
    
    def get_test_cases_dict(self, test_cases: List[TestCase]) -> Dict[str, Any]:
        """Convert test cases to dictionary format."""
        return {
            'test_cases': [tc.to_dict() for tc in test_cases]
        }
