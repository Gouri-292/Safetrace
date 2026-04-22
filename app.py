from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

# Twilio creds (get from dashboard)
ACCOUNT_SID = "your_sid"
AUTH_TOKEN = "your_token"
TWILIO_NUMBER = "+1234567890"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route("/sos", methods=["POST"])
def sos():
    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")

    link = f"https://maps.google.com/?q={lat},{lon}"
    msg = f"HELP! I am in danger. Track me: {link}"

    message = client.messages.create(
        body=msg,
        from_=TWILIO_NUMBER,
        to="+918602121552"   # your number
    )

    return {"status": "sent"}

if __name__ == "__main__":
    app.run(debug=True)