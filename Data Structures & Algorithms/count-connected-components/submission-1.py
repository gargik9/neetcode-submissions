class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(n))


        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            px,py = find(x), find(y)
            if px==py:
                return False

            parent[px] = py
            return True

        count = n

        for x,y in edges:
            if union(x,y):
                count-=1

        return count            