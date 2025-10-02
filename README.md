# 🤖 AI Agent Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A modular Python framework for building AI agents with plugin support, task automation, and conversational capabilities.

## ✨ Features

- **Modular Agent Architecture**: Base agent class with specialized subtypes (Conversational, Task, Retrieval)
- **Plugin System**: Extensible plugin architecture for adding new tools and capabilities
- **Built-in Plugins**: Web search, calculator, calendar, email, file operations, and more
- **Memory Management**: Conversation history and context tracking
- **Easy Extension**: Simple template for adding new skills and capabilities
- **Demo Runners**: CLI and Flask web interface for testing
- **Type Hints**: Full type annotation support for better IDE integration

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/rahit91890/ai-agent-framework.git
cd ai-agent-framework

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Quick Start

### Basic Usage

```python
from agent import create_agent

# Create a conversational agent
agent = create_agent("conversational", name="MyAssistant")

# Have a conversation
response = agent.process("Hello!")
print(response)  # "Hello! I'm MyAssistant. How can I assist you today?"
```

### Using Plugins

```python
from agent import create_agent

# Create an agent
agent = create_agent("conversational")

# Load plugins
agent.load_plugin("web_search")
agent.load_plugin("calculator")

# Use plugin functionality
result = agent.process("search for AI news")
```

### Task Agent

```python
from agent import create_agent

# Create a task agent
agent = create_agent("task", name="TaskBot")

# Load task plugins
agent.load_plugin("file")
agent.load_plugin("email")

# Add and process tasks
agent.add_task({"type": "file", "data": {"action": "read", "path": "data.txt"}})
results = agent.process_queue()
```

### Retrieval Agent (RAG)

```python
from agent import create_agent

# Create a retrieval agent
agent = create_agent("retrieval", name="RAGAgent")

# Add documents to knowledge base
agent.add_document({"id": 1, "content": "Python is a programming language"})
agent.add_document({"id": 2, "content": "AI agents can automate tasks"})

# Query the knowledge base
result = agent.process("What is Python?")
print(result)
```

## 🔌 Built-in Plugins

The framework comes with several pre-built plugins:

### 1. Web Search Plugin
```python
agent.load_plugin("web_search")
result = agent.execute_plugin("web_search", "AI trends 2025")
```

### 2. Calculator Plugin
```python
agent.load_plugin("calculator")
result = agent.execute_plugin("calculator", "2 + 2 * 3")
```

### 3. Calendar Plugin
```python
agent.load_plugin("calendar")
result = agent.execute_plugin("calendar", {"action": "add_event", "title": "Meeting"})
```

### 4. Email Plugin
```python
agent.load_plugin("email")
result = agent.execute_plugin("email", {"action": "send", "to": "user@example.com"})
```

### 5. File Plugin
```python
agent.load_plugin("file")
result = agent.execute_plugin("file", {"action": "read", "path": "data.txt"})
```

## 🛠️ Creating Custom Plugins

Create a new plugin by extending the `BasePlugin` class:

```python
# plugins/my_plugin.py
from plugins import BasePlugin

class MypluginPlugin(BasePlugin):
    def __init__(self):
        super().__init__()
        self.description = "My custom plugin"
    
    def execute(self, *args, **kwargs):
        # Your plugin logic here
        return "Plugin executed!"
    
    def validate(self, *args, **kwargs):
        # Validation logic
        return True
```

Then load it in your agent:

```python
agent.load_plugin("my_plugin")
result = agent.execute_plugin("my_plugin", data)
```

## 📁 Project Structure

```
ai-agent-framework/
├── agent.py                 # Core agent framework
├── plugins/                 # Plugin directory
│   ├── __init__.py         # Plugin base class
│   ├── web_search.py       # Web search plugin
│   ├── calculator.py       # Calculator plugin
│   ├── calendar.py         # Calendar plugin
│   ├── email.py            # Email plugin
│   └── file.py             # File operations plugin
├── examples/               # Example usage scripts
│   ├── cli_demo.py        # CLI demo runner
│   ├── web_demo.py        # Flask web demo
│   ├── conversational_example.py
│   ├── task_example.py
│   └── retrieval_example.py
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── LICENSE                # MIT License
```

## 🎯 Examples

### CLI Demo

```bash
python examples/cli_demo.py
```

Interactive command-line interface for testing agents.

### Web Demo

```bash
python examples/web_demo.py
```

Visit `http://localhost:5000` for a web-based interface.

## 🔧 Configuration

Agents can be configured with custom parameters:

```python
config = {
    "max_memory": 100,          # Maximum memory entries
    "temperature": 0.7,         # Response creativity (future LLM integration)
    "debug": True               # Enable debug mode
}

agent = create_agent("conversational", name="MyAgent", config=config)
```

## 🧪 Running Tests

```bash
# Run example scripts
python examples/conversational_example.py
python examples/task_example.py
python examples/retrieval_example.py
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Requirements

```txt
Python >= 3.8
requests >= 2.28.0
flask >= 2.3.0
```

## 🚀 Roadmap

- [ ] LLM Integration (OpenAI, Anthropic, local models)
- [ ] Vector database support for RAG
- [ ] Multi-agent collaboration
- [ ] Streaming responses
- [ ] Advanced planning and reasoning
- [ ] Web UI dashboard
- [ ] Docker containerization
- [ ] CI/CD pipeline

## 📚 Documentation

### Agent Types

#### ConversationalAgent
Specialized for natural language conversations with memory and context tracking.

#### TaskAgent
Designed for executing and queuing tasks with plugin integration.

#### RetrievalAgent
Optimized for information retrieval and RAG (Retrieval Augmented Generation) patterns.

### Core Methods

- `process(input_data)`: Process input and return output
- `load_plugin(plugin_name)`: Load a plugin dynamically
- `execute_plugin(plugin_name, *args, **kwargs)`: Execute a loaded plugin
- `add_to_memory(entry)`: Add entry to agent memory
- `get_memory(limit)`: Retrieve recent memory entries

## 🔐 Security

This framework is designed for development and educational purposes. For production use:

- Implement proper authentication and authorization
- Sanitize all user inputs
- Use environment variables for sensitive data
- Implement rate limiting
- Add input validation for all plugins

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Rahit Biswas**
- GitHub: [@rahit91890](https://github.com/rahit91890)
- Website: [codaphics.com](https://codaphics.com)
- LinkedIn: [Rahit Biswas](https://www.linkedin.com/in/rahit-biswas-786939153)

## 🙏 Acknowledgments

- Inspired by modern AI agent frameworks
- Built for the developer community
- Special thanks to all contributors

## 📞 Support

For questions and support:
- Open an issue on GitHub
- Email: r.codaphics@gmail.com
- Twitter: [@Rahit1996](https://x.com/Rahit1996)

---

⭐ If you find this project useful, please consider giving it a star!

Made with ❤️ by Rahit Biswas | Codaphics
