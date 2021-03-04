import praw 

reddit = praw.Reddit(client_id = "_oSU2eKnmJbGYw",
	                  client_secret = "OdjV6UM2VG1jYSiUt3pVexRAAyZHDA",
	                  username = "EpiczlolYt",
	                  password = "Edwin2007$",
	                  user_agent = "pythonpraw")

subreddit = reddit.subreddit("memes")


top = subreddit.top(limit = 5)
for submission in top:
	print(submission.title)
	        
