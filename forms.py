import os
from datetime import datetime
import pandas as pd
from flask import Flask, request, make_response, render_template, redirect, url_for, current_app
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates')

#add default route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':  
        return render_template('forms.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        hidden_data = request.form.get('hidden_data')
        return f"Received data: Name={name}, Age={age}, Email={email}, Hidden Data={hidden_data}"
    else:
        return "Unsupported method", 405
    
@app.route('/upload_file', methods=['POST'])    
def upload_file():
    file = request.files.get('file_name')
    if not file:
        return "No file selected", 400

    # If you still want to include filename, do it alongside content (don't return early)
    filename = file.filename
    ctype = file.content_type

    if ctype == 'text/plain' or filename.endswith('.txt'):
        content = file.read().decode('utf-8')
        return f"File uploaded: {filename} \n File content: {content}"

    # handle common Excel content types and extensions
    if ctype in ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                 'application/vnd.ms-excel') or filename.lower().endswith(('.xlsx', '.xls')):
        # pandas can accept the file-like object directly
        df = pd.read_excel(file)
        return f"File uploaded: {filename} \n Excel content:\n{df.to_html()}"

    return f"Unsupported file type: {ctype}", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)