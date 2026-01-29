"""Data models for test cases."""
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional
from enum import Enum


class PriorityEnum(str, Enum):
    """Priority levels for test cases."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class StatusEnum(str, Enum):
    """Status of test cases."""
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    DRAFT = "draft"


@dataclass
class TestStep:
    """Represents a single test step."""
    step_number: int
    action: str
    expected_result: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


@dataclass
class TestCase:
    """Canonical test case model."""
    id: str
    title: str
    description: str
    preconditions: str
    steps: List[TestStep]
    expected_result: str
    priority: PriorityEnum
    status: StatusEnum
    tags: List[str]
    module: Optional[str] = None
    created_date: Optional[str] = None
    last_modified: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        data = asdict(self)
        data['steps'] = [step.to_dict() if isinstance(step, TestStep) else step for step in self.steps]
        data['priority'] = self.priority.value
        data['status'] = self.status.value
        return data
