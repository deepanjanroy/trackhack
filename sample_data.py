import datetime
from random import randint

git_repo = {
                "github_url": "https://github.com/DeepanjanRoy/trackhack",
                "contributors": [], # List of users
                "seven_day_stat": [], # List of {user: id, commits: num_commits}
                "total_commits_seven_days": 0,
                "last_updated": datetime.datetime.utcnow(),
                "created": datetime.datetime.utcnow()
            }

{
    "id"
    "NAme"
    "commits"
}

beta_users = [
            {
                "Name": "Alex Norton",
                "facebook_id": "503835850",
                "github_username": "alex-norton",
                "projects": [],
                "seven_day_stat": [ {"_id": None, "num_commits": randint(1,20)}],
                "total_commits_seven_days": 0,
                "last_updated": datetime.datetime.utcnow(),
                "created": datetime.datetime.utcnow()
            },

            {
                "Name": "Deepanjan Roy",
                "facebook_id": "572325542",
                "github_username": "DeepanjanRoy",
                "projects": [],
                "seven_day_stat": [ {"_id": None, "num_commits": randint(1,20)}],
                "total_commits_seven_days": 0,
                "last_updated": datetime.datetime.utcnow(),
                "created": datetime.datetime.utcnow()
            },

            {
                "Name": "Sami Jaber",
                "facebook_id": "762185164",
                "github_username": "samijaber",
                "projects": [],
                "seven_day_stat": [ {"_id": None, "num_commits": randint(1,20)}],
                "total_commits_seven_days": 0,
                "last_updated": datetime.datetime.utcnow(),
                "created": datetime.datetime.utcnow()
            }
        ]
