import datetime as dt
from random import randint

curDT = dt.datetime.utcnow()
randTime = dt.datetime.utcnow()
randEarlierTime = dt.datetime.utcnow()

def randDt():
	randDelta = dt.timedelta(days=randint(-20,0),hours=randint(-24,0),minutes=randint(-60,0),seconds=randint(-60,0))
	randTime = curDT + randDelta
	return randTime
	
def randEarlierDt():
	randDelta = dt.timedelta(days=randint(-20,0),hours=randint(-24,0),minutes=randint(-60,0),seconds=randint(-60,0))
	randEarlierTime = randTime + randDelta
	return randEarlierTime

git_repos = [
			{
                "github_url": "https://github.com/DeepanjanRoy/trackhack",
                "contributors": [], # List of users
                "seven_day_stat": [], # List of {user: id, commits: num_commits}
                "total_commits_seven_days": 0,
                "last_updated": randDt(),
                "created": randEarlierDt()
            },
			
			{
				"github_url": "https://github.com/alex-norton/fsharp-taocp",
                "contributors": [], # List of users
                "seven_day_stat": [], # List of {user: id, commits: num_commits}
                "total_commits_seven_days": 0,
                "last_updated": randDt(),
                "created": randEarlierDt()
			},
			
			{
				"github_url": "https://github.com/hackmcgill/website",
                "contributors": [], # List of users
                "seven_day_stat": [], # List of {user: id, commits: num_commits}
                "total_commits_seven_days": 0,
                "last_updated": randDt(),
                "created": randEarlierDt()
			},
				
			{
				"github_url": "https://github.com/mkgorshkov/Pass-Keep",
                "contributors": [], # List of users
                "seven_day_stat": [], # List of {user: id, commits: num_commits}
                "total_commits_seven_days": 0,
                "last_updated": randDt(),
                "created": randEarlierDt()
			},
			
			{
				"github_url": "https://github.com/wetmore/MathGenius",
                "contributors": [], # List of users
                "seven_day_stat": [], # List of {user: id, commits: num_commits}
                "total_commits_seven_days": 0,
                "last_updated": randDt(),
                "created": randEarlierDt()
			}
			]
			

#{
#    "id"
#    "NAme"
#    "commits"
#}

beta_users = [
            {
                "Name": "Alex Norton",
                "facebook_id": "503835850",
                "github_username": "alex-norton",
                "projects": [],
                "seven_day_stat": [ {"_id": None, "num_commits": randint(1,20)}], #list of projects and their commits
                "total_commits_seven_days": 0,
                "last_updated": randDt(),
                "created": randEarlierDt()
            },

            {
                "Name": "Deepanjan Roy",
                "facebook_id": "572325542",
                "github_username": "DeepanjanRoy",
                "projects": [],
                "seven_day_stat": [ {"_id": None, "num_commits": randint(1,20)}],
                "total_commits_seven_days": 0,
                "last_updated": randDt(),
                "created": randEarlierDt()
            },

            {
                "Name": "Sami Jaber",
                "facebook_id": "762185164",
                "github_username": "samijaber",
                "projects": [],
                "seven_day_stat": [ {"_id": None, "num_commits": randint(1,20)}],
                "total_commits_seven_days": 0,
                "last_updated": randDt(),
                "created": randEarlierDt()
            },
			
			{
				"Name": "Maxim Gorshkov",
				"facebook_id": "1069405217",
				"github_username": "mkgorshkov",
				"projects": [],
				"seven_day_stat": [ {"_id": None, "num_commits": randint(1,20)}],
                "total_commits_seven_days": 0,
                "last_updated": randDt(),
                "created": randEarlierDt()
			},
			
			{
				"Name:": "Daphnne Chacon",
				"facebook_id": "1378550369",
				"github_username": "daphchacon",
				"projects": [],
				"seven_day_stat": [ {"_id": None, "num_commits": randint(1,20)}],
                "total_commits_seven_days": 0,
                "last_updated": randDt(),
                "created": randEarlierDt()
			}
        ]
