#!python2
#20180721

#staircase challenge hackerrank
def hashes(n):
	r = []
	for x in range(n,0,-1):
		p = (n - x) + 1
		r = x - 1
		print (" " * r) + ("#" * p)

hashes(5)

#min max sum hackerrank
def function(n):
    p = 1
    for x in range(1,n+1):
        p *= x
    return p
print function(25)
        
#chocolate challenge
def reducing02(n,c,m):
    n = n / c
    c = n
    if c < m:
        return n
    else:
        while c >= m:
            n = n + (c / m)
            c = c + (c / m ) - ((c / m ) * m)
        else:
            return n
#diagonal sums difference challenge
def diagonalsums(a):
    sum1 = 0
    sum2 = 0
    for x in a:
        if x == a[0]:
            sum1 = x[0] + a[1][1] + a[2][2]
        elif x == a[2]:
            sum2 = x[2] + a[1][1] + a[0][2]
    return sum1,sum2

def sums(a):
    o = a[0]
    t = a[1]
    th = a[2]
    sum = (o[0] + t[1] + th[2]) - (o[2] + t[1] + th[0])
    if sum == 0:
        return sum
    elif sum < 0:
        count += len(range(sum,0))
        return count                                    

"""
def difference(sums):
    return sums[0] - sums[1]
"""

print reducing02(6,2,2)
print reducing02(10,2,5)
print reducing02(7,3,2)
print reducing02(12,4,4)
print
array = [[1,2,3],[1,2,3],[1,2,3]]
#print difference(diagonalsums(array))
print diagonalsums(array)
print sums(array)
