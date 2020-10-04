adj_graph=[
    [0,4,2,0,0,0],
    [4,0,1,5,0,0],
    [2,1,0,8,10,0],
    [0,5,8,0,2,6],
    [0,0,10,2,0,5],
    [0,0,0,6,5,0]
    ]
vertices=len(adj_graph[0])
for a in range(vertices):
    for b in range(vertices):
        if a!=b and adj_graph[a][b]==0:
            adj_graph[a][b]=float('inf')

for start in range(vertices):
    print("Starting with Node %c\n\n\n"%(chr(start+97)))
    node1=start
    minElem=start
    shortest=[float('inf') for i in range(vertices)]
    shortest[node1]=0
    visited=[False for i in range(vertices)]
    notVisited=[c for c in range(vertices)]
    prev_node=[0 for i in range(vertices)]
    for u in range(vertices):
        for v in range(vertices):
            if adj_graph[node1][v]+shortest[node1]<shortest[v]:
                shortest[v]=adj_graph[node1][v]+shortest[node1]
                prev_node[v]=node1
        visited[node1]=True
        notVisited.remove(node1)
        if len(notVisited)==0:
            break
        minElem=notVisited[0]
        for i in notVisited:
            if i==start:
                continue
            if shortest[minElem]>shortest[i]:
                minElem=i
        node1=minElem
    print("Node\t\tDistance\tPrevious Node")
    for i in range(vertices):
        if i!=start:
            print("  %c\t\t%d\t\t%c"%(chr(i+97),shortest[i], chr(prev_node[i]+97)))
        else:
            print("=>%c\t\t%d\t\t-"%(chr(i+97),shortest[i]))