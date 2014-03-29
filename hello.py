import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

# For serving WSGI
wsgi_app = web.application(urls, globals()).wsgifunc()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


