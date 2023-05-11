# https://open.kattis.com/problems/dartscoring
# Time: 2022-09-04 13:01:59
# title: Dart Scoring
# language: Python 3


def Left_index(points):
    minn = 0
    for i in range(1,len(points)):
        if points[i][0] < points[minn][0]:
            minn = i
        elif points[i][0] == points[minn][0]:
            if points[i][1] > points[minn][1]:
                minn = i
    return minn
 
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])
 
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2
 
def convexHull(points, n):
     
    if n < 3:
        return
    l = Left_index(points)
 
    hull = []
    
    p = l
    q = 0
    while(True):
        hull.append(p)
        q = (p + 1) % n
 
        for i in range(n):
            if(orientation(points[p],
                           points[i], points[q]) == 2):
                q = i
        p = q
 
        if(p == l):
            break
    return hull
    
while 1:
    try:
        points = []
        x = list(map(float, input().split()))
        
        for i in range(0, len(x), 2):
            points.append((x[i], x[i+1]))
        n = len(points)
        
        if n == 1:
            print("100.0000000000")
            continue
        
        if n == 2:
            s = (points[0][0] - points[1][0]) **2 + (points[0][1] - points[1][1]) ** 2
            s = 2 * s ** 0.5
            print(f'%.11f' % (200 / (1+s)))
            continue
        
        
        h = convexHull(points, n)
        p = []
        for each in h:
            p.append(points[each])
        m = len(p)
        s = 0
        for i in range(m):
            d = (p[i][0] - p[(i+1)%m][0]) **2 + (p[i][1] - p[(i+1)%m][1]) ** 2
            d = d ** 0.5
            s += d
        print(f'%.11f' % (100 * n / (1+s)))
    except EOFError:
        break
