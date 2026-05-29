from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():

    try:
        data = request.json

        ticker = data.get('ticker', 'N/A')
        action = data.get('action', 'N/A')
        price = data.get('price', 'N/A')
        time = data.get('time', 'N/A')
        timeframe = data.get('timeframe', 'N/A')

        if "BUY" in action:
            emoji = "🟢"
        elif "SELL" in action:
            emoji = "🔴"
        else:
            emoji = "📊"

        message = f"""
{emoji} GENAN TRADING SIGNAL

📊 Signal: {action}

🪙 Ticker: {ticker}

💰 Price: {price}

⏰ Time: {time}

🕒 Timeframe: {timeframe}
"""

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": message
            }
        )

        return "OK", 200

    except Exception as e:
        return str(e), 500


if name == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
