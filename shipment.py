import copy
n0=0
n1=1
c0=2
c1=3
c2=4
j0=5
w0=6
a0=7
a1=8
N = 9#planet num

dist = [
        [0,0,564,564,564,927,0,884,884],#n0
        [0,0,564,564,564,927,0,884,884],#n1
        [564,564,0,0,0,508,927,400,400],#c0
        [564,564,0,0,0,508,927,400,400],#c1
        [564,564,0,0,0,508,927,400,400],#c2
        [927,927,508,508,508,0,607,874,874],#j0
        [0,0,927,927,927,607,0,1526,1526],#w0
        [884,84,400,400,400,874,1526,0,0],#a0
        [884,84,400,400,400,874,1526,0,0],#a1
        ]

capacity = 4
shipments = [
        [n1,n1,c0,c0,c0,c1,c1,c1,c1,c1,c2,c2,c2,c2,a1,a1,a0],#n0
        [n0,n0,n0,c0,c0,c0,c1,j0,j0,c2,w0,w0,w0,w0,a1,a0,a0,a0],#n1
        [c1,c1,c1,c2,c2,a1,a1,j0,n0,w0],#c0
        [c2,c0,c0,c0,a1,j0,n1,w0,w0,w0],#c1
        [c1,c0,a0,a0,a1,n1,n1,n1,n1,n1],#c2
        [c2,c2,c2,c0,c1,c1,c1,n1,n1,n1,n0,n0,n0,a1],#j0
        [n1,n1,j0,n0,n0,c0,c0,c0,c2,c2,c2,c1,c1,c1,a0,a0,a0,a0,a0,a1,a1,a1],#w0
        [c1,c1,c1,c1,c2,c2,c2,c0,c0,c0,j0,j0,n0,n0,w0],#a0
        [a0,a0,c1,c1,c0,c0,c2,n1,n1,n0,j0,j0,j0,w0,w0],#a1
        ]
total_shipments = sum([len(i) for i in shipments])
def cmp_score(sc1,sc2):
    if(sc1[0]>sc2[0]):return 1
    if(sc1[0]<sc2[0]):return -1
    if(sc1[1]<sc2[1]):return 1
    if(sc1[1]>sc2[1]):return -1
    if(len(sc1[2])<len(sc2[2])):return 1
    if(len(sc1[2])>len(sc2[2])):return -1
    return 0
def calScore(path):
    sm = copy.deepcopy(shipments)
    cargo = []
    score = 0
    cost = 0
    #print('cargo ',cargo)
    for p in range(len(path)):
        if p!=0:cost+=dist[path[p-1]][path[p]]
        cur_p = path[p]
        #unload
        for i,s in reversed(list(enumerate(cargo))):
            if s == cur_p:
                cargo.pop(i)
                score +=1
        #load
        for i in range(p+1,len(path)):
            load_p = path[i]
            if len(cargo) >= capacity: break
            for ind,s in reversed(list(enumerate(sm[cur_p]))):
                if s == load_p:
                    sm[cur_p].pop(ind)
                    cargo.append(load_p)
                    if len(cargo) >= capacity: break
        #print('At ',cur_p,cargo)
    return (score,cost,path)
def IDAstar(path, length, pre_sc, cut):
    #print(path)
    sc = calScore(path)#score,cost,path
    #cut if not improve or too far
    if cmp_score(sc,pre_sc)<0:
        cut += 1
        if cut>2:
            return sc
    else:
        cut = 0
    if sc[0] >= total_shipments: return sc
    if len(path) >= length: return sc
    #iter
    for i in range(N):
        if len(path)>0 and i == path[-1]:continue
        tmp = IDAstar(path+[i], length, sc, cut)
        if cmp_score(tmp,sc)>0:sc = tmp
    return sc
if __name__ == '__main__':
    path = []
    print(total_shipments)
    for i in range(1,70):
        sol = IDAstar(path, i, (0,0,path), 0)
        if(len(sol[2]))>4:
            path = sol[2][:-4]
        if sol[0] >= total_shipments:break
        print('step: %2d done:%3d/%3d'%(i,sol[0],total_shipments))
        print(sol[2])
