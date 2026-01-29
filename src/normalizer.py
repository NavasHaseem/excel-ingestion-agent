"""Test case normalizer for converting parsed data to canonical format."""
from typing import List, Dict, Any
from src.models import TestCase, TestStep, PriorityEnum, StatusEnum


class TestCaseNormalizer:
    """Normalizes parsed test case data into canonical format."""
    
    def __init__(self):
        """Initialize normalizer."""
        pass
    
    def normalize(self, parsed_data: List[Dict[str, Any]]) -> List[TestCase]:
        """
        Normalize parsed test case data into canonical TestCase objects.
        
        Args:
            parsed_data: List of dictionaries from ExcelParser
            
        Returns:
            List of normalized TestCase objects
        """
        normalized_cases = []
        
        for i, case_data in enumerate(parsed_data):
            try:
                test_case = self._normalize_single(case_data)
                normalized_cases.append(test_case)
            except Exception as e:
                print(f"Error normalizing test case {i}: {str(e)}")
                continue
        
        return normalized_cases
    
    def _normalize_single(self, case_data: Dict[str, Any]) -> TestCase:
        """Normalize a single test case."""
        # Parse steps
        steps = []
        if case_data.get('steps'):
            for step_data in case_data['steps']:
                step = TestStep(
                    step_number=step_data.get('step_number', 0),
                    action=step_data.get('action', ''),
                    expected_result=step_data.get('expected_result', '')
                )
                steps.append(step)
        
        # Create canonical test case
        test_case = TestCase(
            id=case_data.get('id', ''),
            title=case_data.get('title', ''),
            description=case_data.get('description', ''),
            preconditions=case_data.get('preconditions', ''),
            steps=steps,
            expected_result=case_data.get('expected_result', ''),
            priority=PriorityEnum(case_data.get('priority', 'medium')),
            status=StatusEnum(case_data.get('status', 'active')),
            tags=case_data.get('tags', []),
            module=case_data.get('module', None),
            created_date=case_data.get('created_date', None),
            last_modified=case_data.get('last_modified', None),
        )
        
        return test_case
