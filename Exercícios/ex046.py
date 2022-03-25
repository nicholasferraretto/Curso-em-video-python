from emoji import emojize
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)

print(emojize(':sparkler:' * 60, use_aliases=True))
