def run(chooser,nbrOfPart,stream,vPP):
    comp = []
    #run a partitions streaming chooser on file of hyperEdge
    partitions = [[]for i in range(nbrOfPart)]
    l = len(stream)
    for i,hedge in enumerate(stream):
        pos = chooser(hedge,partitions,vPP)
        partitions[pos].append(hedge)
        for vertex in hedge:
            vPP[pos].add(vertex)
        if i%1000 == 0:
            print("Percent done: " + str(float(i)/l*100))
    return(partitions)
