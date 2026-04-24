from flask import Flask, render_template, session, make_response, request, flash

app = Flask(__name__, template_folder='templates',
            static_folder='static', static_url_path='/')
app.secret_key = 'my_key'


@app.route('/')
def home():
    return render_template('06_session_cookies.html', message='index page')


@app.route('/set_session_data')
def set_session_data():
    session['name'] = 'Easter'
    session['id'] = 123456
    return render_template('06_session_cookies.html', message='Session data has been set!')


@app.route('/get_session_data')
def get_session_data():
    if 'name' in session.keys() and 'id' in session.keys():
        name = session.get('name', 'Guest')
        user_id = session.get('id', 'N/A')
        return render_template('06_session_cookies.html', message=f'Name: {name}, ID: {user_id}')
    else:
        return render_template('06_session_cookies.html', message='Session data not found!')


@app.route('/clear_session_data')
def clear_session_data():
    session.clear()
    return render_template('06_session_cookies.html', message='Session data has been cleared!')


@app.route('/set_cookie')
def set_cookie() -> Response:
    response = make_response(render_template(
        '06_session_cookies.html', message='Cookie has be set.'))
    response.set_cookie('cookie_name', 'cookie_value')
    return response


@app.route('/get_session_cookie')
def get_session_cookie() -> str:
    cookie_value: str = request.cookies['cookie_name']
    return render_template('06_session_cookies.html', message=f'Cookie Value is :{cookie_value}')


@app.route('/clear_session_cookie')
def clear_session_cookie():
    response = make_response(render_template(
        '06_session_cookies.html', message='Cookie removed.'))
    response.set_cookie('cookie_name', expires=0)
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('06.1_login.html')

    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'abc' and password == '12345':
            flash('Successful Login!')
            return render_template('06_session_cookies.html', message='')
        else:
            flash('Login Failed!')
            return render_template('06_session_cookies.html', message='')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
