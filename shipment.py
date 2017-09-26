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

cargo = [
        [n1,c0],#n0
        [n0],#n1
        [n1],#c0
        [],#c1
        [],#c2
        [],#j0
        [],#w0
        [],#a0
        [],#a1
        ]
def calscore(path):
    path = copy.copy(path)
    car = copy.deepcopy(cargo)
    shipment = [c0,c0,c1,c2]
    score = 0
    cost = 0
    for p in range(len(path)):
        #unload
        for i,s in reversed(list(enumerate(shipment))):
            if s == p:
                shipment.pop(i)
        print('at',p,shipment)
        #load
        pass
    return (score,cost)
def IDAstar(path,length):
    print(path)
    tmp = calscore(path)
    ans = (tmp[0],tmp[1],path)#score,cost,path
    if len(path) >= length:return ans
    for i in range(N):
        tmp = IDAstar(path+[i],length)
        if tmp[0]>ans[0]:
            ans = tmp
    return ans
if __name__ == '__main__':
    path = [c0,c1,c2]
    sol = IDAstar(path,3)
    print(sol)
