class Graph:
	def __init__(self, V):
		self.V = V
		self.adj = [[] for i in range(V)]

	def dfs(self, temp, v, visited):
		visited[v] = True

		temp.append(v)

		for i in self.adj[v]:
			if visited[i] == False:
				temp = self.dfs(temp, i, visited)
		return temp

	def addEdge(self, v, w):
		self.adj[v].append(w)
		self.adj[w].append(v)

	def find(self):
		visited = []
		cc = []
		for i in range(self.V):
			visited.append(False)
		for v in range(self.V):
			if visited[v] == False:
				temp = []
				cc.append(self.dfs(temp, v, visited))
		return cc


line = input().split()
n = int(line[0])
m = int(line[1])

g = Graph(n)

for _ in range(m):
    line = input().split()
    i = int(line[0])
    j = int(line[1])
    g.addEdge(i-1, j-1)

cc = g.find()
print(len(cc))

