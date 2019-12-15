# Find bridges on a undirected graph.
# For any edge:u-v, (u having discovery time less than v), 
# if the earliest discovered vertex that can be visited from any vertex in the subtree rooted at vertex "v" has discovery time strictly greater than that of "u", 
# then u-v is a Bridge otherwise not


#Find articulation points on graphs:
# build a DFS tree and two conditions for an articulation point:1) root node with more than 1 children 2) not root node but one of his children does not have back edge above the node
# keynode to preserve information: 1)low to store tallest back edge of nodes rooted on the current subtree 2)disc to store discover the discover time of the node  3)parent to store the parrent node the current node in the DFS tree
# remember to update low array in the callback of neighbors low[u]=min(low[u],low[v]) v is a child of u 
# reference: https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/    https://www.hackerearth.com/zh/practice/algorithms/graphs/articulation-points-and-bridges/tutorial/

import collections
import math
class Graph:
    def __init__(self,edgelist=None):
        self.graph=collections.defaultdict(list)
        self.Time=0
        if edgelist:
            self.edgelist=edgelist
            for edge in edgelist:
                self.graph[edge[0]].append(edge[1])
                self.graph[edge[1]].append(edge[0])
            self.V=len(self.graph)
        else:
            self.edgelist=[]
            self.V=0

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.V=len(self.graph)
        self.edgelist.append([u,v])
    
    def FindArticulation(self):               #Find all articulation point
        self.time=0
        AP=[]
        visited=[False]*self.V
        disc=[math.inf]*self.V
        low=[math.inf]*self.V
        parent=[-1]*self.V
        for index in range(self.V):
            if visited[index]==False:
                self.DFSAP(index,visited,AP,parent,low,disc)
        return list(set(AP))

    def FindBridges(self):
        self.Time=0
        bridges=[]
        visited=[False]*self.V
        disc=[math.inf]*self.V
        low=[math.inf]*self.V
        parent=[-1]*self.V
        for index in range(self.V):
            if visited[index]==False:
                self.DFSBr(index,visited,parent,bridges,low,disc)
        return bridges
    
    def DFSBr(self,index,visited,parent,bridges,low,disc):
        visited[index]=True
        disc[index]=self.Time
        low[index]=self.Time
        self.Time+=1

        for node in self.graph[index]:
            if visited[node]==False:
                parent[node]=index
                self.DFSBr(node,visited,parent,bridges,low,disc)
                low[index]=min(low[index],low[node])
                if low[node]>disc[index]:                                       #important, if low[node]>disc[index] means the back edge link of current subtree is strctly lower than the upper node
                    bridges.append([index,node])
            if parent[index]!=node:
                low[index]=min(low[index],disc[node])
                


    def DFSAP(self,index,visited,AP,parent,low,disc):
        visited[index]=True
        disc[index]=self.Time
        low[index]=self.Time
        self.Time+=1
        children=0
        for node in self.graph[index]:
            if visited[node]==False:
                parent[node]=index
                children+=1
                self.DFSAP(node,visited,AP,parent,low,disc)
                low[index]=min(low[index],low[node])
                if parent[index]==-1 and children>1:                        #AP condition 1: if node is the root and has more than 1 children
                    AP.append(index)
                elif parent[index]!=-1 and low[node]>=disc[index]:          #AP condition 2: if node is not the root and one child of the node dos not have back edge up of the node
                    AP.append(index)
            elif parent[index]!=node:                                     #important, update the lowest back edge, update low[index]=min(low[index],disc[node]) if visited 
                low[index]=min(low[index],disc[node])
if __name__=="__main__":
    graphAP1=Graph([[0,1],[0,5],[1,2],[1,3],[2,3],[2,4],[3,4]])
    graphAP2=Graph([[0,1],[1,2],[0,2],[0,3],[3,4]])
    graphAP3=Graph([[0,1],[1,2],[2,3]])
    graphAP4=Graph([[0,1],[0,2],[1,2],[1,6],[1,4],[1,3],[3,5],[4,5]])
    print(graphAP2.graph)
    print(graphAP4.FindBridges())