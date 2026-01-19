from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Majha DevOps Project Live Zala Aahe!"

app.run(host="0.0.0.0", port=5000)