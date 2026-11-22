import gradio as gr
from google import genai

# 1. अपनी API Key यहाँ पेस्ट करें
client = genai.Client(api_key="api here")

def study_assistant(notes, task):
    if not notes.strip():
        return "कृपया पहले अपने नोट्स या सवाल लिखें!"
    
    prompt = f"You are Notewise AI Study Assistant. Task: {task}. Give a fast, clear, and concise response in bullet points.\n\nNotes/Topic:\n{notes}"
    
    # यह कोड अपने आप आपके अकाउंट के लिए काम करने वाले सभी Flash मॉडल्स को ढूँढ लेगा
    try:
        available_models = [
            m.name.replace("models/", "") 
            for m in client.models.list() 
            if "flash" in m.name.lower()
        ]
    except Exception:
        available_models = ["gemini-2.5-flash", "gemini-2.0-flash"]

    last_error = ""
    for model_name in available_models:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            last_error = str(e)
            continue
            
    return f"अभी कनेक्शन में दिक्कत आ रही है: {last_error}"

app = gr.Interface(
    fn=study_assistant,
    inputs=[
        gr.Textbox(lines=5, placeholder="यहाँ अपने नोट्स या सवाल लिखें...", label="आपके नोट्स / सवाल"),
        gr.Dropdown(
            choices=["Summarize Notes", "Explain in Simple Words", "Create 5 MCQ Quiz"],
            value="Summarize Notes",
            label="AI से क्या करवाना चाहते हैं?"
        )
    ],
    outputs=gr.Textbox(lines=10, label="Notewise AI का जवाब"),
    title="Notewise AI Study Assistant",
    theme=gr.themes.Soft()
)

app.launch()