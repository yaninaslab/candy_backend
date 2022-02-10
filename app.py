import dbinteractions as dbi
from flask import Flask, request, Response
import json

import sys

app = Flask(__name__)

# Making GET request to db


@app.get('/candy')
def list_all_candies():
    try:
        # Trying to get an output from the function and converting it to json
        candies = dbi.list_all_candies()
        candies_json = json.dumps(candies, default=str)
        return Response(candies_json, mimetype="application/json", status=200)
    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)

# Making POST request to db


@app.post('/candy')
def add_new_candy():
    try:
        # Expecting values from the user to pass to the function that will create a new entry in db
        name = request.json['name']
        description = request.json['description']
        image_url = request.json['image_url']
        # Trying to get an output from the function and converting it to json in case a new row is added to db
        new_candy = dbi.add_new_candy(name, description, image_url)
        if(new_candy == True):
            new_candy_json = json.dumps(new_candy, default=str)
            return Response(new_candy_json, mimetype="application/json", status=200)
        else:
            return Response("Please enter valid data", mimetype="plain/text", status=400)

    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)

# Making PATCH (update) request to db


@app.patch('/candy')
def update_candy():
    try:
        # Getting id of the item and passing it to the function so that an item can be edited based on its id
        candy_id = request.json['candy_id']
        # Trying to get an output from the function and converting it to json if the request was successful
        candy_id = dbi.update_candy(candy_id)
        if(candy_id == True):
            candy_id_json = json.dumps(candy_id, default=str)
            return Response(candy_id_json, mimetype="application/json", status=200)
        else:
            return Response("Please enter valid data", mimetype="plain/text", status=400)
    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)

# Making DELETE request to db


@app.delete('/candy')
def delete_candy():
    try:
        # Getting id of the item and passing it to the function so that an item can be deleted based on its id
        candy_id = request.json['candy_id']
        # Trying to get an output from the function and converting it to json if the request was successful
        candy_id = dbi.delete_candy(candy_id)
        if(candy_id == True):
            candy_id_json = json.dumps(candy_id, default=str)
            return Response(candy_id_json, mimetype="application/json", status=200)
        else:
            return Response("Please enter valid data", mimetype="plain/text", status=400)

    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)


if(len(sys.argv) > 1):
    mode = sys.argv[1]
else:
    print("You must pass a mode to run this python script. Either testing or production")
    exit()

if(mode == "testing"):
    print("Running in testing mode")
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
elif(mode == "production"):
    print("Running in production mode")
    import bjoern  # type: ignore
    bjoern.run(app, "0.0.0.0", 5005)
else:
    print("Please run with either testing or production. Example:")
    print("python3.10 app.py production")
