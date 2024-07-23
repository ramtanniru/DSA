class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque([])
        queue.append((sr,sc))
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        vis = set()
        while queue:
            li = queue.copy()
            for x,y in li:
                for dx,dy in dir:
                    if 0<=x+dx<len(image) and 0<=y+dy<len(image[0]) and image[x+dx][y+dy]==image[x][y] and (x+dx,y+dy) not in vis:
                        queue.append((x+dx,y+dy))
                        vis.add((x+dx,y+dy))
                image[x][y] = color
                queue.popleft()
        return image 