import web
import os
import urllib2
import requests
import requests
import json
from pymongo import MongoClient
from bson import json_util
client = MongoClient(os.environ.get("TH_MONGO_URL"));
db = client.trackhackdb

github_client_id = os.environ.get("GITHUB_CLIENT_ID")
github_secret_id = os.environ.get("GITHUB_SECRET_ID")

urls = (
    '/', 'authenticate',
    '/test', 'test',
    '/login_success', 'login_success',
    '/userhome', 'userhome',
    '/api/user_profile/fb/(.*)', 'user_profile'
)

render = web.template.render('templates/')

class user_profile:
    def GET(self, facebook_id):
        user = db.users.find_one({"facebook_id": facebook_id})
        if user is not None:
            return json_util.dumps(user)
        else:
            return "false"

class userhome:
    def GET(self):
        return render.userhome("","","")


class login_success:
    def POST(self):
        data = web.data()
        print data
        return 0


class test:
    def GET(self):
        render = web.template.render('https://s3.amazonaws.com/trackhack/static/test')
        return render.fbauth()


class authenticate:
    def GET(self):
        render = web.template.render('templates')
        user_data = web.input()
        if hasattr(user_data, "code"):

            payload = {"client_id": github_client_id, "client_secret": github_secret_id, "code": user_data.code}
            headers = {"content-type": "application/json"}
            url = "https://github.com/login/oauth/access_token"
            r = requests.post(url, json.dumps(payload), headers=headers)
            access_token_line = r.text

            url = "https://api.github.com/user?" + access_token_line
            r = requests.get(url)
            github_username = r.json()['login']
            return render.enter(github_client_id, github_username, "true")

        return render.enter(github_client_id, "", "false")

class logged:
    def GET(self):
        user_data = web.input()
        url = urllib2.urlopen("https://github.com/login/oauth/access_token", "scope=user,repo&client_id=" + github_client_id + "&client_secret=" + github_secret_id + "&code=" + user_data.code)
        resp = url.read().replace('=', '&').split('&')
        access_token = resp[1]
        render = web.template.render('templates')
        return render.enter(github_client_id, access_token)

class create:
    def GET(self):
        user_data = web.input()
        repoName = json.dumps({"name": user_data.name})

        req = urllib2.Request("https://api.github.com/user/repos?access_token=" + user_data.access_token, repoName, {'Content-Type': 'application/json'})
        f = urllib2.urlopen(req)
        response = f.read()
        f.close()
        return "HAHAHA"


# For serving WSGI
wsgi_app = web.application(urls, globals()).wsgifunc()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


