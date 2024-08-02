from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll', methods=['POST'])
def roll():
    n = int(request.form['dice_number'])
    rolls = [random.randint(1, 6) for _ in range(n)]
    total = sum(rolls)
    return jsonify(rolls=rolls, total=total)

if __name__ == '__main__':
    app.run(debug=True)
