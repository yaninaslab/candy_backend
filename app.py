import dbinteractions as dbi
from flask import Flask, request, Response
import json

import sys

app = Flask(__name__)


@app.get('/candy')
def list_all_candies():
    try:
        candies = dbi.list_all_candies()
        candies_json = json.dumps(candies, default=str)
        return Response(candies_json, mimetype="application/json", status=200)
    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)


@app.post('/candy')
def add_new_candy():
    try:
        name = request.json['name']
        description = request.json['description']
        image_url = request.json['image_url']
        new_candy = dbi.add_new_candy(name, description, image_url)
        if(new_candy == True):
            new_candy_json = json.dumps(new_candy, default=str)
            return Response(new_candy_json, mimetype="application/json", status=200)
        else:
            return Response("Please enter valid data", mimetype="plain/text", status=400)

    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)


@app.patch('/candy')
def update_candy():
    try:
        candy_id = request.json['candy_id']
        candy_id = dbi.update_candy(candy_id)
        if(candy_id == True):
            candy_id_json = json.dumps(candy_id, default=str)
            return Response(candy_id_json, mimetype="application/json", status=200)
        else:
            return Response("Please enter valid data", mimetype="plain/text", status=400)
    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)


@app.delete('/candy')
def delete_candy():
    try:
        candy_id = request.json['candy_id']
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
