#Silas Clymer, 3/1/21
#This is a solver for the "closest points" problem
#Portions of this code were adapted from various sources
import math

#Brute force algorithm -- O(n^2) time
#This algorithm assumes that no 2 points are the same
def brute_closest(points):
    
    pair = (None, None)
    mini = float('inf')
    for a in points:
        for b in points:
            if a != b:
                d = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
                if d < mini:
                    pair = (a,b)
                    mini = d
                    
    return(pair, mini)


#Better algorithm -- O(n*log(n)) time
#This algorithm assumes that no 2 points have the same x- or y-value
def better_closest(points):

    def xsort(points):
        return sorted(points, key=lambda tup: tup[0])
    
    def ysort(points):
        return sorted(points, key=lambda tup: tup[1])
    
    Px = xsort(points)
    Py = ysort(points)

    def closest_pair_rec(Px, Py):
        if len(Px)>1:
            pair = (None, None)
            mini = float('inf')
            if len(Px) <= 3:
                for a in Px:
                    for b in Px:
                        if a != b:
                            d = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
                            if d < mini:
                                pair = (a,b)
                                mini = d
                best = (pair,mini)
                return best
            
            mid = math.ceil(len(Px)/2)
            Q = Px[:mid]
            R = Px[mid:]
            Qx = Q
            Qy = [p for p in Py if p in Q]
            Rx = R
            Ry = [p for p in Py if p in R]
            qbest = closest_pair_rec(Qx, Qy)
            rbest = closest_pair_rec(Rx, Ry)
            
            delta = min(qbest[1],rbest[1])
            L = Q[-1][0]
            S = [p for p in Px if abs(p[0]-L) < delta]

            Sy = [p for p in Py if p in S]
            for i in range(len(S)):
                a = Sy[i]
                j = i
                while j <= i+15 and j < len(S)-1:
                    j += 1
                    b = Sy[j]
                    d = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
                    if d < mini:
                        pair = (a,b)
                        mini = d
            sbest = (pair, mini)

            if sbest[1] < delta:
                return sbest
            elif qbest[1] < rbest[1]:
                return qbest
            else:
                return rbest

    pbest = closest_pair_rec(Px,Py)
    return pbest




P = [(9,2),(2,7),(1,8),(4,3),(5,1),(7,4),(8,6),(3,5),(6,9)]

print('O(n^2):')
print(brute_closest(P))

print('O(n*log(n)):')
print(better_closest(P))

