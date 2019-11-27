# topological order means that when we put all nodes in an array order, all links' directions are from left to right.
# Two methods: 1) Kahn algorithm
#              2) DFS algorithm

#  Kahn:    L← Empty list that will contain the sorted elements
#           S ← Set of all nodes with no incoming edges
#           while S is non-empty do
#               remove a node n from S
#               insert n into L
#               for each node m with an edge e from n to m do
#                   remove edge e from the graph
#                   if m has no other incoming edges then
#                       insert m into S
#           if graph has edges then
#               return error (graph has at least onecycle)
#           else
#               return L (a topologically sortedorder)



# DFS:      L ← Empty list that will contain the sorted nodes
#           S ← Set of all nodes with no outgoing edges
#           for each node n in S do
#               visit(n)
#           function visit(node n)
#               if n has not been visited yet then
#                   mark n as visited
#               for each node m with an edge from m to n do
#                   visit(m)
#               add n to L


# DAG detection: Tarjan's strongly connected components  

#   input:      unvisited=-1 
#               n=number of nodes in graph
#               g=adjacency list with directed edges

#               id=0            used to give each node an id
#               scc=0           used to count number of SCCs found

#  auxilary:    ids=[0,0,0,...,0]  length of n to see whether node is visited or non-visited and node id
#               lows=[0,0,0,...,0]  length of n 
#               onStack=[False, False, False,...,False]
#               stack=[]        empty stack structure

#               def findSccs():
#                   for i in range(n):  ids[i]=unvisited
#                   for i in range(n):
#                       if ids[i]==unvisited:
#                           dfs(i)
#                   return low

#               def dfs(i):
#                   stack.append(i)
#                   onstack[i]=True
#                   ids[i]=low[i]=id
#                   id+=1

#                   for nei in g[at]:
#                       if ids[nei]==unvisited:
#                           dfs(nei)
#                       if onStack[nei]:
#                           low[i]=min(low[i],low[nei])

#                       if ids[i]==low[i]:
#                           while stack:
#                               node=stack.pop()
#                               onStack[node]=False
#                               low[node]=ids[at]
#                               if node==i:
#                                   break
#Example: lc. 207 Course Schedule (Detecting DAG) and lc. 210 Course Schedule II (Find the topological order).


#*******************************************************************************************************************************
#1. Detecting DAG
#    1) Tarjan
import collections
def findSCCs(nodenum,edgelist):
    graph=collections.defaultdict(list)
    for item in edgelist:
        graph[item[0]].append(item[1])
    low=[0]*nodenum                             #component signature pointers
    ids=[-1]*nodenum                            #id mapping of the node, -1 mean unvisited
    onStack=[False]*nodenum                     #whether a node is in the stack
    stack=[]
    id=0

    def dfs(nodeindex):
        nonlocal stack,ids,low,id,graph,onStack
        stack.append(nodeindex)
        onStack[nodeindex]=True
        ids[nodeindex],low[nodeindex]=id,id
        id+=1

        for nei in graph[nodeindex]:
            if ids[nei]==-1:
                dfs(nei)
            if onStack[nei]:                 # if visited it(nei) before and it(nei) is the neighbor of nodeindex, it forms a circle, the circle belongs to smaller low number 
                low[nodeindex]=min(low[nodeindex],low[nei])    # most important
        if ids[nodeindex]==low[nodeindex]:       # if we are at the head of a strongly connected component, pop all related items inside the component
            while(stack):
                node=stack.pop()
                onStack[node]=False
                low[node]=low[nodeindex]
                if node==nodeindex:
                    break

    for index in range(nodenum):
        if ids[index]==-1:
            dfs(index)
    return low

