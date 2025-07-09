# 🚀 Creating Your First AI Agent

Welcome! This guide will help you build your very first AI agent from scratch. Just follow the steps below. Each step has simple commands and a short explanation. Enjoy the ride! 🥰

---

## 1️⃣ Install UV

UV is a command-line tool we'll use to manage the environment.

```bash
pip install uv-cli
```

---

## 2️⃣ Create Folder

Create a new folder where your agent code will live.

```bash
mkdir creating-First-AI-Agent
cd creating-First-AI-Agent
```

---

## 3️⃣ Create Virtual Environment

We use a virtual environment to keep things clean.

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\Activate.ps1
```

---

## 4️⃣ Install Python Env Package

Install required Python packages:

```bash
pip install python-dotenv openai
```

Then save them to requirements:

```bash
pip freeze > requirements.txt
```

---

## 5️⃣ Create API Key

Go to https://platform.openai.com/account/api-keys  
Login and click "Create API Key"  
Copy your key for later use.

---

## 6️⃣ Apply API Key in `.env`

Create a `.env` file in your project folder and add:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Also, make sure `.env` is listed in your `.gitignore` so it's never pushed to GitHub.

---

## 7️⃣ Install OpenAI Agent

Install the OpenAI SDK if not already installed:

```bash
pip install openai
```

---

## 8️⃣ Create Your First Agent

Create a file called `main.py` and add this code:

```python
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
```

---

## 9️⃣ Connection With Your LLM

Add this to your `main.py` file:

```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello Agent!"}
  ]
)

print(response.choices[0].message.content)
```

---

## 🔟 Execute / Run the Agent

Run your agent using this command:

```bash
python main.py
```

You should see the agent's response in your terminal 🎉

---

## 🗂 Project Structure

Your folder should look like this:

```
creating-First-AI-Agent/
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── .venv/
```

---

Made with ❤️ by [@aimanshahid800](https://github.com/aimanshahid800)

