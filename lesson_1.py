def strcounter (data):
    counter = {}
    for sym in data:
        counter[sym] = counter.get(sym,0) + 1
        print(counter)

strcounter('fffggghgheyg')