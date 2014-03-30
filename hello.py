import web
import os
from pymongo import MongoClient
client = MongoClient(os.environ.get("TH_MONGO_URL"));
db = client.testdb1
col = db.testData

urls = (
    '/', 'index',
    '/test', 'test',
	'/enter', 'authenticate'
)

render = web.template.render('templates/')


class test:
    def GET(self):
        render = web.template.render('static/test')
        return render.fbauth()


class authenticate:
	def GET(self):
		#double authentication across the skyyyy

		render = web.template.render('templates/')
		return render.enter()
		#wow wooooow so intense


# For serving WSGI
wsgi_app = web.application(urls, globals()).wsgifunc()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


