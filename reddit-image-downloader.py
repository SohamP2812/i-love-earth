import praw, requests, os, bs4, urllib

def get_images(val):
    temp = int(val)
    temp += 2
    for submission in reddit.subreddit('earthporn').hot(limit=temp):
        print(submission.url)
        url = requests.get(submission.url)
        if submission.url.endswith(('jpg', 'jpeg', 'png')):
            img_data = requests.get(submission.url).content
            with open(os.path.join('redditpics', os.path.basename(submission.url)), 'wb') as handler:
                handler.write(img_data) 
    print("Images have been saved to a folder named 'redditpics' in the current directory. Enjoy 🌎")
    quit()


reddit = praw.Reddit(client_id='********',
                      client_secret='********',
                      user_agent='picture download thing',
                      username='********',
                      password='********'
                      ) 

os.makedirs('redditpics', exist_ok=True) 

val = ""

while val.isnumeric() == False:
    val = input("How many images would you like to be downloaded? ")

    if val.isnumeric():
        get_images(val)

