from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def home():
    return "Welcome to Reddit Clone!"

if __name__ == "__main__":
    app.run(debug=True)
