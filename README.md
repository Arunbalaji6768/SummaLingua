# SummaLingua
This project is a Flask-based web application that allows users to summarize and translate content from any given website URL. It leverages AI models for summarization and Google Translate for translation, supporting multiple languages.

#Features
Content Extraction: Extracts text content from a webpage using BeautifulSoup.
Summarization: Summarizes the extracted content using the facebook/bart-large-cnn model from Hugging Face Transformers.
Translation: Translates the summarized or original content into one of the supported languages using Google Translate.
Real-Time Progress Updates: Utilizes Server-Sent Events (SSE) to provide real-time progress updates during processing.
User-Friendly Interface: Simple and intuitive web interface for input and output.

#Supported Languages
The application supports the following languages for translation:
Tamil (ta),Hindi (hi),Telugu (te),Odia (or),Kannada (kn),Malayalam (ml),Bengali (bn),Gujarati (gu),Marathi (mr),Punjabi (pa),Urdu (ur),English (en) multiple level language like german and other language in future

#Usage
Home Page: Enter the URL of the webpage you want to process and select the desired language and option (summarize or translate).
Processing: The application will extract the content, summarize it (if selected), and translate it into the chosen language.
Results: The results will be displayed on the result page, showing the original content, summarized content (if applicable), and the translated content.

#Dependencies
Flask
BeautifulSoup
requests
transformers
googletrans

#Installation

Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:
pip install -r requirements.txt
Run the Application:
python app.py

#Acknowledgments
Hugging Face Transformers for the summarization model.
Google Translate for the translation functionality.
Flask for the web framework.

#Contact
For any questions or suggestions, feel free to reach out:
Arunbalaji PR
Email: prarunbalaji853@gmail.com
