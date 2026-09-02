class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by slashes
        components = path.split("/")
        stack = []

        for component in components:
            # If '..', go up one directory level by popping the stack
            if component == "..":
                if stack:
                    stack.pop()
            # Ignore empty strings and single dots
            elif component == "." or component == "":
                continue
            # Push valid directory names to the stack
            else:
                stack.append(component)

        # Join components with a leading slash
        return "/" + "/".join(stack)
