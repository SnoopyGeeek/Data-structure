# 1. topological order: means that when we put all nodes in an array order, all links' directions are from left to right.
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
#               return error (graph has at least one cycle)
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


# 2. DAG detection: 
#     two methods  1) Tarjan's strongly connected components  
#                  2) Kahn's algorithm

#   1) Tarjin: a little bit difficult.
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
#    1) Tarjan--------------------------------
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

#    2) Kahn detection----------------------------
def KahnDetect(nodesum,edgelist):
    graph=collections.defaultdict(list)
    ind=collections.defaultdict(int)
    avai=set()
    for item in edgelist:
        graph[item[0]].append(item[1])
        ind[item[1]]+=1
    for i in range(nodesum):
        if ind[i]==0:
            avai.add(i)
    while(avai):
        node=avai.pop()
        for i in graph[node]:             #delete the edges associated with node
            ind[i]-=1
            if ind[i]==0:                 #if neighbor of the node has no incoming edges, add it to the set avai
                avai.add(i)
   
    for key in ind:                 #   check whether there are edges left in the remaining graph
        if ind[key]>0:
            return False
    return True
        

#*******************************************************************************************************************************
#2. Topological sort
#    1) Kahn-----------------------------    
def KahnSort(nodesum,edgelist):
    ans=[]
    graph=collections.defaultdict(list)                 #graph edges storing dictionary
    ind=collections.defaultdict(int)                    #in_degree storing dictionary
    avai=set()                                          # a set to store nodes with 0 in-coming degree
    for item in edgelist:
        if item[0]==item[1]:
            return ans
        graph[item[0]].append(item[1])
        ind[item[1]]+=1
    for i in range(nodesum):                            #Add nodes with 0 in-coming degrees to the avai
        if ind[i]==0:
            avai.add(i)
    
    while(avai):                                       
        node=avai.pop()                                 # pop one node from avai
        ans.append(node)
        for i in graph[node]:                           # substract one in-coming degree from the node's neighbors
            ind[i]-=1
            if ind[i]==0:                               # if the neighbor has 0 in-coming degree, add it to the set
                avai.add(i)
    for key in ind:
        if ind[key]>0:
            return []
    return ans


#    2) DFS solution----------------------
#       Also we need to detect existence of cycles. Here we use a temp to record the temporary visited route, if dfs revisit the temp route, it means a cycle.
def DFSSort(nodesum,edgelist):
    ans=[]
    visited=[False]*nodesum
    temp=[False]*nodesum                     #temp list to record the temporary visited route
    flag=0                                  # detect whether there is a cycle
    graph=collections.defaultdict(list)
    for item in edgelist:
        if item[0]==item[1]:
            return ans
        graph[item[0]].append(item[1])

    def visit(node):
        nonlocal visited,graph,ans,temp,flag
        visted[node]=True
        temp[node]=True                           # temporariely visted mark
        for i in graph[node]:
            if temp[i]:
                flag=1
                return 
            if not visited[i]:
                visit(i)
        temp[node]=False                         #delete the temporary visited mark on the callback
        ans.append(node)                         #Add the current node to the result on the callback, denoting we have finished visiting all his neighbors.

    for i in range(nodesum):                     
        if not visited[i] and not flag:         # for all unvisited nodes and no cycles, visit them.
            visit(i)
        if flag:                                # if found a cycle, return an empty list.
            return []
    return ans