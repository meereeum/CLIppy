import math


def pprint_header_with_lines(str_header, l_lines, UNDERLINE_CHAR='_'):
    """Pretty-print `str_header` + list of `l_lines`

    ____header____
    line 1
    line 2.........
    line 3...
    """
    round_up_to_even = lambda x: math.ceil(x / 2) * 2 # closest even int (>=)

    header_space = len(str_header)
    underline_space = round_up_to_even(len(max(l_lines, key=len)) -
                                       header_space) + header_space
    str_header_final = '{:{}^{}}'.format(str_header, UNDERLINE_CHAR, underline_space)

    print(str_header_final); print('\n'.join(l_lines))
