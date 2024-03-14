from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def show_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def process_login():

      return redirect(url_for('show_dashboard'))

@app.route('/dashboard')
def show_dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
