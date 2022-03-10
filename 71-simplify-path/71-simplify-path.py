class Solution:
    def simplifyPath(self, path: str) -> str:
        pathElements = path.split('/')
        stack = []
        for ele in pathElements:
            if ele == '' or ele == '.':
                continue
            elif ele == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ele)
        return '/' + '/'.join(stack)