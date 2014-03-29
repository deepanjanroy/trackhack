import facebook
import sys
import os
import time
from datetime import datetime


#all args are strings
# can expand with text attachments and "custom stories" if we really want

sessionKey = os.environ['FB_SESSION_KEY']
pageID = os.environ['FB_PAGE_ID']
graph = facebook.GraphAPI(sessionKey)
def makeTextPost(content):
	graph.put_object(pageID, "feed", message=content)

if __name__ == "__main__":
	interval = int(sys.argv[1])
	makeTextPost("py post at time " + str(datetime.now()))
	while True:
		time.sleep(interval)
		makeTextPost("py post at time " + str(datetime.now()))