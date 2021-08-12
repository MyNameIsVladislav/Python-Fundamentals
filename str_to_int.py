
def str_to_int(str_o='', k=1):
    if not str_o:
        return 0
    if str_o[0] == '-':
        k, str_o = -1, str_o.replace('-', '', 1)
    if str_o.isnumeric():
        dict_int = {j: i for i, j in enumerate('0123456789')}
        len_ = len(str_o)
        int_ = 0
        for pow_, num in enumerate(str_o, 1):
            int_ += dict_int[num] * 10 ** (len_ - pow_)
        return int_ * k
    else:
        raise ValueError


print(str_to_int())
