""" IDEA: The idea behind is the use of the concept that 
if number of edges are more than 2 in the graph, then it 
won't be possible to complete the process, Moreover, if the
connecting edges with length 2 are such that there is a cycle , 
then also it is not possible. Else possible (I know very less cases)
"""

for _ in range(input()):
    n , m = map(int, raw_input().split())
    a = []
    b = []
    for i in range(m):
        t1 , t2 = map(int, raw_input().split())
        a.append(t1)
        b.append(t2)

    if m > 2:
        flag = False
    elif m == 2 and (b[0] == b[1] or a[1] == a[0] or a[0]  == b[1] or b[0] == a[1]):
        flag = False
    else:
        flag = True
    
    if flag :
        print "YES"
    else :
        print "NO"
