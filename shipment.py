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

capacity = 4
shipments = [
        [n1],#n0
        [n0],#n1
        [n1,n0,c1,c2,j0,w0,a0,a1],#c0
        [],#c1
        [],#c2
        [],#j0
        [],#w0
        [],#a0
        [],#a1
        ]
total_shipments = sum([len(i) for i in shipments])
def calScore(path):
    path = copy.copy(path)
    sm = copy.deepcopy(shipments)
    cargo = []
    score = 0
    cost = 0
    #print('cargo ',cargo)
    for p in range(len(path)):
        cur_p = path[p]
        #unload
        for i,s in reversed(list(enumerate(cargo))):
            if s == cur_p:
                cargo.pop(i)
                score +=1
        #load
        for i in range(p+1,len(path)):
            tmp = path[i]
            if len(cargo) >= capacity: break
            while tmp in sm[cur_p]:
                sm[cur_p].remove(tmp)
                cargo.append(tmp)
        #print('At ',cur_p,cargo)
    return (score,cost)
def IDAstar(path,length):
    #print(path)
    tmp = calScore(path)
    ans = (tmp[0],tmp[1],path)#score,cost,path
    if ans[0] >= total_shipments: return ans
    if len(path) >= length:return ans
    for i in range(N):
        tmp = IDAstar(path+[i],length)
        if tmp[0]>ans[0]:
            ans = tmp
    return ans
if __name__ == '__main__':
    path = [c0]
    print(total_shipments)
    for i in range(10):
        sol = IDAstar(path,i)
        if sol[0] >= total_shipments:break
    print(sol)
