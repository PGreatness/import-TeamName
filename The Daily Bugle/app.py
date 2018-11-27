from flask import Flask, render_template, request, session, url_for, redirect, flash
import json
import urllib
import ssl
import os
from util import db

app = Flask(__name__)
app.secret_key = os.urandom(32)
# stubs for paths to REST APIs
NEWS_STUB = "https://developers.nytimes.com/svc/topstories/v2/{}.json?api-key={}" # section of news, api key
WEATHER_STUB = "https://api.darksky.net/forecast/{}/{},{}" # api key, longitude, latitude
COMIC_STUB = "http://xkcd.com/{}/info.0.json" # comic number

@app.route('/')
def home():
    # for mac
    context = ssl._create_unverified_context()

    # read json file containing the api keys
    with open('data/API_Keys/keys.json') as json_file:
        json_data = json.loads(json_file.read())
    print(json_data) # should print           {'News': 'api_key', 'Weather': 'api_key', 'Comic': ''}
    print(json_data['News']) #  should print      "api_key"

    # # # # News API
    #
    # n = urllib.request.urlopen(NEWS_STUB.format("home", json_data['News']))
    # news = json.loads(n.read())
    # print ( news["response"]["docs"][0]["headline"]["main"] )

    # # # Weather API
    w = urllib.request.urlopen(WEATHER_STUB.format(json_data['Weather'], 34, -118), context=context) # 34,-118 is LA
    weather = json.loads(w.read())

    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth',methods = ["POST"])
def auth():
    # # # Authenticate
    username_input = request.form.get("username")
    password_input = request.form.get("password")
    all_usernames = dict() # FILL IN
    if username_input in all_usernames:
        hashed_pass = password_input # FILL IN
        if hashed_pass == all_usernames[username_input]:
            # Log them in
            pass
        # Failed password and username match
        pass
    # Username doesnt exist
    flash('wowow')
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.debug = True
    app.run()
