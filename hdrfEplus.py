eps = 1
rho = 1.1
maxsize = 0
minsize = 0
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
    return CHDRFeREP(hedge,vpp,i) + len(hedge)*CgreedyBal(part)/2


def init(vertexs,numberOfPartitions,stream):
    global maxsize
    global minsize
    for vertex in vertexs:
        partdeg[vertex] = 0
    for i, l in enumerate(stream):
        pass
    card = i+1
    s = float(card)/numberOfPartitions
    maxsize = int(rho*s)
    minsize = int((1/rho)*s)

def chooseEdge(hedge,partitions,vpp,_eps=1.1,_rho=1.1):
    #return a the number of the partition where edge should go
    global eps
    global rho
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
    return buff
