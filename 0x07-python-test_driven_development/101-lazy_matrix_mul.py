#!/usr/bin/python3
def lazy_matrix_mul(m_a, m_b):
    msg1 = "m_a must be a list"
    msg2 = "m_b must be a list"
    msg3 = "m_a must be a list of lists"
    msg4 = "m_a must be a list of lists"
    msg5 = "m_a can't be empty"
    msg6 = "m_b can't be empty"
    msg7 = "m_a should contain only integers or floats"
    msg8 = "m_b should contain only integers or floats"
    msg9 = "each row of m_a must be of the same size"
    msg10 = "each row of m_a must be of the same size"
    msg11 = "m_a and m_b can't be multiplied"
    if type(m_a) is not list:
        raise TypeError(msg1)
    if type(m_b) is not list:
        raise TypeError(msg2)
    elif not all(map(lambda x: True if type(x) is list else False, m_a)):
        raise TypeError(msg3)
    elif not all(map(lambda x: True if type(x) is list else False, m_b)):
        raise TypeError(msg4)
    elif not m_a:
        raise ValueError(msg5)
    elif not m_b:
        raise ValueError(msg6)
    for lta in m_a:
        if len(lta) != len(m_a[0]):
            raise TypeError(msg9)
        T = list(map(lambda x: False if type(x) != int and type(x) != float else True, lta))
        if not all(T):
            raise TypeError(msg7)
    for ltb in m_b:
        if len(ltb) != len(m_b[0]):
            raise TypeError(msg10)
        T = map(lambda x: 1 if type(x) != int and type(x) != float else 0, ltb)
        if all(T):
            raise TypeError(msg8)
    if (len(m_a[0]) != len(m_b)):
        raise ValueError(msg11)
    m_b_t = []
    for i in range(len(m_b[0])):
        m_b_t.append(list(map(lambda l: l[i], m_b)))
    new_matrix = []
    for row in m_a:
        new = []
        for col in m_b_t:
            new.append(sum(list(map(lambda i: row[i]*col[i],range(len(row))))))
        new_matrix.append(new)
    return new_matrix
