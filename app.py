from flask import Flask, render_template, request, jsonify
from google import genai
from PIL import Image
import io
import os
from dotenv import load_dotenv

# טעינת המפתח
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

app = Flask(__name__)

# אתחול לקוח ג'מיני החדש
client = genai.Client(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({'error': 'לא נשלחה תמונה'}), 400
        
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'לא נבחר קובץ'}), 400

    try:
        image_bytes = file.read()
        pil_image = Image.open(io.BytesIO(image_bytes))

        prompt = "תאר בפירוט מה אתה רואה בתמונה הזו. ענה בעברית ברורה וטבעית."
        
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=[pil_image, prompt]
        )
        
        # === התיקון שלנו מתחיל כאן ===
        
        # נבדוק אם יש טקסט בתשובה
        if response.text:
            return jsonify({'description': response.text})
            
        # אם אין טקסט, נבדוק אם התשובה נחסמה בגלל בטיחות
        elif response.prompt_feedback:
            block_reason = response.prompt_feedback.block_reason
            return jsonify({'error': f'התמונה נחסמה על ידי מנגנון הבטיחות של גוגל. סיבה: {block_reason}'}), 400
            
        else:
            return jsonify({'error': 'המודל לא הצליח לייצר תיאור לתמונה הזו (תשובה ריקה)'}), 400

    except Exception as e:
        print(f"❌ שגיאה: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)