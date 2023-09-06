#!/usr/bin/python3
""" Module composed of a function that multiplies 2 matrices"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Return:
        result of multiplication
    """
    return (np.matmul(m_a, m_b))
