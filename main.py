from flask import Flask, request, jsonify, render_template
from Users.User import *
import Users
app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)