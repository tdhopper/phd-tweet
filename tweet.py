import random
import time
import os
import twitter as tw
import schedule

content = ["Maybe", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No",
           "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No",
           "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "Probably not",
           "Probably not", "Probably not", "Should I Do a Ph.D.? @ansate answers http://stiglerdiet.com/blog/2013/Sep/05/should-i-do-a-phd-melissa-santos/",
           "Should I Do a Ph.D.? @johndcook answers http://stiglerdiet.com/blog/2013/Aug/22/should-i-do-a-Ph.D.-john-d-cook/",
           "Should I Do a Ph.D.? @lauramclay answers http://stiglerdiet.com/blog/2013/Sep/19/should-i-do-a-phd-laura-mclay/",
           "Should I Do a Ph.D.? @michaelnute answers http://stiglerdiet.com/blog/2014/Jan/20/should-i-do-a-phd-mike-nute/",
           "Should I Do a Ph.D.? @parubin answers http://stiglerdiet.com/blog/2013/Aug/25/should-i-do-a-phd-paul-rubin/",
           "Should I Do a Ph.D.? @posco answers http://stiglerdiet.com/blog/2014/Jan/29/should-i-do-a-phd-oscar-boykin/",
           "Should I Do a Ph.D.? @profpaulharper answers http://stiglerdiet.com/blog/2013/Sep/17/should-i-do-a-phd-paul-harper/",
           "Should I Do a Ph.D.? @slendrmeans answers http://stiglerdiet.com/blog/2013/Sep/03/should-i-do-a-phd-carl-vogel/",
           "Should I Do a Ph.D.? @stochastician answers http://stiglerdiet.com/blog/2013/Aug/27/should-i-do-a-phd-eric-jonas/",
           "Unlikely", "Unlikely", "Unlikely"]

cred = {
    "consumer_key": os.environ['PHD_CONSUMER_KEY'],
    "consumer_secret": os.environ['PHD_CONSUMER_SECRET'],
    "token": os.environ['PHD_TOKEN'],
    "token_secret": os.environ['PHD_TOKEN_SECRET'],
}


def tweet():
    auth = tw.OAuth(**cred)
    t = tw.Twitter(auth=auth)
    status = random.choice(content)
    t.statuses.update(status=status)

schedule.every(895).minutes.do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
