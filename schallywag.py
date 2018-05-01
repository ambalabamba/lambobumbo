import threading
import requests
import random

def spam():
    threading.Timer(0.1, spam).start()
    List = ['http://discourse.xgenstudios.com/t/forum-staff-impersonation/1579', 'http://discourse.xgenstudios.com/t/a-new-stick-rpg-is-what-we-all-want/1588', 'http://discourse.xgenstudios.com/t/season-1-discussion/1547']
    url = "".join(random.choice(List))
    requests.get(url)       
spam()
