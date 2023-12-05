from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Telegram API token and URL
TELEGRAM_API_TOKEN = 'your_telegram_api_token'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    chat_id = request.form.get('chat_id')
    message_text = request.form.get('message_text')

    if chat_id and message_text:
        params = {
            'chat_id': chat_id,
            'text': message_text,
        }

        response = requests.post(TELEGRAM_API_URL, params=params)

        if response.ok:
            return 'Message sent successfully!'
        else:
            return f'Failed to send message. Check your chat_id and token. Response: {response.content.decode("utf-8")}'
    else:
        return 'Invalid input. Please provide chat_id and message_text.'

if __name__ == '__main__':
    app.run(debug=True)
