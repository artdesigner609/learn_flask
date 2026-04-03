from flask import Flask, request, make_response, render_template

app = Flask(__name__, template_folder='templates')

#add default route
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)