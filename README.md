# Notewise AI Study Assistant 📚🤖

**Homingo Hackathon (Edition 01) — LLM Apps Track Submission**

Notewise AI Study Assistant is an AI-powered personal tutor built for every learner. It helps students study smarter by turning lengthy notes and complex topics into clear summaries, simple explanations, and instant practice quizzes.

---

## ✨ Key Features
- **Summarize Notes:** Converts long study material into concise, structured bullet points.
- **Explain in Simple Words:** Breaks down difficult concepts into easy-to-understand language.
- **Create 5 MCQ Quiz:** Generates instant multiple-choice questions for quick exam self-assessment.
- **Dynamic Model Selection:** Automatically detects available Gemini Flash models for fast and reliable responses.

---

## 🛠️ Tech Stack & AI Tools Used
*(Disclosed as per Homingo Hackathon guidelines)*
- **Language:** Python 3
- **Frontend / UI Framework:** Gradio (`gradio`)
- **AI Model & SDK:** Google Gemini API (`google-genai` SDK using Gemini Flash models)

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd NOTEWISE-AI-STUDY-ASSISTANT
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Gemini API Key:**
   Open `app.py` and replace `"YOUR_GEMINI_API_KEY"` with your own API key from [Google AI Studio](https://google.com).

4. **Run the application:**
   ```bash
   python app.py
   ```
   Open the local URL (`http://127.0.0.1:7860`) in your browser.
