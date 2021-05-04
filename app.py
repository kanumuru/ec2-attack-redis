from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)
data =[]

import redis
redisClient = redis.StrictRedis(host="127.0.0.1",port=6379,db=0,decode_responses=True)

@app.route("/", methods=["GET","POST"])
def get_email():
    if request.method == "GET":

        return render_template("email.html")

    if request.method == "POST":
        if request.form.get("email"):
            query = "email*"
            keys = redisClient.keys(query)
            for j in keys:
                if redisClient.get(j) == request.form.get("email"):
                    return render_template("email.html")
            if len(keys)<=0:
                keyid=1
            else:
                keyid=len(keys)+1
            count="email"+str(keyid)
            redisClient.set(count, request.form.get("email"))
        email = request.form.get("email")
        print(email)
        
        return render_template("email.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
