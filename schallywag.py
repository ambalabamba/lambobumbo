import threading
import requests
import random

def spam():
    threading.Timer(0.001, spam).start()
    String = "!#$%&'()*+,-./00300123456789:;<=>?0040@ABCDEFGHIJKLMNO0050PQRSTUVWXYZ[\]^_0060`abcdefghijklmno0070pqrstuvwxyz{|}~␡0080009000A0 ¡¢£¤¥¦§¨©ª«¬ ®¯00B0°±²³´µ¶·¸¹º»¼½¾¿00C0ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏ00D0ÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß00E0àáâãäåæçèéêëìíîï00F0ðñòóôõö÷øùúûüýþÿ0100ĀāĂăĄąĆćĈĉĊċČčĎď0110ĐđĒēĔĕĖėĘęĚěĜĝĞğ0120ĠġĢģĤĥĦħĨĩĪīĬĭĮį0130İıĲĳĴĵĶķĸĹĺĻļĽľĿ0140ŀŁłŃńŅņŇňŉŊŋŌōŎŏ0150ŐőŒœŔŕŖŗŘřŚśŜŝŞş0160ŠšŢţŤťŦŧŨũŪūŬŭŮů0170ŰűŲųŴŵŶŷŸŹźŻżŽžſ0180ƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏ0190ƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟ01A0ƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯ01B0ưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿ01C0ǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏ01D0ǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟ01E0ǠǡǢǣǤǥǦǧǨǩǪǫǬǭǮǯ01F0ǰǱǲǳǴǵǶǷǸǹǺǻǼǽǾǿ"
    requests.get("http://api.xgenstudios.com/?method=xgen.stats.submit&username=weathernowdays&password=lol&game_id=TW3&stat_id=!#$%&'()*+,-./00300123456789:;<=>?0040@ABCDEFGHIJKLMNO0050PQRSTUVWXYZ[\]^_0060`abcdefghijklmno0070pqrstuvwxyz{|}~␡0080&value=100000000")
spam()
