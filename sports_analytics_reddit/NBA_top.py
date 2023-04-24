
import praw
import pandas as pd
from sympy import limit

reddit = praw.Reddit(client_id="9brjanq9xg9P6WS-5I6UMw", client_secret="J3tRlZnusp4D--9MKhKRFFOFoUWYGA", user_agent="Web_scraper (by /u/Excellent-Ad-3452)")

appended_data = []

Input = "NBA"
subreddit = reddit.subreddit(Input)  

top_python = subreddit.hot(limit=10)    

for submission in top_python:

    if not submission.stickied:

        appended_data.append(submission.url)


print(appended_data)

combined = list(appended_data)
# # Export to CSV
df = pd.DataFrame(combined)
df.columns = [Input]
df.to_csv('topNBA.csv', index=False)
