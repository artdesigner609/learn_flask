from flask import Flask, request, make_response

app = Flask(__name__)

# add default index route


@app.route('/', methods=['POST'])
def index():
    return "hello world!"

# add another static route


@app.route('/about_me', methods=['GET'])
def about_me() -> LiteralString:
    return "<p>I am a software Engineer. i love to code in python. and sushi</p>"

# create a greet route


@app.route('/greet/<first_name>', methods=['GET'])
def greet_user(first_name) -> str:
    return f"<h2>Hello {first_name}, welcome to website!.</h2>"

# adding numbers


@app.route('/add_me/<n1>/<n2>', methods=['GET'])
def add(n1, n2) -> Response | str:
    """
    For Example: Type in Url: http:localhost:5000/add_me/8/2
    """
    try:
        a = int(n1)
        b = int(n2)
    except ValueError:
        return make_response("Error: Please provide valid integer for addition process", 404)
    return f"Number 1 : {a} and Number 2 : {b}. Sum is : {a+b}"

# check what request is made through URL


@app.route('/check_request_method', methods=['GET', 'POST', 'PUT'])
def check_request():
    if request.method == 'GET':
        return "This is a GET request"
    elif request.method == 'POST':
        return "This is a POST request"
    elif request.method == 'PUT':
        return "This is a PUT request"

# curl http://127.0.0.1:5555/check_request_method
# curl http://127.0.0.1:5555/check_request_method -X POST


# run the applicaiton
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)
