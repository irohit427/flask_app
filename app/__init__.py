from flask import Flask, render_template, jsonify, request
from config import Config
app = Flask(__name__)

app.config.from_object(Config)

from app import routes