with open('./in/6.txt') as f:
    text = f.read().strip()

for i in range(4, len(text)):
    if len(set(text[i - 4:i])) == 4:
        print(i)
        break

for i in range(14, len(text)):
    if len(set(text[i - 14:i])) == 14:
        print(i)
        break


# Old solution
"""
from collections import deque

stream = deque(text)
marker = deque([], maxlen=4)
while stream:
    marker.append(stream.popleft())
    if len(set(marker)) == 4:
        break
print(len(text) - len(stream))

stream = deque(text)
marker = deque([], maxlen=14)
while stream:
    marker.append(stream.popleft())
    if len(set(marker)) == 14:
        break
print(len(text) - len(stream))
"""
