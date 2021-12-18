#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author  : zhige
@contact : 303585825@qq.com
@Software: PyCharm
@project : ouran_fuzhuangxitong
@File    : ean13jiaoyan
@Time    : 2021/9/4
'''
try:
    from functools import reduce
except ImportError:
    pass

def calculate_check_digit(code):

    def sum_str(total, digit):
        return total + int(digit)
    oddsum = reduce(sum_str, code[1::2], 0)
    evensum = reduce(sum_str, code[:12:2], 0)
    total = oddsum * 3 + evensum
    return code + str((10 - (total % 10)) % 10)

def jiaoyan(s):
    return calculate_check_digit(s[0:-1]) == s