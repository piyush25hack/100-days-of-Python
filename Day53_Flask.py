from flask import Flask
import requests  

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://www.google.com")
    return response.text

if __name__ == '__main__':
    app.run(debug=True)