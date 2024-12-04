"""
71. Simplify Path
Given a string path, which is an absolute path (starting with a slash '/') to a file 
or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double 
period '..' refers to the directory up a level, and any multiple consecutive slashes 
(i.e. '//') are treated as a single slash '/'. For this problem, any other format of 
periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target 
file or directory (i.e., no period '.' or double period '..' needs to be dealt with).
Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Constraints:
1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
"""
# solution:
# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         while True:
#             if path[-1] == "/" and len(path) > 1:
#                 path = path[:-1]
#             else:
#                 break
#         delete_list = []
#         if len(path) > 1:
#             for index, pa in enumerate(path):
#                 if pa == "/" and path[index+1]=="/":
#                     delete_list.append(index)
#         # print(delete_list)
#         for i in delete_list[::-1]:
#             path = path[:i] + path[i+1:]
#         # print(path)
#         path_list = path.split("/")
#         # print(path_list)
#         stack = []
#         for p in path_list:
#             if p == ".." and len(stack)>1:
#                 stack.pop()
#             elif p ==".." and len(stack)==1:
#                 pass
#             elif p == ".":
#                 pass
#             else:
#                 stack.append(p)
#         # print("/".join(stack))
#         return "/".join(stack) if "/".join(stack) else "/"

# solution 1 optimized:
class Solution:
    def simplifyPath(self, path: str) -> str:

        while len(path) > 1 and path.endswith("/"):
            path = path[:-1]

        delete_list = []
        for index in range(len(path) - 1):
            if path[index] == "/" and path[index + 1] == "/":
                delete_list.append(index)

        for i in reversed(delete_list):
            path = path[:i] + path[i + 1:]

        path_list = path.split("/")
        stack = []
        for p in path_list:
            if p == "..":
                if stack:
                    stack.pop()
            elif p != "." and p:
                stack.append(p)

        simplified_path = "/" + "/".join(stack)
        return simplified_path if simplified_path else "/"

# solution 2:
# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         # Split the path by '/' and filter out empty parts
#         parts = [p for p in path.split('/') if p not in ['', '.']]
#         stack = []

#         for part in parts:
#             if part == "..":
#                 if stack:
#                     stack.pop()
#             else:
#                 stack.append(part)

#         # Join the stack with '/' and ensure it starts with '/'
#         return "/" + "/".join(stack)
