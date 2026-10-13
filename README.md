# Gemini-Conversational-AI

A Python-based AI chatbot powered by Google's Gemini API that remembers previous conversations by saving and restoring chat history.

Unlike a basic chatbot that starts a fresh conversation every time, this project stores conversation history in a local JSON file and loads it when the program starts again. This helps the chatbot maintain conversational context across multiple sessions.

Built as a learning project while exploring **Artificial Intelligence, Generative AI, Large Language Models (LLMs), and Conversational AI**.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation Guide](#-installation-guide)
- [Google Gemini API Key Setup](#-google-gemini-api-key-setup)
- [Environment Configuration](#-environment-configuration)
- [How to Run](#-how-to-run)
- [Example Conversation](#-example-conversation)
- [Chat History and Memory](#-chat-history-and-memory)
- [Troubleshooting](#-troubleshooting)
- [Security and Privacy](#-security-and-privacy)
- [Future Improvements](#-future-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [Author](#-author)
- [License](#-license)

---

## 📖 Project Overview

The Gemini Memory Chatbot is a command-line AI chatbot developed using Python and Google's Gemini API.

Its main purpose is to provide an interactive AI conversation experience while preserving previous messages between program runs.

For example, a user can tell the chatbot their name and ask questions about Artificial Intelligence. When the chatbot is started again, it can restore the saved conversation and use the available context to respond more consistently.

### Why This Project?

Many basic chatbot programs lose their conversation history when they stop running.

This project explores a simple solution by saving conversation messages to a JSON file and restoring them when a new chat session starts.

It demonstrates how conversation history can be used to build more continuous and context-aware AI applications.

**Important:** The chatbot remembers information through saved conversation history. It does not currently implement a separate personal-memory database or independently extract permanent user profiles.

---

## ✨ Features

- 🤖 **Google Gemini Integration:** Generate AI responses using the Gemini API.
- 🧠 **Persistent Conversation History:** Save previous conversation messages locally.
- 🔄 **Session Restoration:** Load saved messages when restarting the chatbot.
- 💬 **Context-Aware Conversations:** Use previous messages as conversational context.
- 💾 **JSON Storage:** Store conversation history in a structured JSON file.
- 🔐 **Environment Variables:** Load the API key from a `.env` file instead of hardcoding it.
- 🛡️ **Error Handling:** Handle API errors and continue the conversation when possible.
- 🖥️ **Command-Line Interface:** Interact with the chatbot directly from a terminal.
- 🚪 **Exit Command:** Type `exit` to stop the chatbot.
- 🐍 **Python-Based Project:** Simple structure suitable for beginners learning AI development.

---

## ⚙️ How It Works

The chatbot follows a straightforward workflow:

1. Load the Gemini API key from the `.env` file.
2. Check whether a saved conversation history file exists.
3. Load the previous messages from `chat_history.json`.
4. Create a Gemini chat session using the restored history.
5. Accept a message from the user.
6. Send the message to the Gemini API.
7. Display the AI-generated response.
8. Save the updated conversation history to the JSON file.
9. Repeat until the user enters `exit`.

### Workflow Diagram

```text
             Start Chatbot
                   |
                   v
          Load API Key (.env)
                   |
                   v
       Load Previous Chat History
                   |
                   v
         Create Gemini Chat Session
                   |
                   v
            Enter User Message
                   |
                   v
          Send Message to Gemini
                   |
                   v
          Display AI Response
                   |
                   v
          Save History to JSON
                   |
                   v
          Continue Conversation
                   |
          Type "exit" to stop
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Google Gemini API | AI-generated responses |
| `google-genai` | Python SDK for Gemini |
| `python-dotenv` | Load environment variables |
| JSON | Store conversation history |
| `pathlib` | Manage file paths |
| `os` | Access environment variables |

---

## 📂 Project Structure

After setting up the project, your folder can look like this:

```text
gemini-memory-chatbot/
│
├── chatbot.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── chat_history.json
```

### File Explanation

**`chatbot.py`**

The main Python program that connects to Gemini, accepts user input, restores saved conversations, displays responses, and saves updated history.

**`requirements.txt`**

Contains the Python packages required to run the project.

**`.env`**

Stores your Gemini API key locally.

**`.gitignore`**

Prevents sensitive or personal files from being uploaded to GitHub.

**`README.md`**

Provides project documentation and setup instructions.

**`chat_history.json`**

Created when the program successfully saves a conversation. It stores the messages used to restore chat history.

The `.env`, `.gitignore`, and `requirements.txt` files must be created separately if they are not already present.

---

## 📋 Requirements

Before running the chatbot, make sure you have:

- Python 3.10 or a compatible version supported by the installed Google Gen AI SDK.
- A Google Gemini API key.
- An internet connection.
- A code editor such as Visual Studio Code or PyCharm, or another Python-compatible editor.
- A terminal or command prompt.

Python download: https://www.python.org/downloads/

Google AI Studio: https://aistudio.google.com/

---

## 🚀 Installation Guide

Follow these steps to set up the project from scratch.

### Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/gemini-memory-chatbot.git
```

Replace `YOUR-USERNAME` with your GitHub username.

Move into the project folder:

```bash
cd gemini-memory-chatbot
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

If the `code` command is available, you can run:

```bash
code .
```

You can also open the folder manually through your editor.

### Step 3: Create a Virtual Environment (Recommended)

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

A virtual environment keeps this project's dependencies separate from other Python projects.

### Step 4: Install Required Packages

Create a `requirements.txt` file containing:

```text
google-genai
python-dotenv
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Alternatively, install them directly:

```bash
python -m pip install google-genai python-dotenv
```

### Step 5: Configure the API Key

Create a file named `.env` in the same folder as `chatbot.py`.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

Replace `your_actual_api_key_here` with your own API key.

Do not add quotation marks unless specifically required by your configuration.

### Step 6: Run the Chatbot

Make sure the virtual environment is activated and run:

```bash
python chatbot.py
```

The chatbot should start in your terminal.

---

## 🔑 Google Gemini API Key Setup

The chatbot uses Google's Gemini API to generate responses.

Follow these steps:

1. Visit [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Open the API key section.
4. Create an API key if your account and region are eligible.
5. Copy the key.
6. Paste it into your local `.env` file.

Example:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

Keep your API key private. Never publish it in your source code, README, screenshots, or public GitHub repository.

API availability, model access, and usage limits depend on Google's current policies and your account.

---

## ▶️ How to Run

Once the dependencies and API key are configured, open a terminal inside the project directory.

Run:

```bash
python chatbot.py
```

You should see a startup message similar to:

```text
Gemini Chatbot Started!
Loaded 0 previous messages.
Type 'exit' to stop.

You:
```

The number of previous messages depends on the saved conversation history.

Type your question after `You:` and press Enter.

The chatbot will display the Gemini response.

To end the session, enter:

```text
exit
```

---

## 💬 Example Conversation

The following is an illustrative example of how the chatbot may be used.

```text
Gemini Chatbot Started!
Loaded 0 previous messages.
Type 'exit' to stop.

You: My name is Musab.

Gemini: Nice to meet you, Musab!

You: What is Artificial Intelligence?

Gemini: Artificial Intelligence is a field of
computer science that enables machines to
perform tasks that normally require human
intelligence.

You: What is a Large Language Model?

Gemini: A Large Language Model is an AI model
trained on large amounts of text to understand
and generate language.

You: exit

Chatbot stopped!
```

If the conversation is saved successfully, the program can load its history during the next run.

A later question such as "What is my name?" may be answered using the earlier message, provided the relevant context remains available to the model.

Actual responses depend on the model and the conversation.

---

## 🧠 Chat History and Memory

One of the main features of this project is persistent chat history.

### How Is Conversation History Saved?

The program uses Python's `json` module to save conversation messages in:

```text
chat_history.json
```

The `load_history()` function reads previously saved messages and converts them into Gemini-compatible content objects.

The `save_history()` function retrieves the current conversation history and writes it to the JSON file.

The program then supplies the restored history when creating the next chat session.

### Does It Remember My Name?

Yes, it can use your name if that information is present in the restored conversation history and available within the context sent to the model.

For example:

1. Tell the chatbot your name.
2. Ask it questions about AI.
3. Exit the program.
4. Run the program again.
5. Ask it what your name is.

This demonstrates conversational continuity across sessions.

### Is This Permanent AI Memory?

Not exactly.

This project saves conversation history rather than building a dedicated long-term memory system. As conversations grow, model context limits and the amount of history sent to the model may affect what information it can use.

A future version could implement a separate memory system to store selected user preferences, important facts, and summaries.

---

## 🐛 Troubleshooting

### 1. Missing API Key

**Error:**

```text
Add GEMINI_API_KEY to your .env file.
```

**Solution:**

- Create a `.env` file beside `chatbot.py`.
- Add your key using the format shown in the API setup section.
- Make sure the variable is named `GEMINI_API_KEY`.
- Run the program again.

### 2. API Error

The program may display an API error if the request fails.

Possible causes include:

- Invalid or revoked API key.
- Network connection problems.
- API quota or rate limits.
- Model access restrictions.
- An unavailable or unsupported model name.

Check your API key, internet connection, account limits, and Google's current Gemini documentation.

The code currently specifies a model name in `chatbot.py`. If that model is unavailable to your account, replace it with a currently supported model that your API key can access.

Official documentation:

https://ai.google.dev/gemini-api/docs

### 3. Missing Python Packages

If Python reports that a module cannot be found, activate your virtual environment and install the dependencies again:

```bash
python -m pip install google-genai python-dotenv
```

Make sure you run the program using the same Python environment where the packages were installed.

### 4. Chat History Cannot Be Loaded

If the program reports that `chat_history.json` cannot be loaded:

- Check whether the file contains valid JSON.
- Make a backup before editing or replacing the file.
- If you want to start a fresh conversation, rename or remove the old history file.

Removing the history file will discard the local saved conversation unless you have a backup.

### 5. Chat History Is Not Saving

Check whether the project folder is writable and that the program has permission to create or modify files.

The program saves history after a successful AI response. If an error occurs, review the message printed in the terminal.

---

## 🔐 Security and Privacy

This project stores conversation history locally in a JSON file.

Keep these points in mind:

- Never commit your API key to GitHub.
- Do not upload personal conversations or private information.
- Add `.env` and `chat_history.json` to `.gitignore`.
- Use a private repository if you intentionally need to keep sensitive project files in GitHub, while remembering that private repositories are not a substitute for secure secret storage.
- The chatbot sends messages to Google's Gemini API to generate responses. Review Google's applicable privacy and data policies before sending sensitive information.
- Anyone who obtains your API key may be able to use it according to its permissions and limits.

### Recommended `.gitignore`

Create a file named `.gitignore` with:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
chat_history.json
```

This prevents the local API key, virtual environment, Python cache files, and personal chat history from being included in normal Git commits.

**Important:** If you have already committed an API key, removing it from the latest version of the file is not enough. Revoke or rotate the exposed key and clean up the repository history as appropriate.

---

## 🔮 Future Improvements

Possible improvements for future versions include:

- Store selected user details in a dedicated memory system.
- Add a graphical user interface using Streamlit or another framework.
- Support clearing chat history from within the application.
- Add commands for viewing and managing saved conversations.
- Organize conversations into separate sessions.
- Implement conversation summarization for long chats.
- Add timestamps to saved messages.
- Add configurable model selection.
- Support exporting and importing conversations.
- Improve logging and error handling.
- Add automated tests.
- Explore retrieval-augmented generation (RAG) for searching personal documents.

These are possible future enhancements and are not necessarily implemented in the current version.

---

## 🎯 Learning Outcomes

This project provides practical experience with:

- Python application development.
- Calling an external AI API.
- Using Google's Gemini SDK.
- Environment variables and API key management.
- Reading and writing JSON files.
- Persistent application state.
- Restoring conversational context.
- Exception handling.
- Building command-line applications.
- Understanding the foundations of conversational AI.

---

## 👨‍💻 Author

**Muhammad Musab**

Computer Science Student | AI and Generative AI Learner

Interested in Artificial Intelligence, Large Language Models (LLMs), Generative AI, and Conversational AI.

GitHub: [@muhammad-musab03](https://github.com/muhammad-musab03)

---

## 📄 License

This project is available for learning and educational purposes.

If you want others to reuse, modify, and distribute your code under clear terms, consider adding an appropriate open-source license, such as the MIT License, in a separate `LICENSE` file.

---

## ⭐ Support

If you find this project useful for learning Python, Gemini API integration, or conversational AI, consider starring the repository on GitHub.

Thank you for checking out the Gemini-Conversational-AI.
**Keep Learning. Keep Building. Keep Exploring AI.** 🚀
