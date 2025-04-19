# 🧠 Simple-KI-Chat

A minimalist, local console-based chat interface powered by a local language model via LM Studio.  
Ideal for experimental conversations, role-playing, or philosophical exchanges with a creative and empathetic assistant.

This project represents the author's first steps with Python and was created entirely through *Vibe Coding* — using prompt engineering and AI-assisted development.

## 🚀 Features

- Local use of an AI model via LM Studio (OpenAI-compatible API)
- Automatic saving of chat history with timestamps
- Support for system prompts and model selection
- **Streaming responses** — the reply is shown in real time while being generated
- Highlighting of `<think>` blocks to show the model's "thoughts"
- Simple configuration via `config.json`

## 📦 Requirements

- Python 3.9+
- A local LM Studio server with API access enabled
- A compatible model (e.g. Mistral, MythoMax) that works with the OpenAI-compatible endpoint

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/simple-ki-chat.git
cd simple-ki-chat
```

2. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

> **Note:** The only external dependency is `requests`. Ensure it is installed:
>
> ```bash
> pip install requests
> ```

3. Create your configuration file:

```bash
cp config.json.sample config.json
```

> **Important:** You must rename `config.json.sample` to `config.json` for the program to run correctly.

Edit `config.json` to your needs. Example:

```json
{
  "system_prompt": "You are a helpful, creative AI model.",
  "endpoint_url": "http://localhost:1234",
  "max_history": 10
}
```

## 🗨️ Usage

Start the console chat with:

```bash
python chat_console.py
```

Type your messages — the AI will reply in real time with colored highlights. Exit the chat by typing `exit` or `quit`.

At the end of the session, a file such as `chat_20250419_1530.json` will be created, containing the full conversation history.

## 📁 Project Structure

```
.
├── chat_console.py        # Main program for console interaction
├── lmstudio_api.py        # API communication with LM Studio (OpenAI-compatible)
├── config.json.sample     # Sample configuration file
├── .gitignore             # Ignores chat logs and config.json
├── LICENSE                # License information
├── README.md              # This file
```

## 🛡️ Privacy

All data remains local. There is no communication with external servers — everything runs via your local LM Studio server.

## 📜 License

See [LICENSE](LICENSE).

## 💡 Ideas or Contributions?

Pull requests, feedback, and suggestions are welcome!

---

🛠️ *This documentation was written by the author using AI and prompt engineering.*

