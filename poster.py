import facebook
import sys

#rather than args can we load sessionKey and pageID from Heroku ENV VARS?

#all args are strings
# can expand with text attachments and "custom stories" if we really want
def makeTextPost(sessionKey, pageID, content):
	graph = facebook.GraphAPI(sessionKey)
	graph.put_object(pageID, "feed", message=content)
	
if __name__ == "__main__":
	makeTextPost(sys.argv[1], sys.argv[2], sys.argv[3])