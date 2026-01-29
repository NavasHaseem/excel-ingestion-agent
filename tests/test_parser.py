"""Tests for Excel parser."""
import unittest
import tempfile
import os
from pathlib import Path

import pandas as pd

from src.parser import ExcelParser


class TestExcelParser(unittest.TestCase):
    """Test cases for ExcelParser."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_data = {
            'id': ['TC-001', 'TC-002'],
            'title': ['Test 1', 'Test 2'],
            'description': ['Description 1', 'Description 2'],
            'preconditions': ['Precond 1', 'Precond 2'],
            'steps': ['Step 1 | Result 1', 'Step 2 | Result 2'],
            'expected_result': ['Expected 1', 'Expected 2'],
            'priority': ['high', 'medium'],
            'status': ['active', 'draft'],
            'tags': ['tag1,tag2', 'tag3'],
            'module': ['Module1', 'Module2']
        }
    
    def test_parse_valid_excel(self):
        """Test parsing a valid Excel file."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test Excel file
            file_path = os.path.join(temp_dir, 'test.xlsx')
            df = pd.DataFrame(self.test_data)
            df.to_excel(file_path, index=False)
            
            # Parse file
            parser = ExcelParser(file_path)
            result = parser.parse()
            
            # Assertions
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0]['id'], 'TC-001')
            self.assertEqual(result[0]['title'], 'Test 1')
    
    def test_parse_nonexistent_file(self):
        """Test parsing nonexistent file."""
        parser = ExcelParser('/nonexistent/file.xlsx')
        
        with self.assertRaises(FileNotFoundError):
            parser.parse()
    
    def test_normalize_priority(self):
        """Test priority normalization."""
        parser = ExcelParser('')
        
        self.assertEqual(parser._normalize_priority('HIGH'), 'high')
        self.assertEqual(parser._normalize_priority('Invalid'), 'medium')
        self.assertEqual(parser._normalize_priority(None), 'medium')
    
    def test_normalize_status(self):
        """Test status normalization."""
        parser = ExcelParser('')
        
        self.assertEqual(parser._normalize_status('ACTIVE'), 'active')
        self.assertEqual(parser._normalize_status('Invalid'), 'active')
        self.assertEqual(parser._normalize_status(None), 'active')
    
    def test_parse_steps(self):
        """Test step parsing."""
        parser = ExcelParser('')
        
        steps_text = "Click button | Button clicked\nVerify result | Result visible"
        result = parser._parse_steps(steps_text)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['step_number'], 1)
        self.assertEqual(result[0]['action'], 'Click button')
        self.assertEqual(result[0]['expected_result'], 'Button clicked')
    
    def test_parse_tags(self):
        """Test tag parsing."""
        parser = ExcelParser('')
        
        tags_text = "tag1, tag2, tag3"
        result = parser._parse_tags(tags_text)
        
        self.assertEqual(len(result), 3)
        self.assertIn('tag1', result)
        self.assertIn('tag2', result)


if __name__ == '__main__':
    unittest.main()
