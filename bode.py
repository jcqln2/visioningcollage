from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    data = request.json
    words = data.get("words", [])
    
    if not words or len(words) > 20:
        return jsonify({"error": "Please enter between 1 and 20 words."}), 400
    
    # Construct AI prompt
    prompt = f"Create a digital medley of images featuring: {', '.join(words)}. Use artistic variety and visual storytelling."
    
    return jsonify({"prompt": prompt})

if __name__ == '__main__':
    app.run(debug=True)