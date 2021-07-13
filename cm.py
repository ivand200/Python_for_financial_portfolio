import click
import json
import requests
import csv

@click.command()
@click.option('--index', default='dj30', help='name of the index.')
@click.option('--task', prompt='Enter method(add, show)',  help='add, show.')

def enter(index, task):
    if index == "dj30" and task == "add":
        add(index)
    elif index == "dj30" and task == "show":
        show(index)
    elif index == "sp500" and task == "add":
        add(index)
    elif index == "sp500" and task == "show":
        show(index)
    else:
        print("Something wrong, use --help")



    #elif index == "dj30" and task == "add":
    #    add(index)




def add(index):
    with open(f"{index}.csv", "w", newline='') as f:
        csv_file = csv.writer(f, delimiter=",")
        url = requests.get(f"http://ivand200.pythonanywhere.com/{index}/").json()
        csv_file.writerow(["symbol", "momentum_12_2", "momentum_avg", "E/P"])
        for item in url:
            symbol = item["symbol"]
            momentum = item["momentum_12_2"]
            avg_momentum = item["avg_momentum"]
            ep = item["ep"]
            csv_file.writerow([symbol, momentum, avg_momentum, ep])


def show(index):
    url = requests.get(f"http://ivand200.pythonanywhere.com/{index}/").json()
    #click.echo(url)
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

if __name__ == '__main__':
    enter()
