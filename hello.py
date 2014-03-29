import web
import os
from pymongo import MongoClient
client = MongoClient(os.environ.get("TH_MONGO_URL"));
db = client.testdb1
col = db.testData

urls = (
    '/', 'index',
    '/test', 'test'
)

class test:
    def GET(self):
        render = web.template.render('static/test')
        return render.fbauth()

class index:
    # def GET(self):
    # 	database_stuff = list(col.find());
    #     return str(database_stuff);

    def GET(self):
        render = web.template.render('templates')
        return render.index()


# For serving WSGI
wsgi_app = web.application(urls, globals()).wsgifunc()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


