import random
import time
import os
import twitter as tw
import schedule

content = ["Maybe"] \
    + ["No"] * 20 \
    + ["Probably not"] * 3 \
    + ["Unlikely"] * 3 \
    + ["Should I Do a Ph.D.? @ansate answers http://shouldigetaphd.com/#santos",
       "Should I Do a Ph.D.? @johndcook answers http://shouldigetaphd.com/#cook",
       "Should I Do a Ph.D.? @lauramclay answers http://shouldigetaphd.com/#mclay",
       "Should I Do a Ph.D.? @michaelnute answers http://shouldigetaphd.com/#nute",
       "Should I Do a Ph.D.? @parubin answers http://shouldigetaphd.com/#rubin",
       "Should I Do a Ph.D.? @posco answers http://shouldigetaphd.com/#boykin",
       "Should I Do a Ph.D.? @profpaulharper answers http://shouldigetaphd.com/#harper",
       "Should I Do a Ph.D.? @slendrmeans answers http://shouldigetaphd.com/#vogel",
       "Should I Do a Ph.D.? @stochastician answers http://shouldigetaphd.com/#jonas"]

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

schedule.every(1111).minutes.do(tweet)

tweet()
while True:
    schedule.run_pending()
    time.sleep(1)
