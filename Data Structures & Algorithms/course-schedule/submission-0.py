class Solution:
    # dfs + memo, if cycle detected return false 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        curToPre = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            curToPre[c].append(p)

        visited = set()

        def dfs(course):
            # base cases 
            if course in visited:
                return False 
            if not curToPre[course]:
                return True 
            
            visited.add(course)

            for pre in curToPre[course]:
                # if false can just return, meaning cycle detetced  
                if dfs(pre) == False:
                    return False

            visited.remove(course) 
            # memoize the results because no cycle detected so net time can hit base case immediately if revisit this possible node
            curToPre[course] = []
            # return true because no cycle detected 
            return True 
                
        # call dfs on all elements since graph might be disconnected 
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True 
