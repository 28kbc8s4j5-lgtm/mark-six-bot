from flask import Flask, request, render_template
from main import parse_bet_text, get_current_lunar_year

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/parse", methods=["POST"])
def parse():
    text = request.form.get("text")

    _, _, zodiac_mapping = get_current_lunar_year()

    import asyncio
    result = asyncio.run(parse_bet_text(text, zodiac_mapping))

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)