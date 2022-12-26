import re
from collections import deque, defaultdict
from functools import lru_cache


with open('./in/16.txt') as f:
    lines = f.read().strip().splitlines()

graph = defaultdict(set)
flows = defaultdict(lambda: 0)
distances = defaultdict(dict)
start_distances = {}

for line in lines:
    valve, *tunnels = re.findall(r'[A-Z]{2}', line)
    graph[valve] = set(tunnels)
    flow = int(re.findall(r'\d+', line)[0])
    flows[valve] = flow

for start, flow in flows.items():
    if flow == 0:
        continue
    visited = {start}
    q = deque([(start, 0)])
    while q:
        curr, distance = q.popleft()
        if flows[curr]:
            distances[start][curr] = distance
        if curr == 'AA':
            start_distances[start] = distance
        for neighbor in graph[curr]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            q.append((neighbor, distance + 1))


T = 30
q = deque()
pressures = {}
for curr, distance in start_distances.items():
    t = distance + 1
    if t >= T:
        continue
    key = (curr, (curr,), t)
    pressures[key] = (T - t) * flows[curr]
    q.append((key, pressures[key]))
while q:
    start_key, base_pressure = q.pop()
    if base_pressure < pressures[start_key]:
        continue
    assert base_pressure == pressures[start_key]
    curr, opened, t = start_key
    opened_set = set(opened)
    for neighbor, distance in distances[curr].items():
        if neighbor in opened_set:
            continue
        t1 = t + distance + 1
        if t1 >= T:
            continue
        key = (neighbor, tuple(sorted((*opened, neighbor))), t1)
        pressure = base_pressure + (T - t1) * flows[neighbor]
        if pressures.get(key, 0) < pressure:
            pressures[key] = pressure
            q.append((key, pressure))

print(max(pressures.values()))


T = 26

valves = sorted(start_distances.keys())
indexes = {valve: i for i, valve in enumerate(valves)}

def toggle_valve(bitmap, valve):
    return bitmap ^ (1 << indexes[valve])

def gen_open_valves(bitmap):
    for valve in valves:
        if bitmap & 1:
            yield valve
        bitmap >>= 1

def get_added_pressure(valve, t):
    return (T - t) * flows[valve]

@lru_cache(maxsize=None)
def dfs_pressure(p1, t1, p2, t2, bitmap):
    assert t1 <= t2
    if t1 >= T:
        return 0
    best = 0
    for valve in gen_open_valves(bitmap):
        t4 = t1 + distances[p1][valve] + 1
        if t4 >= T:
            continue
        p4 = valve
        pressure = get_added_pressure(p4, t4)
        bm = toggle_valve(bitmap, valve)
        t3 = t2
        p3 = p2
        if t4 < t3:
            t3, t4 = t4, t3
            p3, p4 = p4, p3
        pressure += dfs_pressure(p3, t3, p4, t4, bm)
        best = max(best, pressure)
    return best

q = deque()
bitmap = 2 ** len(valves) - 1
best = 0
for p1, d1 in start_distances.items():
    for p2, d2 in start_distances.items():
        if p1 == p2 or d1 > d2 or (d1 == d2 and p1 < p2):
            continue
        t1, t2 = d1 + 1, d2 + 1
        if t1 >= T or t2 >= T:
            continue
        bm = toggle_valve(toggle_valve(bitmap, p1), p2)
        pressure = get_added_pressure(p1, t1) + get_added_pressure(p2, t2)
        pressure += dfs_pressure(p1, t1, p2, t2, bm)
        best = max(best, pressure)

print(best)
