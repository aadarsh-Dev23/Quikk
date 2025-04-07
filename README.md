# ⚡ Quikk

> Instantly build your million dollar idea from just a prompt. Powered by AI. Made for dreamers who ship fast.

---

## 🚀 What is Quikk?

**Quikk** is a Python-based CLI tool that takes your idea as input and generates a full project structure with actual file contents — using the power of **Google Gemini AI**.

Think of it as your instant startup partner. You give it an idea like:

```bash
quikk "Build me a Flask-based URL shortener"
```

And boom 💥 — it creates a complete project, with folders, files, and code. All AI-generated and ready to hack on.

---

## 🧠 How It Works

1. You give it a product/idea description.
2. Quikk sends your idea to the Google Gemini API.
3. Gemini returns:
   - Suggested file/folder structure
   - Content of each file
4. Quikk builds it all on your machine, ready to run.

---

## 🛠️ Installation

### 🔁 1. Clone the repo

```bash
git clone https://github.com/yourusername/quikk.git
cd quikk
```

### 📦 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 🔑 3. Set your Gemini API key

Create a `.env` file in the root with:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ⚡ Usage

### Run it via Python:

```bash
python app.py
```

Or directly with an idea:

```bash
python app.py "Build a CLI tool that manages student attendance"
```

### If installed globally (via `setup.py` or `.bat`):

```bash
quikk "An AI-powered personal budget tracker"
```

---


## 🧰 Tech Stack

- Python 3.11
- Google Gemini API (`google-generativeai`)
- dotenv
- CLI UX (`input()` or `argparse`)

---

## 📁 Example Output

```
your_project/
├── main.py
├── utils/
│   └── helpers.py
├── requirements.txt
├── README.md
└── .env
```

All files include content generated from your prompt.

---

## 💡 Prompt Ideas

- `Create a FastAPI backend for a to-do app`
- `Generate a Telegram bot that responds to weather queries`
- `Build a desktop note-taking app using Tkinter`
- `Make a Flask + SQLAlchemy REST API for managing books`

---

## 📌 Roadmap

- [ ] Templates for popular app types
- [ ] Multi-model support (OpenAI, Gemini, Ollama)
- [ ] Web UI (maybe Streamlit or Flask?)
- [ ] GitHub integration to push generated projects
- [ ] Configurable file content rules

---

## ❤️ Contributing

Feel free to fork, PR, or open issues. Let's build the fastest way to ship ideas — together.

---

## ⚠️ Disclaimer

This tool uses AI to generate code. Always review and test it before using in production.

---

## 📄 License

MIT License

---

> Built with 💡 by Aadarsh S

---
