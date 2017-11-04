# LINK: https://github.com/brean/python-pathfinding
from path_finding_lib.core.diagonal_movement import DiagonalMovement
from path_finding_lib.core.grid import Grid
from path_finding_lib.finder.a_star import AStarFinder
import numpy as np


def _path_between_points(start_x, start_y, end_x, end_y, map_file_location):
    """ Given start and end coordinates and a map file, 
            outputs the shortest path from start to end points on the map.
    
    Args:
        start_x (int): The x coordinate of the start position.
        start_y (int): The y coordinate of the start position.
        end_x (int): The x coordinate of the end position.
        end_y (int): The y coordinate of the end position.
        map_file_location (int): The file location of the map file to search through.

    Returns:
        The map with the path taken.
    """

    with open(map_file_location) as fp:
        data = fp.read()
    # print data

    # print

    lol = map(lambda line: list(line), data.split('\n'))
    arr = np.array(lol)
    arr[arr == '.'] = 0
    arr[arr == 'x'] = 1
    arr = arr.astype(dtype=np.int32)
    print arr

    grid = Grid(matrix=arr.tolist())

    start = grid.node(start_x, start_y)
    end = grid.node(end_x, end_y)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    # print 'operations:', runs, 'path length:', len(path)
    # print
    map_output = grid.grid_str(path=path, start=start, end=end,
                               border=False, start_chr='S', end_chr='E', empty_chr='.', block_chr='x', path_chr='0')

    return map_output, path


def path_between_points(start_x, start_y, end_x, end_y, map_file_location):
    return _path_between_points(start_x, start_y, end_x, end_y, map_file_location)[0]


if __name__ == '__main__':
    map_file_location = 'test_files/pathfinding_test_files/pathFindingTestMap.txt'
    from os.path import isfile

    print open(map_file_location).read()
    print
    assert isfile(map_file_location)
    print path_between_points(start_x=0, start_y=2, end_x=4, end_y=2, map_file_location=map_file_location)
    print
    print "DONE"

    # print grid
