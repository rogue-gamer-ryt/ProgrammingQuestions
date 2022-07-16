"""
Given a 2D array of black and white entries representing a maze with designated entrance and exit
points, find a path from the entrance to the exit, if one exists.
"""
WHITE, BLACK =  range(2)
Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

# Time O(|v| + |E|)
def search_maze(maze, s, e):
    # Perform DFS
    def helper(cur):
        # Chech the current coordinate is valid
        if not(
            0 <= cur.x < len(maze) 
            and 0 <= cur.y < len(maze[cur.x]) 
            and maze[cur.x][cur.y] == WHITE
            ):
            return False
        
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True
        if any(
            map(helper, (
                Coordinate(cur.x - 1, cur.y), 
                Coordinate(cur.x , cur.y - 1), 
                Coordinate(cur.x + 1, cur.y),
                Coordinate(cur.x , cur.y + 1), 
                ))
            ):
            return True
        # Cannot find a path, remove the last entry from the path
        del path[-1]
        return False
    path = []
    if not helper(s):
        return []
    return path
