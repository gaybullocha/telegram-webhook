from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.json

    action = data.get('action', 'NO SIGNAL')

    if "BUY" in action:
        signal_emoji = "🟢"
    elif "SELL" in action:
        signal_emoji = "🔴"
    else:
        signal_emoji = "📊"

    message = f"""
{signal_emoji} GENAN TRADING SIGNAL

📊 Signal: {data.get('action')}

🪙 Ticker: {data.get('ticker')}

💰 Price: {data.get('price')}

⏰ Time: {data.get('time')}

🕒 Timeframe: {data.get('timeframe')}
"""

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    return "OK", 200


if name == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
