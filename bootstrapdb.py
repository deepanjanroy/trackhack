import web
import os
from sample_data import git_repo, beta_users
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
proj_id = projects.insert(git_repo)

for u in beta_users:
    u["projects"] = [proj_id]
    u["seven_day_stat"][0]["_id"] = proj_id


inserted_users = users.insert(beta_users)
stat7proj = []
for u in inserted_users:
    stat7proj.append({"_id": u, "num_commits":randint(1,20)})
print stat7proj

projects.update({"_id": proj_id},{"$set": {"contributors": inserted_users, "seven_day_stat": stat7proj}})
