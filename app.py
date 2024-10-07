from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')

    if not message:
        return jsonify({'error': 'Message not provided'}), 400

    try:
        response = ollama.chat(model='tinyllama', messages=[
            {
                'role': 'user',
                'content': message,
            },
        ])
        return jsonify({'response': response['message']['content']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8120, debug=True)

