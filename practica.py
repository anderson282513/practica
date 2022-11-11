from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "servidor en ejecucion"

# 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