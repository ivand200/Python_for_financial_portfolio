import json
import sys
import click
import requests


@click.command()
@click.option('--index', default="dj30", help='Please enter index name')


def rest(index):
    try:
        """Get Momentum_12_2 list"""
        url = requests.get(f"http://ivand200.pythonanywhere.com/{index}/").json()
        lst = list()
        for item in url:
            symbol = item["symbol"]
            name = item["name"]
            momentum = item["momentum_12_2"]
            newtuple = symbol, name, momentum
            lst.append(newtuple)
        #lst.sort(key=sort_mom, reverse=True)
        short_lst = lst[:20]
        best_list = "\n".join(str(el) for el in short_lst)
        best_20 = best_list.replace("(","").replace(")","").replace("'", "")
        print(best_20)
    except:
        print("Something wrong!. Use dj30 or sp500")



if __name__ == '__main__':
    rest()
