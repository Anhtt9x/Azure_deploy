import urllib.error
from flask import Flask, render_template, request
import urllib.request
import json
import os


app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def handle_form():
    if request.method == "POST":
        query = request.form.get("user-input")
        data = {"query":f"{query}"}

        body = str.encode(json.dumps(data))

        url = ""

        api_key = ""

        if not api_key:
            raise Exception("A key should be provided to invoke the endpoint")
        
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'myliveproject-yqwte-1' }

        req = urllib.request.Request(url,body,headers)

        try:
            response = urllib.request.urlopen(req)
            result = response.read()

            result_json = json.loads(result.decode('utf-8'))
            reply = result_json['reply']

            return render_template("chatbot.html",reply)

        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))
            print(error.info())
            print(error.read().decode('utf-8','ignore'))
    
    else:
        return render_template("chatbot.html")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port="8000")  # Run the Flask app in debug mode