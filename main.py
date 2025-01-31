from flask import Flask, request, render_template, jsonify, Response
from bs4 import BeautifulSoup
import requests
from transformers import pipeline
from googletrans import Translator
import time

app = Flask(__name__)

translator = Translator()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Supported language mapping
LANGUAGE_MAP = {
    '1': 'ta',  # Tamil
    '2': 'hi',  # Hindi
    '3': 'te',  # Telugu
    '4': 'or',  # Odia
    '5': 'kn',  # Kannada
    '6': 'ml',  # Malayalam
    '7': 'bn',  # Bengali
    '8': 'gu',  # Gujarati
    '9': 'mr',  # Marathi
    '10': 'pa',  # Punjabi
    '11': 'ur',  # Urdu
    '12': 'en',  # English (default)
}

# Function to extract content from a webpage
def extract_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No Title Found"
        paragraphs = [p.get_text() for p in soup.find_all('p') if p.get_text()]
        content = f"{title}\n\n" + "\n".join(paragraphs)
        return content
    except requests.exceptions.RequestException as e:
        return f"Error fetching content: {e}"

# Function to translate text with retry logic
def translate_text(text, language, retries=3, delay=2):
    lang_code = LANGUAGE_MAP.get(language, 'en')  # Default to English if not found
    for attempt in range(retries):
        try:
            translated = translator.translate(text, dest=lang_code)
            return translated.text
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                return f"Error translating text: {e}"

# Function to summarize text
def summarize_text(text):
    word_count = len(text.split())
    if word_count < 50:  # Avoid summarizing very short texts
        return text

    max_length = word_count // 3
    min_length = word_count // 4
    try:
        summarized = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summarized[0]['summary_text']
    except Exception as e:
        return f"Error summarizing text: {e}"

# **Progress Route (SSE for real-time updates)**
@app.route('/progress')
def progress():
    def generate():
        steps = ["Extracting content", "Summarizing content", "Translating content", "Finalizing"]
        for i, step in enumerate(steps):
            time.sleep(2)  # Simulating processing delay
            progress = (i + 2) * 20  # 25%, 50%, 75%, 100%
            yield f"data: {progress}\n\n"
    return Response(generate(), mimetype='text/event-stream')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    url = request.form.get('url')
    language = request.form.get('language')
    option = request.form.get('option')

    content = extract_content(url)
    if content.startswith("Error"):
        return render_template("result.html", original="Error fetching content.", summarized="", translated="")

    summarized_text = ""
    if option == '2':  # If summarization is selected
        summarized_text = summarize_text(content)
        
    translated_text = translate_text(summarized_text if summarized_text else content, language)

    return render_template("result.html", original=content, summarized=summarized_text, translated=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
