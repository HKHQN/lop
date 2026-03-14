# app.py
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return jsonify({'status': 'success', 'message': f'Cảm ơn {name}!'})
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='speak.keancapytuong.xyz', port=port, debug=True)
