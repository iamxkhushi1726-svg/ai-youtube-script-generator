# 🎬 AI YouTube Script Generator

> Project 12/100 — Building a strong GitHub portfolio from scratch.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://iamxkhushi1726-svg-ai-youtube-script-generator-app-zj1xdm.streamlit.app/)

---

## 📌 Overview

Generate complete, production-ready YouTube scripts in seconds. By inputting your topic, preferred tone, desired duration, and target audience, the **AI YouTube Script Generator** leverages **Groq & Llama 3** to write a perfectly structured script complete with a hook, introduction, three content body sections, a Call to Action (CTA), and an end screen.

> 🚀 **Live Demo:** [Open the Streamlit App](https://iamxkhushi1726-svg-ai-youtube-script-generator-app-zj1xdm.streamlit.app/)

---

## 📸 App Interface

![dashboard](image.png)

---

## ✨ Features

- **Complete Script Structuring:** Automatically generates a hook, intro, 3 distinct body sections, a CTA, and an end screen.
- **Dynamic Tone Adaptation:** Choose between 6 unique tones (*energetic, professional, casual, storytelling, motivational, humorous*).
- **Smart Length Calibration:** Select durations from 5 to 20 minutes; the LLM automatically calibrates word counts based on average speaking pacing.
- **Custom Control:** Input your own specific section titles or let the AI auto-generate them.
- **SEO Optimization:** Include target keywords to weave throughout the script for better video discoverability.
- **One-Click Export:** Download the finalized script instantly as a clean `.txt` file.
- **Real-time Metrics:** Displays live word counts and estimated read times.
- **Built-in Guidance:** Sidebar loaded with practical script-writing and pacing tips.

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit
- **LLM Orchestration:** LangChain
- **Inference Engine:** Groq API (`Llama 3 8B`)
- **Language & Environment:** Python, `python-dotenv`

---

## 🚀 Run Locally

Clone the repository and set up your local environment in less than two minutes:

```bash
# Clone the repository
git clone https://github.com/iamxkhushi1726-svg/ai-youtube-script-generator.git

cd ai-youtube-script-generator

# Set up a virtual environment
python -m venv venv

# Activate the virtual environment

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
echo "GROQ_API_KEY=your_actual_api_key_here" > .env

# Run the application
streamlit run app.py
```

---

## 💡 Example Prompt Configuration

To test the application with optimal results, try these settings:

| Setting | Value |
|----------|-------|
| **Topic** | How to start investing in 2026 as a student |
| **Tone** | Casual and conversational |
| **Duration** | 10 minutes |
| **Audience** | College students aged 18–22 |

---

## 🧠 What I Learned

Building this project helped me sharpen several production-level AI engineering and frontend skills:

- How to use `temperature=0.7` for creative LLM output vs `0.1` for factual.
- How to build download buttons in Streamlit with `st.download_button`.
- How to design multi-column Streamlit layouts for clean UX.
- How to calibrate script length by word count (150 WPM rule).

---

## 🏆 Part of the 100 Projects Challenge

This repository is **Project 12** of my personal challenge to build **100 distinct applications**, focusing on AI, data engineering, and clean web interfaces.

👨‍💻 **Follow my journey on GitHub:** [@khushi-ai](https://github.com/iamxkhushi1726-svg)

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.