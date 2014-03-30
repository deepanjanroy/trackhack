import web, json, urllib2, requests

github_client_id = MongoClient(os.environ.get("GITHUB_CLIENT_ID"))
github_secret_id = MongoClient(os.environ.get("GITHUB_SECRET_ID"))
        
urls = (
    '/logged', 'logged',
    '/create', 'create',
    '/', 'index'
)
app = web.application(urls, globals())

class create:
	def GET(self):
		user_data = web.input()
		repoName = json.dumps({"name": user_data.name})
		
		req = urllib2.Request("https://api.github.com/user/repos?access_token=" + user_data.access_token, repoName, {'Content-Type': 'application/json'})
		f = urllib2.urlopen(req)
		response = f.read()
		f.close()
		return "HAHAHA"

class logged:
	def GET(self):
		user_data = web.input()
		url = urllib2.urlopen("https://github.com/login/oauth/access_token", "scope=user,repo&client_id=" + github_client_id + "&client_secret=" + github_secret_id + "&code=" + user_data.code)		
		resp = url.read().replace('=', '&').split('&')
		access_token = resp[1]
		render = web.template.render('.')
		return render.repo(access_token)

class index:        
    def GET(self):
		render = web.template.render('.')
		return render.repo(github_client_id)

if __name__ == "__main__":
    app.run()