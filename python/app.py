from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

def generate_serial_number(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

users = {}

def add_user(name):
    if name not in users:
        serial_number = generate_serial_number()
        users[name] = serial_number
        return f"{name}님이 추가되었습니다. 일련번호: {serial_number}"
    else:
        return f"{name}님은 이미 등록되어 있습니다."

def check_serial_number(name):
    if name in users:
        return f"{name}님의 일련번호는 {users[name]}입니다."
    else:
        return f"{name}님은 일련번호가 없습니다."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user_route():
    name = request.form['name']
    result = add_user(name)
    return redirect(url_for('index', message=result))

@app.route('/check_serial_number', methods=['POST'])
def check_serial_number_route():
    name = request.form['name']
    result = check_serial_number(name)
    return redirect(url_for('index', message=result))

@app.route('/add_user_page')
def add_user_page():
    return render_template('add_user.html')

@app.route('/user_list')
def user_list():
    return render_template('user_list.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
