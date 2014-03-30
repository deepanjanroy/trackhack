import web
import os
from sample_data import git_repos, beta_users
from pymongo import MongoClient
from random import randint

client = MongoClient(os.environ.get("TH_MONGO_URL"));
db = client.trackhackdb

projects = db.projects
users = db.users

print "Cleaning up database"
print projects.remove()
print users.remove()


print "Adding sample data"
proj_ids = projects.insert(git_repos)


for u in beta_users:
	total_coms = 0
	for v in proj_ids:
		if randint(0,1):
			u["projects"].append(v)
			u["seven_day_stat"].append({"_id": v, "num_commits": randint(1,20)})
			total_coms += u["seven_day_stat"][-1]["num_commits"] #most recent commit count
	u["total_commits_seven_days"] = total_coms
	
user_ids = users.insert(beta_users)

for u in proj_ids:
	stat7proj = []
	inserted_users = []
	total_coms = 0
	for v in user_ids:
		if randint(0,1):
			stat7proj.append({"_id": v, "num_commits":randint(1,20)})
			inserted_users.append(v)
			total_coms += stat7proj[-1]["num_commits"] #most recently added commit cou t
	projects.update({"_id": u},{"$set": {"contributors": inserted_users, "seven_day_stat": stat7proj, "total_commits_seven_days": total_coms}})


