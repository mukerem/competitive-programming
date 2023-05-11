# https://open.kattis.com/problems/workstations
# Time: 2022-07-19 18:13:17
# title: Assigning Workstations
# language: Python 3


from heapq import heappop, heappush

def saves(arrivals, departures, m):
    saves = 0
    while arrivals:
        arrival = heappop(arrivals)
        while arrival - departures[0] > m:
            heappop(departures)
        if departures[0] <= arrival:
            heappop(departures)
            saves += 1
    return saves

def main():
    n,m = map(int,input().split())
    arrivals, departures = [], []
    for _ in range(n):
        a,b = map(int,input().split())
        heappush(arrivals, a)
        heappush(departures, a+b)
    print(saves(arrivals, departures, m))


if __name__ == "__main__":
    main()