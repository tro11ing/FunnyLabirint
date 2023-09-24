from collections import deque
from constants import *

class PathFinding:
	def __init__(self, game):
		self.game = game
		self.map = game.map.str_map
		self.ways = [0,1], [1,0], [0,-1], [-1,0]
		self.graph = {}
		self.build_graph()

	def get_path(self,start,goal):
		self.visited = self.bfs(start,goal,self.graph)
		path = [goal]
		step = self.visited.get(goal,start)

		while step and step != start:
			path.append(step)
			step = self.visited[step]
		return path[-1]

	def bfs(self,start,goal,graph):
		queue =  deque([start])
		visited = {start: None}

		while queue:
			cur_node = queue.popleft()
			if cur_node == goal:
				break
			next_nodes = graph[cur_node]

			for next_node in next_nodes:
				if next_node not in visited:
					queue.append(next_node)
					visited[next_node] = cur_node
		return visited

	def get_next_nodes(self,x,y):
		nodes = []
		for dx, dy in self.ways:
			if ((x + dx)*CELL_SIZE, (y + dy)*CELL_SIZE) not in self.game.map.set_walls:
				nodes.append((x + dx, y + dy))
		return nodes

	def build_graph(self):
		for y, line in enumerate(self.map):
			for x, col in enumerate(line):
				if col != "1":
					self.graph[(x,y)] = self.graph.get((x,y), []) + self.get_next_nodes(x,y)