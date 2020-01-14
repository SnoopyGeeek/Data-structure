import collections
import copy
def unionfind(syn):
        ans=collections.defaultdict(list)
        tran={}
        for pair in syn:
            tran[pair[0]]=pair[0]
            tran[pair[1]]=pair[1]
        for pair in syn:
            tran[pair[0]]=pair[1]
        for key in tran:
            while(1):
                father=tran[key]
                if father!=tran[father]:
                    tran[key]=tran[father]
                else:
                    break
        for key,value in tran.items():
            ans[value].append(key)
        return list(ans.values())

class UnionFind_graph:    #union find on a two diementional graph, can solve leetcode No.803
    def __init__(self,R,C):          #R and C represent the the quantity of rows and collumns, then R*C=totl number of nodes
        self.pair=[i for i in range(R*C+1)]
        self.sz=[1]*(R*C+1)
    def find(self,x):  #find one node's belonging
        while 1:
            father=self.pair[x]
            if father!=self.pair[father]:
                self.pair[x]=self.pair[father]
            else:
                break
        return self.pair[x]

    def union(self,x,y):         #link two nodes on the graph
        xr,yr=self.find(x),self.find(y)
        if xr==yr:return
        if xr<yr:
            xr,yr=yr,xr
        self.pair[yr]=xr
        self.sz[xr]+=self.sz[yr]   

    def size(self,x):
        return self.sz[self.find(x)]
    def top(self):
        return self.sz[-1]-1



if __name__=="__main__":
    print(unionfind([["happy","joy"],["sad","sorrow"],["joy","cheerful"]]))
    #a=[[1,0,1],[1,1,1]]
    #b=[[0,0],[0,2],[1,1]]