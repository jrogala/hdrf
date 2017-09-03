eps = 1
rho = 1.1
maxsize = 0
minsize = 0
lamb = 1.01
partdeg = {}
s = 0

def updatepartdeg(hedge):
    for vertex in hedge:
        partdeg[vertex] = partdeg[vertex] + 1

def teta(vertex,hedge):
    d = 0.0
    for v in hedge:
        d += partdeg[v]
    s = partdeg[vertex]/d
    return s

def g(vertex,hedge,vpp,i):
    if vertex in vpp[i]:
        return(1+1-teta(vertex,hedge))
    return 0

def CgreedyBal(part):
    n = maxsize - len(part)
    d = eps + maxsize - minsize
    return (n/d)

def CHDRFeREP(hedge,vpp,i):
    s = 0.0
    for vertex in hedge:
        s += g(vertex,hedge,vpp,i)
    return s

def CHDRFe(hedge,part,vpp,i):
    part1 = CHDRFeREP(hedge,vpp,i)
    part2 = CgreedyBal(part)
    # print(" " + str(part1) + " " +str(part2))
    return part1 + lamb*part2


def init(vertexs,numberOfPartitions,stream):
    for vertex in vertexs:
        partdeg[vertex] = 0.0

def chooseEdge(hedge,partitions,vpp,_lamb=5,_eps=1.1,_rho=1.1):
    #return a the number of the partition where edge should go
    global lamb
    global eps
    global rho
    global maxsize
    global minsize
    lamb = _lamb
    eps = _eps
    rho = _rho
    buff = -1
    scoreBuff = -1
    updatepartdeg(hedge)
    for i,part in enumerate(partitions):
        scoreloc = CHDRFe(hedge,part,vpp,i)
        if scoreloc > scoreBuff:
            buff = i
            scoreBuff = scoreloc
        if len(vpp[i])>maxsize:
            maxsize += 1
    for part in vpp:
        minsize = min(minsize,len(part))
    return buff
