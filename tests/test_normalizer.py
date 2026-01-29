"""Tests for test case normalizer."""
import unittest

from src.normalizer import TestCaseNormalizer
from src.models import PriorityEnum, StatusEnum


class TestNormalizer(unittest.TestCase):
    """Test cases for TestCaseNormalizer."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.normalizer = TestCaseNormalizer()
        self.sample_data = {
            'id': 'TC-001',
            'title': 'Test Case 1',
            'description': 'Description',
            'preconditions': 'Preconditions',
            'steps': [
                {'step_number': 1, 'action': 'Action 1', 'expected_result': 'Result 1'},
                {'step_number': 2, 'action': 'Action 2', 'expected_result': 'Result 2'}
            ],
            'expected_result': 'Expected',
            'priority': 'high',
            'status': 'active',
            'tags': ['tag1', 'tag2'],
            'module': 'TestModule'
        }
    
    def test_normalize_single_testcase(self):
        """Test normalizing a single test case."""
        result = self.normalizer._normalize_single(self.sample_data)
        
        self.assertEqual(result.id, 'TC-001')
        self.assertEqual(result.title, 'Test Case 1')
        self.assertEqual(len(result.steps), 2)
        self.assertEqual(result.priority, PriorityEnum.HIGH)
        self.assertEqual(result.status, StatusEnum.ACTIVE)
    
    def test_normalize_multiple_testcases(self):
        """Test normalizing multiple test cases."""
        data = [self.sample_data, self.sample_data.copy()]
        result = self.normalizer.normalize(data)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, 'TC-001')
    
    def test_testcase_to_dict(self):
        """Test converting test case to dictionary."""
        test_case = self.normalizer._normalize_single(self.sample_data)
        result = test_case.to_dict()
        
        self.assertEqual(result['id'], 'TC-001')
        self.assertEqual(result['priority'], 'high')
        self.assertEqual(result['status'], 'active')
        self.assertEqual(len(result['steps']), 2)


if __name__ == '__main__':
    unittest.main()
