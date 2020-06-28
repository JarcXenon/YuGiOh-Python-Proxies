import os

l = {"decklist.txt", "decklist.ydk", "cards.tex", "proxies.pdf"}

for t in l:
    if os.path.exists(t):
        os.remove(t)
