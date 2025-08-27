from flask import Flask
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return html_content

if __name__ == '__main__':
    app.run(debug=True)
