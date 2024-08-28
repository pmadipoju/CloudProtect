# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# # A mock user for the sake of this example
# mock_user = {
#     "username": "admin",
#     "password": "admin"
# }

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/login')
# def index():
#     return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']

#     if username == mock_user['username'] and password == mock_user['password']:
#         return redirect(url_for('loading'))
#     else:
#         return redirect(url_for('index', error=True))

# @app.route('/loading')
# def loading():
#     return render_template('loading.html')

# # @app.route('/dashboard')
# # def dashboard():
# #     return render_template('dashboard.html')

# @app.route('/dashboard')
# def dashboard():
#     return redirect('http://172.18.157.153:8091/')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A mock user for the sake of this example
mock_user = {
    "username": "admin",
    "password": "admin"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == mock_user['username'] and password == mock_user['password']:
        return redirect(url_for('loading'))
    else:
        return redirect(url_for('index', error=True))

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/dashboard')
def dashboard():
    return redirect('http://172.18.157.153:8091/')

if __name__ == '__main__':
    app.run(debug=True)
