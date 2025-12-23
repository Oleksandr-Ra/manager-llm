### Manager LLM Service
Python, FastAPI, Pydantic, Docker, OpenAI API, Groq

FastAPI-based service featuring a client manager to handle requests to multiple LLM APIs. Built with the Factory Design Pattern to ensure SOLID principles and easy extensibility.

#### How to use?
- Fork the repository.
- Initialize the project:
- git init
- git remote add origin https://github.com/your-name/manager-llm.git
- git branch -M main
- git pull origin main
- rename .env.example to .env
- change GROQ_API_KEY
- pip install uv (if not installed)
- uv sync
- docker-compose up -d