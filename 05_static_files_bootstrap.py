from flask import Flask, render_template

app = Flask(__name__, template_folder='templates',
            static_folder='static', static_url_path='/')


@app.route('/', methods=['GET'])
def home() -> str:
    return render_template('05_static_files_bootstrap.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)
