from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'replace-this-with-a-secure-secret'
BACKEND_URL = 'http://localhost:8000'

VALID_USERNAME = 'admin'
VALID_PASSWORD = 'admin123'

@app.route('/')
def home():
    if session.get('logged_in'):
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if session.get('logged_in'):
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if username.lower() == VALID_USERNAME and password == VALID_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        error = 'Invalid credentials'

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    result = None
    error = None
    action = ''

    if request.method == 'POST':
        action = request.form.get('action', '').strip()
        if not action:
            error = 'Please enter an action to check.'
        else:
            try:
                response = requests.post(
                    f'{BACKEND_URL}/check',
                    json={'action': action},
                    timeout=10
                )
                if response.ok:
                    data = response.json()
                    result = data.get('result')
                else:
                    error = f'Backend error: {response.status_code} - {response.text}'
            except requests.RequestException:
                error = 'Unable to connect to backend server.'

    return render_template('dashboard.html', result=result, error=error, action=action)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
