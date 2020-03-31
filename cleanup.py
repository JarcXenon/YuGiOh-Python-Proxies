import os

l = {"decklist.txt", "decklist.ydk"}

for t in l:
    if os.path.exists(t):
        os.remove(t)
