# 📺 Chat with YouTube Videos using OpenAI 🤖

> Engage in meaningful conversations with your favorite YouTube videos!  
This app extracts video transcripts and uses **GPT-4** to let you ask natural language questions about the content — right inside a simple Streamlit interface.

---

## 🚀 Features

✅ Chat with any YouTube video  
✅ Automatic transcript extraction  
✅ Powered by OpenAI GPT-4  
✅ Streamlit UI — no setup hassle  
✅ Modular architecture for easy extension  
✅ Local vector database (ChromaDB) support  

---

## 🧠 How It Works

1. Paste a YouTube video URL
2. The transcript is automatically fetched
3. The content is added to a vector database
4. Ask questions — the AI answers using video context!

---

## 📂 Project Structure

```plaintext
game_design_swarm/
│
├── README.md                   # 📖 Project documentation
├── requirements.txt            # 📦 Python dependencies
├── main.py                     # 🔵 Streamlit app
│
├── config/
│   └── settings.py             # ⚙️ App settings & model config
│
├── services/
│   ├── youtube_service.py      # 📺 YouTube transcript fetcher
│   └── embedchain_service.py   # 🤖 Embedchain app initializer
│
└── utils/
    └── helpers.py              # 🔧 Utility functions (ID extractors, etc.)
```

---

## 🛠️ Installation

```bash
git clone https://github.com/andredisa/youtube_chat_AI.git
cd youtube_chat_AI
pip install -r requirements.txt
```

---

## ▶️ Run the App
```bash
streamlit run main.py
```

---

## 🔑 Required API Keys
| Service | API Key Name     | Where to Get It          |
|---------|------------------|--------------------------|
| OpenAI  | `OPENAI_API_KEY` | https://platform.openai.com |

>Paste your API key directly in the app input field when prompted.
No keys are stored locally.

---

## 💬 Example Use Cases
- 🧠 Learn deeply from interviews, lectures, or talks

- 🔍 Extract insights from long-form content

- 📚 Summarize educational material

- 🗣️ Ask follow-up questions on key moments

---

## ✨ Contributing

🎉 **Contributions are more than welcome!**

If you find a bug 🐞, have a feature request ✨, or want to improve the code 💻:

- Open an [Issue](https://github.com/andredisa/youtube_chat_AI/issues)  
- Submit a [Pull Request](https://github.com/andredisa/youtube_chat_AI/pulls) 🚀  

>💬 Feel free to reach out on [GitHub](https://github.com/andredisa) or by [email](mailto:andreadisanti22@gmail.com)!

Let’s build this together!

---

## 📜 License

📄 This project is released under the **MIT License**.  
Please refer to the [LICENSE](LICENSE) file for full details.

---

### 🧑‍💻✨ Happy coding
