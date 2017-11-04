from hashlib import md5
import numpy as np
# TODO with multiple threads
from run_in_parallel import runInParallel
from multiprocessing import Process, Value, Array


def searcher(generator, number_of_zeros, salt, pos_remain, debug=False):
    # cur_hex = None
    # cur_str = None
    cur_letter = None

    tuples = []

    for cur_seq in generator(salt):
        for cur_str in cur_seq:
            cur_hex = md5(cur_str).hexdigest()

            for cur_letter in cur_hex[:number_of_zeros]:
                if cur_letter != '0':
                    break

                    # if cur_hex[:number_of_zeros] == '0' * number_of_zeros:
                    # print
                    # print "found it"
                    # print cur_letter
                    # print cur_hex

            if cur_letter == '0':
                try:
                    # print cur_hex[number_of_zeros]
                    postfix = int(cur_str[len(salt):])
                    position_of_character = int(cur_hex[number_of_zeros])
                    character_to_use = cur_hex[postfix % 32]

                    tuples.append((position_of_character, character_to_use, postfix))

                    pos_remain[position_of_character] = -1
                    # print "removing position: {}".format(position_of_character)
                    print "values {}".format(pos_remain[:])

                    if sum(pos_remain[:]) == -10:  # only when all are -1 you will get a sum of -10
                        if debug:
                            print "ALL FOUND"
                        return tuples

                except ValueError:  # ignore because not useful if we have 'g' for example
                    # print "pefto edw"
                    continue


def get_indices_generator(filter_tpl=None):
    def _gen(prefix, step=1e6):
        """
        :param prefix:
        :param step:
        :param filter_tpl: the first element is how many processes in total and 2nd elem is the process it belongs
        :return:
        """

        step = int(step)
        nn = 0
        while True:
            postfix_list = range(step * nn, step * (nn + 1))

            if filter_tpl is not None:
                postfix_list = filter(lambda xx: xx % filter_tpl[0] == filter_tpl[1], postfix_list)

            yield map(lambda xx: prefix + str(xx), postfix_list)
            nn += 1

    return _gen


def find_zero_collision_from_salt(salt, number_of_zeros, target_len=10, debug=False, jobs=1, TUPLES_STR_SIZE=4096):
    """Finds the hash collisions string returns it.

    Args:
        salt (string): The salt to iterate and hash.
        number_of_zeros (int): The number of zeros to be searching for at the start of the hash.
    
    Returns:
        The collisions string the function has built.
    """

    # strs = map(lambda xx: salt + str(xx), range(int(1e7)))

    # print strs
    # zeros = '0' * number_of_zeros
    # print zeros

    invalid_hash_char = ''
    collision_output = [invalid_hash_char] * target_len
    # print collision_output
    # return
    # print

    # cur_tuples_str

    pos_remain = Array('i', range(target_len))
    tuples_str = Array('c',
                       ' ' * TUPLES_STR_SIZE)  # should be enough because this case is covered: "(10,a,1000000000);" * 100

    def tuples_from_str():
        tpl_str = tuples_str[:].strip()
        return [tuple(cur_tpl.split(',')) for cur_tpl in tpl_str.split(';')]

    def tuples_to_str(tuples_input):
        return ";".join(
            [','.join(map(lambda _: str(_), cur_tpl)) for cur_tpl in tuples_input]
        )  # 8,4,5017308;0,0,8605828;6,8,8609554;9,d,9495334;6,0,12763908;2,0,15819744
        # print cur_tuples_str

    if jobs == 1:
        # pos, char, postfix
        tuples = searcher(generator=get_indices_generator(),  # lambda xx: strs,
                          number_of_zeros=number_of_zeros, salt=salt, debug=debug,
                          pos_remain=pos_remain)
    else:
        # now we need to run searcher in multiple processes and each one is going to take the postfixs that correspond to the
        # modulo that corresponds to the process. The returned tuples will be appended to the "global" tuples variable
        def function_generator(cur_job):
            def _search():
                cur_tuples = searcher(generator=get_indices_generator(filter_tpl=(jobs, cur_job)),
                                      number_of_zeros=number_of_zeros, salt=salt, debug=debug,
                                      pos_remain=pos_remain)
                existing_tuples = tuples_from_str()  # this could be empty array

                all_tuples = cur_tuples + existing_tuples

                all_tuples_str = tuples_to_str(all_tuples)

                remain_size = (TUPLES_STR_SIZE - len(all_tuples_str))
                assert remain_size >= 0, "increase size if this crashes"

                full_str = all_tuples_str + (' ' * remain_size)

                tuples_str[:] = full_str

            return _search

        funcs = [function_generator(cur_job=job_num) for job_num in range(jobs)]

        runInParallel(*funcs)

        tuples = tuples_from_str()

    tuples_norm = [(int(tpl[0]), tpl[1], long(tpl[2])) for tpl in tuples if len(tpl) == 3]

    # keep the minimum postfix for each position
    firsts_only = [tpl for tpl in tuples_norm if
                   tpl[2] == np.min([cur_tuple[2] for cur_tuple in tuples_norm if cur_tuple[0] == tpl[0]])]

    for pos, char, postfix in firsts_only:
        collision_output[pos] = char

    collision_output = "".join(collision_output)
    assert len(collision_output) == target_len, "length is actually: {}".format(len(collision_output))

    return collision_output


if __name__ == '__main__':
    # print arr[:]
    # print len(arr[:].strip())
    # exit()

    # TODO make multiprocessing to work more intelligently, now the processes do not know that they should abandon immediately if they process is over
    out = find_zero_collision_from_salt('abc', 5, debug=True, jobs=8)
    print out
    assert out == '0a7c3b804d'

    # out = find_zero_collision_from_salt('machine-learning', 4)
    # assert out == 'f320e001d1'

    # out = find_zero_collision_from_salt('artificial-intelligence', 5)
    # assert out == '610d370320'

    # out = find_zero_collision_from_salt('code-quality', 3, debug=True)
    # assert out == '09e97089ae'

    # tuples = [(1, 'a', 3231929), (8, '4', 5017308), (4, '3', 5357525), (7, '0', 5708769), (3, 'c', 8036669),
    #           (0, '0', 8605828), (6, '8', 8609554), (7, '1', 8760605), (9, 'd', 9495334), (6, '0', 12763908),
    #           (5, 'b', 13666005), (2, '7', 13753421)]
    # print len(tuples)
    # aa =
    # print aa
    # print len(aa)

    print "ALL CORRECT"
