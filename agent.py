"""AI Agent Framework - Core Module

A modular framework for building AI agents with plugin support,
task automation, and conversational capabilities.
"""

import json
import importlib
import os
from typing import Dict, List, Any, Optional
from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Abstract base class for all agents."""
    
    def __init__(self, name: str, config: Optional[Dict] = None):
        self.name = name
        self.config = config or {}
        self.plugins = {}
        self.memory = []
        self.context = {}
    
    @abstractmethod
    def process(self, input_data: Any) -> Any:
        """Process input and return output."""
        pass
    
    def load_plugin(self, plugin_name: str, plugin_path: str = "plugins"):
        """Dynamically load a plugin."""
        try:
            module_name = f"{plugin_path}.{plugin_name}"
            module = importlib.import_module(module_name)
            plugin_class = getattr(module, f"{plugin_name.title().replace('_', '')}Plugin")
            self.plugins[plugin_name] = plugin_class()
            print(f"✓ Plugin '{plugin_name}' loaded successfully")
            return True
        except Exception as e:
            print(f"✗ Failed to load plugin '{plugin_name}': {e}")
            return False
    
    def execute_plugin(self, plugin_name: str, *args, **kwargs):
        """Execute a loaded plugin."""
        if plugin_name in self.plugins:
            return self.plugins[plugin_name].execute(*args, **kwargs)
        else:
            raise ValueError(f"Plugin '{plugin_name}' not loaded")
    
    def add_to_memory(self, entry: Dict):
        """Add an entry to agent's memory."""
        self.memory.append(entry)
        if len(self.memory) > self.config.get('max_memory', 100):
            self.memory.pop(0)
    
    def get_memory(self, limit: int = 10) -> List[Dict]:
        """Retrieve recent memory entries."""
        return self.memory[-limit:]


class ConversationalAgent(BaseAgent):
    """Agent specialized for conversational interactions."""
    
    def __init__(self, name: str = "ConversationalAgent", config: Optional[Dict] = None):
        super().__init__(name, config)
        self.conversation_history = []
    
    def process(self, user_input: str) -> str:
        """Process user input and generate response."""
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Simple rule-based response (can be extended with LLM integration)
        response = self._generate_response(user_input)
        
        self.conversation_history.append({"role": "assistant", "content": response})
        self.add_to_memory({"user": user_input, "assistant": response})
        
        return response
    
    def _generate_response(self, user_input: str) -> str:
        """Generate response based on input."""
        user_input_lower = user_input.lower()
        
        # Check if plugins can handle this
        if "search" in user_input_lower and "web_search" in self.plugins:
            query = user_input.replace("search", "").strip()
            return self.execute_plugin("web_search", query)
        
        if "calculate" in user_input_lower and "calculator" in self.plugins:
            return self.execute_plugin("calculator", user_input)
        
        # Default responses
        greetings = ["hello", "hi", "hey", "greetings"]
        if any(g in user_input_lower for g in greetings):
            return f"Hello! I'm {self.name}. How can I assist you today?"
        
        return "I understand. How else can I help you?"


class TaskAgent(BaseAgent):
    """Agent specialized for task execution and automation."""
    
    def __init__(self, name: str = "TaskAgent", config: Optional[Dict] = None):
        super().__init__(name, config)
        self.task_queue = []
        self.completed_tasks = []
    
    def process(self, task: Dict) -> Dict:
        """Process a task."""
        task_type = task.get("type")
        task_data = task.get("data")
        
        result = {"task": task, "status": "pending", "result": None}
        
        try:
            if task_type in self.plugins:
                result["result"] = self.execute_plugin(task_type, task_data)
                result["status"] = "completed"
            else:
                result["status"] = "failed"
                result["error"] = f"No plugin for task type '{task_type}'"
        except Exception as e:
            result["status"] = "failed"
            result["error"] = str(e)
        
        self.completed_tasks.append(result)
        return result
    
    def add_task(self, task: Dict):
        """Add task to queue."""
        self.task_queue.append(task)
    
    def process_queue(self) -> List[Dict]:
        """Process all tasks in queue."""
        results = []
        while self.task_queue:
            task = self.task_queue.pop(0)
            results.append(self.process(task))
        return results


class RetrievalAgent(BaseAgent):
    """Agent specialized for information retrieval and RAG."""
    
    def __init__(self, name: str = "RetrievalAgent", config: Optional[Dict] = None):
        super().__init__(name, config)
        self.knowledge_base = []
    
    def process(self, query: str) -> Dict:
        """Process retrieval query."""
        # Simple keyword-based retrieval
        results = self._retrieve(query)
        
        response = {
            "query": query,
            "results": results,
            "count": len(results)
        }
        
        self.add_to_memory(response)
        return response
    
    def _retrieve(self, query: str) -> List[Dict]:
        """Retrieve relevant documents."""
        query_lower = query.lower()
        results = []
        
        for doc in self.knowledge_base:
            if any(word in doc.get("content", "").lower() for word in query_lower.split()):
                results.append(doc)
        
        return results
    
    def add_document(self, document: Dict):
        """Add document to knowledge base."""
        self.knowledge_base.append(document)
    
    def load_documents(self, documents: List[Dict]):
        """Load multiple documents."""
        self.knowledge_base.extend(documents)


def create_agent(agent_type: str = "conversational", **kwargs) -> BaseAgent:
    """Factory function to create agents."""
    agent_types = {
        "conversational": ConversationalAgent,
        "task": TaskAgent,
        "retrieval": RetrievalAgent
    }
    
    agent_class = agent_types.get(agent_type.lower())
    if not agent_class:
        raise ValueError(f"Unknown agent type: {agent_type}")
    
    return agent_class(**kwargs)


if __name__ == "__main__":
    # Example usage
    print("AI Agent Framework - Core Module")
    print("=" * 40)
    
    # Create a conversational agent
    agent = create_agent("conversational", name="MyAgent")
    print(f"Created agent: {agent.name}")
    
    # Test conversation
    response = agent.process("Hello!")
    print(f"Agent: {response}")
