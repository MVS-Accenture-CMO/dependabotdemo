import requests
import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    r = requests.get("https://example.com")
    return "Dependabot & GHAS Demo"

if __name__ == "__main__":
    app.run(debug=True)
