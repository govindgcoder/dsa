from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display(self):
        for node, neighbours in self.adj_list.items():
            print(node, ":", neighbours)

    def bfs(self, start):
        self.visited = set()
        queue = deque()
        queue.append(start)
        self.visited.add(start)
        while queue:
            curr = queue.popleft()
            print(curr)
            for i in self.adj_list[curr]:
                if i not in self.visited:
                    self.visited.add(i)
                    queue.append(i)

    def dfs(self, start):
        self.visited = set()

        def helper(start):
            self.visited.add(start)
            print(start)
            for i in self.adj_list[start]:
                if i not in self.visited:
                    helper(i)

        helper(start)


test = Graph()
test.add_edge(1, 2)
test.add_edge(2, 3)
test.add_edge(2, 4)
test.add_edge(3, 4)
test.display()

test.bfs(2)
test.dfs(2)
