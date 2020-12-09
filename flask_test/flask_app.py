import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

persons = [
    {'id': 0,
    'name': "Leszek",
    'phone': "23123123"},
    {'id': 1,
    'name': "Sonia",
    'phone': "12312313"}
]

@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome</h1>"

@app.route("/api/phonebook", methods=["GET"])
def phonebook():    
    return jsonify(persons)

@app.route("/api/phonebook/add", methods=["POST"])
def add_person():    
    #print(request.json)
    person = {}
    if request.json:
        try:    
            person['id'] = 123
            person["name"] = request.json["name"]
            person["phone"] = request.json["phone"]
        except KeyError:
            person = {}
        persons.append(person)

    return jsonify(person)

app.run()