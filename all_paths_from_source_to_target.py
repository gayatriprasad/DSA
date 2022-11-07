class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = [] 
        n = len(graph) 
        visited = [False] * n
        
        sourceToTarget(graph, 0, visited, n, answer, [])
        
        return answer
    
    
    def sourceToTarget(graph, currentNode, visited, n, answer, currentPath ):
        
        if currentNode == n-1:
            currentPath.append(currentNode)
            answer.append(currentPath)
            currentPath.remove(len(currentPath)-1)
            return 
            
        if visited[currentNode] == True:
            return 
        
        visited[currentNode] = True