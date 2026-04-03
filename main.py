from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

#add default route
@app.route('/', methods=['GET'])
def home():
    eng_desc = {
        'name' : 'John Doe',
        'age' : 30,
        'city' : 'New York',
        'salary' : 50000,
        'education' : 'Computer Science'
    }
    return render_template('index.html', context=eng_desc)

#add aboutme route
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)