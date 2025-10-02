"""Plugin system for AI Agent Framework."""

from abc import ABC, abstractmethod
from typing import Any


class BasePlugin(ABC):
    """Base class for all plugins."""
    
    def __init__(self):
        self.name = self.__class__.__name__
        self.description = ""
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """Execute plugin functionality."""
        pass
    
    def validate(self, *args, **kwargs) -> bool:
        """Validate plugin inputs."""
        return True


__all__ = ['BasePlugin']
