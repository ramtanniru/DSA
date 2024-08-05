from collections import defaultdict,deque

class Solution:
    def bottomView(self, root):
        d = defaultdict(tuple)
        queue = deque()
        queue.append((root,0))
        leftMost = 0
        while queue:
            temp,idx = queue.popleft()
            d[idx] = temp
            leftMost = min(idx,leftMost)
            if temp.left:
                queue.append((temp.left,idx-1))
            if temp.right:
                queue.append((temp.right,idx+1))
        res = []
        i = leftMost
        while i in d:
            res.append(d[i].data)
            i += 1
        return res 