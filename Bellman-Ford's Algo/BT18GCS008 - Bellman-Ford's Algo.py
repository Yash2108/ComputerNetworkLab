adj_graph=[
    [0,5,-3,0,0],
    [0,0,0,0,-4],
    [0,0,0,3,0],
    [0,2,0,0,0],
    [0,0,0,1,0],
    ]
# adj_graph = [
#          [0, 10, 0, 0, 0, 8],
#          [0, 0, 0, 2, 0, 0],
#          [1, 0, 0, 0, 0, 0],
#          [0, 0, -2, 0, 0, 0],
#          [0, -4, 0, -1, 0, 0],
#          [0, 0, 0, 0, 1, 0]
#          ]
vertices=len(adj_graph[0])
edges=[]
for i in range(vertices):
    source=i
    print("\nStarting with Node %c"%(chr(source+97)))
    weights=[float('inf')]*vertices
    prev_nodes=[float('inf')]*vertices
    weights[source]=0
    relaxed=False
    negatives=False
    for a in range(vertices):
        for b in range(vertices):
            if a!=b and adj_graph[a][b]==0:
                adj_graph[a][b]=float('inf')
    for i in range(vertices):
        for j in range(vertices):
            if adj_graph[i][j]!=float('inf') and i!=j:
                edges.append([i,j])
    # print(edges)
    for x in range(vertices-1):
        for i, j in edges:
            if adj_graph[i][j]+weights[i]<weights[j]:
                weights[j]=adj_graph[i][j]+weights[i]
                prev_nodes[j]=i
                relaxed=True
        if relaxed==False:
            print('No relaxation in loop %d so stopping'%x)
            break
    
    for x in range(vertices-1):
        for i, j in edges:
            if adj_graph[i][j]+weights[i]<weights[j]:
                negatives=True
    if negatives:
        print("There is/are negative cycle/s in the graph")
    print("Node\t\tDistance\tPrevious Node")
    for i in range(vertices):
        if i!=source:
            if weights[i]>=0 and weights[i]<10:
                print("  %c\t\t %d\t\t%c"%(chr(i+97),weights[i], chr(prev_nodes[i]+97)))
            elif prev_nodes[i]==float('inf'):
                print("  %c\t\t %.0f\t\tN/A"%(chr(i+97),weights[i]))
            else:
                print("  %c\t\t%d\t\t%c"%(chr(i+97),weights[i], chr(prev_nodes[i]+97)))
        else:
            print("=>%c\t\t %.0f\t\tN/A"%(chr(i+97),weights[i]))
