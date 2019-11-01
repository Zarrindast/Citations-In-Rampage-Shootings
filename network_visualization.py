# make edgelist for directed citations 

node1 = list()
node2 = list()
x = 0
while x < len(citations_Unique):
    if len(citations_Unique[x][1]) > 0:
        z = 0
        while z < len(citations_Unique[x][1]):
            node1.append(citations_Unique[x][0])
            node2.append(citations_Unique[x][1][z])
            z = z + 1
    x = x + 1

d = {'from': node1, 'to': node2}
df = pd.DataFrame(data=d)
df
