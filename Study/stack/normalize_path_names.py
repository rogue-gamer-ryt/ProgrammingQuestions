"""
Write a program which takes a pathname, and retums the shortest equivalent pathname. Assume
individual directories and files have names that use only alphanumeric characters. Subdirectory
names may be combined using forward slashes (/), the current directory (.) and parent directory
(. .).
"""

# Time complexity - O(n)
def shortest_equivalent_path(path):
    ipath_names = []
    if path[0] == "/":
      path_names.append("")

    for token in (token for token in path.split('/') if token not in ['.', '']):
        if token == "..":
            if not path_names or path_names[-1] == "..":
                path_names.append(token)
            elif path_names[-1] != "":
                path_names.pop()
        else:
            path_names.append(token)
    if len(path_names) == 1 and path_names[0] == '':
        return "/"

    return '/'.join(path_names)
