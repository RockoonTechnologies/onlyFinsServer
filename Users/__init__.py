import json

import Users.User
savefile = "Users/savefile.json"
inSave = False

def load():
    while inSave:
        pass
    with open(savefile) as f:
        data = json.load(f)
        return data

def save(data):
    inSave = True
    with open(savefile, 'w') as json_file:
        json.dump(data, json_file)
    inSave = False


def searchUsers(param, query):
    for item in load():
        if item[param] == query:
            return item


def validateUser(user):
    if searchUsers("username", user.username) != None:
        return "U"
    if searchUsers("email", user.email) != None:
        return "E"
    return True

def createNewUser(user):
    current = load()
    current.append(user.jsonify())
    save(current)


def login(username, password):
    user = searchUsers("username", username)
    print(user)
    password = searchUsers("password", password)
    if user == None or password == None:
        return {"Error": "Username/Password is not registered"}
    return user
