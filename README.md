# Learn Flask with NeuralNine
Learning Flask from Beginner to Development from NeuaralNine
[Course Link](https://youtu.be/oQ5UfJqW5Jo?si=2sLHY_I55FEr2cKs&t=7111)

- create github repository
- clone github repository in the folder
- `code .` to open in vscode

OR

### create project directory
```bash
mkdir project_name
```
### create virtual environemnt
```bash
python3 -m venv .venv
```
### activate virtual environment
```bash
source .venv/bin/activate
```
### install required packages
```bash
pip3 install flask
```
### see installed packages inside virtual environment
```bash
pip3 freeze
```
### create requirements.txt file for server deployment
```bash
pip3 freeze > requirements.txt
```
### install requirements.txt file for server deployment
```bash
pip3 install -r requirements.txt
```
### if we need to set `GET,POST` in the app route. it will exculively use it
```python
@app.route('/about', methods=['POST'])
```
- for posing data we use POST
- for getting data from URL use GET
- to submit or change/update data to the db use PUT
- to delte data use delete