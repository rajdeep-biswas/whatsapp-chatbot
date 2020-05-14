from random import random, seed, randrange
seed(1)

replies = []
with open('randomreplies.txt', 'r') as f:
    for line in f:
        replies.append(line)

reply = replies[randrange(len(replies))][:-1]
