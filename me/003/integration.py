from mapcreator import parse_and_create_map
from pathfinding import path_between_points, _path_between_points
from hashiterator import find_zero_collision_from_salt


def all_together(start_x, start_y, end_x, end_y, coordinates_directory, number_of_zeros, temp_filepath='temporary'):
    """ Takes the files in the coordinates directory and creates a map. Then 
            given start and end coordinates it outputs the shortest path from the start 
            to end points on the map. This map is then saved to a file location. 
            The function will then take the string of the path taken, 
            find the hash collisions with the number of zeros input and 
            return the hash result.
    
    Args:
        start_x (int): The x coordinate of the start position.
        start_y (int): The y coordinate of the start position.
        end_x (int): The x coordinate of the end position.
        end_y (int): The y coordinate of the end position.
        coordinates_directory (string): Directory containing the files to parse.
        number_of_zeros (int): The number of zeros to be searching for at the start of the hash.

    Returns:
        The collisions string the function has built.
    """
    the_map = parse_and_create_map(coordinates_directory)
    with open(temp_filepath, mode='w') as fp:
        fp.write(the_map)

    path = \
        _path_between_points(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y,
                             map_file_location=temp_filepath)[1]

    # path_str = "".join(['x{}y{}'.format(elem[0], elem[1]) for elem in path])
    # TODO not sure if the hash function should take the above input or the below, sorry confused from description in pdf file
    path_str = "".join(['{:02d}{:02d}'.format(elem[0], elem[1]) for elem in path])

    collision_output = find_zero_collision_from_salt(salt=path_str, number_of_zeros=number_of_zeros)

    import os
    os.remove(temp_filepath)

    return collision_output


if __name__ == '__main__':
    print all_together(start_x=7, start_y=1, end_x=17, end_y=27, coordinates_directory='CoordinateSystem',
                       number_of_zeros=2)
