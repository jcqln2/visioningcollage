from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Better practice: use environment variables

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    data = request.json
    words = data.get("words", [])
    
    if not words or len(words) > 20:
        return jsonify({"error": "Please enter between 1 and 20 words."}), 400
    
    prompt = f"Create a digital medley of images featuring: {', '.join(words)}. Use artistic variety and visual storytelling."
    
    return jsonify({"prompt": prompt})

@app.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        response = openai.images.generate(
            model="dall-e-3",  # Specify the latest model
            prompt=prompt,
            n=1,  # Generate one image
            size="1024x1024"
        )
        
        # Extract image URL from response
        image_url = response.data[0].url
        return jsonify({"image_url": image_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
