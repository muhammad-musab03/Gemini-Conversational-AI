from google import genai
from google.genai import types, errors
from dotenv import load_dotenv
from pathlib import Path
import json
import os

# Keep .env and history beside this Python file.
BASE_DIR = Path(__file__).resolve().parent
HISTORY_FILE = BASE_DIR / "chat_history.json"

# Load API key.
load_dotenv(BASE_DIR / ".env")
api_key = os.getenv("Gemini_key")

if not api_key:
    raise SystemExit("Add GEMINI_API_KEY to your .env file.")

# Connect to Gemini.
client = genai.Client(api_key=api_key)


def load_history():
    """Read saved messages when the program starts."""
    if not HISTORY_FILE.exists():
        return []

    with HISTORY_FILE.open("r", encoding="utf-8") as file:
        saved_messages = json.load(file)

    # Convert saved dictionaries into Gemini Content objects.
    return [
        types.Content.model_validate(message)
        for message in saved_messages
    ]


def save_history(chat):
    """Save the conversation after a successful response."""
    messages = [
        message.model_dump(mode="json", exclude_none=True)
        for message in chat.get_history(curated=True)
    ]

    # Write a temporary file, then replace the previous history.
    temporary_file = HISTORY_FILE.with_suffix(".tmp")

    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(messages, file, indent=2, ensure_ascii=False)

    temporary_file.replace(HISTORY_FILE)


# Restore the previous conversation.
try:
    history = load_history()
except (OSError, ValueError, TypeError) as error:
    raise SystemExit(
        f"Could not load chat_history.json: {error}\n"
        "Check the file or rename it to start a new conversation."
    )

# Create one chat session with the restored messages.
chat = client.chats.create(
    model="gemini-3.8-flash",
    history=history,
)

print("Gemini Chatbot Started!")
print(f"Loaded {len(history)} previous messages.")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Chatbot stopped!")
        break

    if not user_input:
        continue

    try:
        response = chat.send_message(user_input)
    except errors.APIError as error:
        print(f"API error: {error}\n")
        continue

    print("Gemini:", response.text or "No text response returned.")

    try:
        save_history(chat)
    except OSError as error:
        print(f"Could not save history: {error}")

    print()