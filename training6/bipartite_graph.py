class Graph():

	def __init__(self, V):
		self.V = V
		self.graph = [[0 for column in range(V)]
					for row in range(V)]

		self.color_list = [-1 for i in range(self.V)]

	def utils(self, src):

		queue = []
		queue.append(src)
		while queue:

			u = queue.pop()
			if self.graph[u][u] == 1:
				return False

			for v in range(self.V):
				if (self.graph[u][v] == 1 and
						self.color_list[v] == -1):
					self.color_list[v] = 1 - self.color_list[u]
					queue.append(v)

				elif (self.graph[u][v] == 1 and
					self.color_list[v] == self.color_list[u]):
					return False
		return True

	def check(self):
		self.color_list = [-1 for i in range(self.V)]
		for i in range(self.V):
			if self.color_list[i] == -1:
				if not self.utils(i):
					return 0
		return 1


line = input().split()
n = int(line[0])
m = int(line[1])

g = Graph(n)

for _ in range(m):
    line = input().split()
    i = int(line[0])
    j = int(line[1])
    g.graph[i-1][j-1] = 1

print(g.check())