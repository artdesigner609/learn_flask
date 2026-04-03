import os
from datetime import datetime
from flask import Flask, request, current_app, render_template
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)

UPLOAD_SUBDIR = os.path.join('templates', 'uploaded_files')
@app.route('/', methods=['GET'])
def home():
    return render_template('upload.html')

def ensure_upload_dir():
    base = current_app.root_path  # app root path
    upload_dir = os.path.join(base, UPLOAD_SUBDIR)
    os.makedirs(upload_dir, exist_ok=True)
    return upload_dir

def timestamped_filename(original_filename):
    name = secure_filename(original_filename)
    stem, ext = os.path.splitext(name)
    ts = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-UTC')  # YYYY-MM-DD-HH-MM-SS-UTC
    return f"{stem}-{ts}{ext}"

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files.get('file_name')
    if not file:
        return "No file selected", 400

    filename = file.filename
    ctype = file.content_type

    # Save file with timestamped name inside templates/uploaded_files
    upload_dir = ensure_upload_dir()
    new_name = timestamped_filename(filename)
    save_path = os.path.join(upload_dir, new_name)
    file.seek(0)
    file.save(save_path)

    # Return filename and content (do not return before reading content)
    if ctype == 'text/plain' or filename.lower().endswith('.txt'):
        file.seek(0)
        content = file.read().decode('utf-8')
        return f"File uploaded: {new_name}\nFile content: {content}"

    if ctype in ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                 'application/vnd.ms-excel') or filename.lower().endswith(('.xlsx', '.xls')):
        file.seek(0)
        df = pd.read_excel(file)
        return f"File uploaded: {new_name}\nExcel content:\n{df.to_html()}"

    return f"File uploaded: {new_name}\nUnsupported file type: {ctype}", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)