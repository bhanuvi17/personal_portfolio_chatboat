from flask import Flask, render_template, request, jsonify, session
from datetime import datetime
import json
from chatbot import generate_contextual_response

app = Flask(__name__)
app.secret_key = "bhanuprakash_portfolio_chatbot"  # For session management

# Flask routes
@app.route('/')
def home():
    # Initialize chat history in session if not already there
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Get chatbot response with context awareness
    bot_response = generate_contextual_response(user_message, session.get('chat_history', []))
    
    # Add to chat history
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    chat_entry = {
        'user': user_message,
        'bot': bot_response,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    session['chat_history'].append(chat_entry)
    session.modified = True
    
    return jsonify({
        'response': bot_response,
        'history': session['chat_history']
    })

@app.route('/clear-history', methods=['POST'])
def clear_history():
    session['chat_history'] = []
    return jsonify({'success': True})

# Save chat history to file
@app.route('/save-history', methods=['POST'])
def save_history():
    if 'chat_history' in session and session['chat_history']:
        filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(session['chat_history'], f, indent=4)
        return jsonify({'success': True, 'filename': filename})
    return jsonify({'success': False, 'message': 'No chat history to save'})

if __name__ == '__main__':
    app.run(debug=True)