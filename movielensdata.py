import sys

def writing(g,line):
    g.write(str(line)+"\n")

def main(file):
    with open("raw data/" + file,'r') as f:
        with open("data/"+file[:-8]+".data",'w') as g:
            buff = ["" for i in range(2)]
            for i,line in enumerate(f):
                if i >= 2:
                    l = line.split(" ")
                    buff[0] = l[0]
                    buff[1] = l[1]
                    writing(g,buff)


if __name__ == "__main__":
    main(sys.argv[1])
