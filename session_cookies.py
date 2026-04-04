from flask import Flask, render_template, session

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = 'my_key'


@app.route('/')
def home():
    return render_template('session_cookies.html', message='index page')

@app.route('/set_session_data')
def set_session_data():
    session['name'] = 'Easter'
    session['id'] = 123456
    return render_template('session_cookies.html', message='Session data has been set!')

@app.route('/get_session_data')
def get_session_data():
    if 'name' in session.keys() and 'id' in session.keys():
        name = session.get('name', 'Guest')
        user_id = session.get('id', 'N/A')
        return render_template('session_cookies.html', message=f'Name: {name}, ID: {user_id}')
    else:
        return render_template('session_cookies.html', message='Session data not found!')

@app.route('/clear_session_data')
def clear_session_data():
    session.clear()
    return render_template('session_cookies.html', message='Session data has been cleared!')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)