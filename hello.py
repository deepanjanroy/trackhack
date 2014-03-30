import web
import os
import urllib2
from pymongo import MongoClient
client = MongoClient(os.environ.get("TH_MONGO_URL"));
db = client.testdb1
col = db.testData

github_client_id = os.environ.get("GITHUB_CLIENT_ID")
github_secret_id = os.environ.get("GITHUB_SECRET_ID")

urls = (
    '/test', 'test',
    '/enter', 'authenticate',
    '/login_success', 'login_success',
)

render = web.template.render('templates/')


class login_success:
    def POST(self):
        data = web.data()
        print data
        return 0


class test:
    def GET(self):
        render = web.template.render('static/test')
        return render.fbauth()


class authenticate:
    def GET(self):
        render = web.template.render('templates')
        user_data = web.input()
        if hasattr(user_data, "code"):
            url = urllib2.urlopen("https://github.com/login/oauth/access_token", "scope=user,repo&client_id=" + github_client_id + "&client_secret=" + github_secret_id + "&code=" + user_data.code)
            resp = url.read().replace('=', '&').split('&')
            access_token = resp[0]
            # from IPython import embed; embed()
            return render.enter(github_client_id, access_token, "true")

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


