import sys
import requests
import json

index = sys.argv[1]
index = str(index)


def get_avg_momentum(index):
    try:
        """Get Momentum_12_2 list"""
        url = requests.get(f"http://ivand200.pythonanywhere.com/{index}/").json()
        lst = list()
        count = 0
        for item in url:
            symbol = item["symbol"]
            name = item["name"]
            momentum = item["avg_momentum"]
            newtuple = symbol, name, momentum
            lst.append(newtuple)
        #lst.sort(key=sort_mom, reverse=True)
        short_lst = lst[:20]
        best_list = "\n".join(str(el) for el in short_lst)
        best_20 = best_list.replace("(","").replace(")","").replace("'", "")
        return best_20
    except:
        return "Something wrong!. Use dj30 or sp500"


if index == "sp500":
    print(get_avg_momentum("sp500"))
elif index == "dj30":
    print(get_avg_momentum("dj30"))
else:
    print("Something wrong!. Use dj30 or sp500")
