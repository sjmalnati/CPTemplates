edge_list = [] #stores edges in (source,dest,weight)
nodes = set()
def add_edge(x,y,w):
    edge_list.append((x,y,w))
    nodes.add(x)
    nodes.add(y)
def get_root(parent,i):
    if parent[i] == i:
        return(i)
    return(get_root(parent,parent[i]))
def union(parent,rank,x,y):
    p1 = get_root(parent,x)
    p2 = get_root(parent,y)
    if rank[p1] < rank[p2]:
        parent[p1] = p2
    elif rank[p1] > rank[p2]:
        parent[p2] = p1
    # if tied arbitrarily choose one
    else:
        parent[p2] = p1
        rank[p1] += 1



#MST algo
def mst(edge_list,nodes):
    edge_list.sort(key=lambda x:x[2])
    result_edges = []
    #index of parent node
    parent = []
    rank = []
    for node in nodes:
        parent.append(node)
        rank.append(0)
    i = 0
    edges = 0
    while edges < len(nodes)-1:
        x,y,w = edge_list[i]
        i+=1
        p1 = get_root(x)
        p2 = get_root(y)
        #same root means they are already connected
        if p1 != p2:
            edges += 1
            result_edges.append((x,y,w))
            union(parent,rank,p1,p2)
    return(result_edges)
add_edge(0, 1, 10)
add_edge(0, 2, 6)
add_edge(0, 3, 5)
add_edge(1, 3, 15)
add_edge(2, 3, 4)
result = mst(edge_list,nodes)
print(result)
