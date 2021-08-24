
def str_to_int(str_obj=''):
    negative_factor = 1
    if not str_obj and str_obj is not None:
        return 0
    elif str_obj is None:
        raise TypeError
    if str_obj[0] == '-':
        negative_factor, str_obj = -1, str_obj.replace('-', '', 1)
    if str_obj.isnumeric():
        dict_int = {j: i for i, j in enumerate('0123456789')}
        len_string, convert_num = len(str_obj), 0
        for degree, num in enumerate(str_obj, 1):
            convert_num += dict_int[num] * 10 ** (len_string - degree)
        return convert_num * negative_factor
    else:
        raise ValueError
