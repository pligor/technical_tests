import numpy as np
from scipy.sparse import coo_matrix
from os import listdir, path
import re

#https://stackoverflow.com/questions/10415028/how-can-i-recover-the-return-value-of-a-function-passed-to-multiprocessing-proce
# TODO read files with multiple threads

def parse_and_create_map(coordinates_directory, filled_symbol='x', empty_symbol='.'):
    """Parses files in the input directory into a map 
        then saves this to a file location and returns it.

    Args:
        coordinates_directory (string): Directory containing 
                the files to parse.
    
    Returns:
        The created map.
    """

    xx = []
    yy = []
    for cur_file in listdir(coordinates_directory):
        # print file
        cur_data = open(path.join(coordinates_directory, cur_file)).read()
        # print data
        tuples = re.findall('x([0-9]+)y([0-9]+)', cur_data)
        # print tuples
        xx += map(lambda vv: int(vv[0]), tuples)
        yy += map(lambda vv: int(vv[1]), tuples)

        # for line in open(path.join(coordinates_directory, file)):
        #     print line
        #     print re.findall('x([0-9]+)y([0-9]+)', line)
        #     break

    rows = np.array(yy)
    cols = np.array(xx)

    assert len(rows) == len(cols)

    ones = np.ones(len(rows))

    spmat = coo_matrix((ones, (rows, cols)))

    arr = spmat.toarray().astype(np.object)
    arr[arr > 0] = filled_symbol
    arr[arr == 0] = empty_symbol

    map_output = "\n".join(["".join(map(lambda _ : str(_), line)) for line in arr])

    return map_output


if __name__ == '__main__':
    print parse_and_create_map('CoordinateSystem')
    print
    print parse_and_create_map(
        '/home/student/pligor.george@gmail.com/msc_Artificial_Intelligence/beyond/test_files/mapcreator_test_files')
