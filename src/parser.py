"""Excel file parser for test cases."""
import pandas as pd
from typing import List, Dict, Any
from pathlib import Path


class ExcelParser:
    """Parser for Excel files containing test cases."""
    
    def __init__(self, file_path: str):
        """Initialize parser with file path."""
        self.file_path = file_path
        self.df = None
        
    def parse(self) -> List[Dict[str, Any]]:
        """
        Parse Excel file and extract test case data.
        
        Expected columns: id, title, description, preconditions, steps, 
                         expected_result, priority, status, tags, module
        """
        try:
            self.df = pd.read_excel(self.file_path)
            return self._extract_test_cases()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")
        except Exception as e:
            raise Exception(f"Error parsing Excel file: {str(e)}")
    
    def _extract_test_cases(self) -> List[Dict[str, Any]]:
        """Extract test cases from parsed dataframe."""
        test_cases = []
        
        for idx, row in self.df.iterrows():
            test_case = self._row_to_test_case(row)
            if test_case:
                test_cases.append(test_case)
        
        return test_cases
    
    def _row_to_test_case(self, row: pd.Series) -> Dict[str, Any]:
        """Convert Excel row to test case dictionary."""
        try:
            # Map column names - support both formats
            id_val = row.get('Test Case ID') or row.get('id') or row.get('ID')
            title_val = row.get('Description') or row.get('title')
            description_val = row.get('Description') or row.get('description')
            
            # Extract and clean data
            test_case = {
                'id': self._clean_value(id_val),
                'title': self._clean_value(title_val),
                'description': self._clean_value(description_val),
                'preconditions': self._clean_value(row.get('Preconditions') or row.get('preconditions', '')),
                'steps': self._parse_steps(row.get('Steps') or row.get('steps', '')),
                'expected_result': self._clean_value(row.get('Expected Result') or row.get('expected_result', '')),
                'priority': self._normalize_priority(row.get('Priority') or row.get('priority', 'medium')),
                'status': self._normalize_status(row.get('Status') or row.get('status', 'active')),
                'tags': self._parse_tags(row.get('Tags') or row.get('tags', '')),
                'module': self._clean_value(row.get('Module') or row.get('module', None)),
                'created_date': self._clean_value(row.get('Created Date') or row.get('created_date', None)),
                'last_modified': self._clean_value(row.get('Last Modified') or row.get('last_modified', None)),
            }
            
            # Validate required fields
            if test_case['id'] and test_case['title']:
                return test_case
            return None
            
        except Exception as e:
            print(f"Error processing row {row.get('Test Case ID', row.get('id', 'unknown'))}: {str(e)}")
            return None
    
    @staticmethod
    def _clean_value(value: Any) -> str:
        """Clean and normalize string values."""
        if pd.isna(value):
            return ""
        return str(value).strip()
    
    @staticmethod
    def _parse_steps(steps_str: str) -> List[Dict[str, Any]]:
        """Parse steps from string format."""
        if not steps_str or pd.isna(steps_str):
            return []
        
        steps = []
        steps_str = str(steps_str).strip()
        
        # Handle newline-separated steps
        step_lines = steps_str.split('\n')
        for i, line in enumerate(step_lines, 1):
            line = line.strip()
            if line:
                # Simple format: action | expected_result
                if '|' in line:
                    parts = line.split('|')
                    steps.append({
                        'step_number': i,
                        'action': parts[0].strip(),
                        'expected_result': parts[1].strip() if len(parts) > 1 else ''
                    })
                else:
                    steps.append({
                        'step_number': i,
                        'action': line,
                        'expected_result': ''
                    })
        
        return steps
    
    @staticmethod
    def _parse_tags(tags_str: str) -> List[str]:
        """Parse tags from comma-separated string."""
        if not tags_str or pd.isna(tags_str):
            return []
        
        tags = str(tags_str).split(',')
        return [tag.strip() for tag in tags if tag.strip()]
    
    @staticmethod
    def _normalize_priority(priority: str) -> str:
        """Normalize priority value."""
        if pd.isna(priority):
            return "medium"
        
        priority_lower = str(priority).lower().strip()
        valid_priorities = ['critical', 'high', 'medium', 'low']
        
        if priority_lower in valid_priorities:
            return priority_lower
        return "medium"
    
    @staticmethod
    def _normalize_status(status: str) -> str:
        """Normalize status value."""
        if pd.isna(status):
            return "active"
        
        status_lower = str(status).lower().strip()
        valid_statuses = ['active', 'deprecated', 'draft']
        
        if status_lower in valid_statuses:
            return status_lower
        return "active"
