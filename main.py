from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename

from Users.User import *
import Users
app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = "static/CDN"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/signup', methods=["POST"])
def signup():
    try:
        username = request.args.get("username")
        password = request.args.get("password")
        email = request.args.get("email")
        potentialUser = User(username, password, email)
        result = Users.validateUser(potentialUser)
        if result == "U":
            return jsonify({"Error": "Username is taken"})
        if result == "E":
            return jsonify({"Error": "Email is taken"})
        Users.createNewUser(potentialUser)
        return jsonify({"Result": "Success"})
    except:
        return jsonify({
           "Error": "POST request invalid"
       })

@app.route('/login', methods=["POST"])
def login():
    print(request.args.get("username"))
    return jsonify(Users.login(request.args.get("username"), request.args.get("password")))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
            return jsonify({"Error": "No files were provided"})
    file = request.files['file']

    if file.filename == '':
            return jsonify({"Error": "No files were provided, or it is empty"})
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"Result": "Success"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')