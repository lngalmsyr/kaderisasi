from stock import Stock

symbols = ['MSFT', 'GOOGL', 'AAPL', 'META']

threads = []

for symbol in symbols:
    t = Stock(symbol)
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
    print(thread)