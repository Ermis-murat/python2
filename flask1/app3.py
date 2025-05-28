from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/greet', methods=['POST'])
def greet():
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    name = request.form.get('name')
    return render_template('greet2.html', name=name, current_date=current_date,
current_time=current_time)
    
if __name__ == '__main__':
    app.run(debug=True)
