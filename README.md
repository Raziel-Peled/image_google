# 👁️ Gemini Image Analyzer

A smart web application built with Flask and the `google-genai` SDK that uses the `gemini-3.6-flash` model to analyze and describe images.

## Features
* 🖼️ Live image preview before upload
* 🤖 AI-powered image analysis using Google's Gemini API
* 🛡️ Built-in handling for Gemini safety blocks
* 🌐 Responsive frontend UI with RTL (Hebrew) support

## Prerequisites
* Python 3.x
* Gemini API Key

## Installation & Setup

1. Clone this repository to your local machine.
2. Install the required Python packages:
   ```bash
   pip install flask google-genai pillow python-dotenv

1. Create a .env file in the root directory and add your API key: GEMINI_API_KEY=your_api_key_here
2. Run the application: python app.py
3. Open your browser and go to http://127.0.0.1:5000