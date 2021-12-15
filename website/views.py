from flask import Blueprint, render_template, request, jsonify
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def index():
  return render_template('index.html')

