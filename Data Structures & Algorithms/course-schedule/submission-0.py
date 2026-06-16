class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses  #declaring an array where indegree[x] = num of prereq courses
        adj = [[] for i in range(numCourses)]  #graph to store course and prereq
        for src, dst in prerequisites:   #adding values to adj
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()                
        for n in range(numCourses):   #fill queue with courses you can take (0 prereq)
            if indegree[n] == 0:
                q.append(n)
        
        finish = 0         
        while q:                 #while q is not empty
            node = q.popleft()   
            finish += 1         #mark course as taken
            for nei in adj[node]:      #check next course adjacent to node
                indegree[nei] -= 1      #reduce indegree by 1
                if indegree[nei] == 0:     #if iindegree 0, just append to queue
                    q.append(nei)
                
        return finish == numCourses      #return true if all courses taken