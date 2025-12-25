import csv
from GambleApp import __path__

def setDeposit(dep=1000):
    with open(__path__+"/config.csv", "r+", newline="") as wallet:
        rows = list(csv.reader(wallet))
        if is_int(rows[1][0]):
            rows[1][0] = dep
        else:
            pass
        wallet.seek(0)
        csv.writer(wallet).writerows(rows)
        wallet.truncate()
