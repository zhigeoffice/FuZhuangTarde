# -*- encoding: utf-8 -*-
"""
@File    : get_system_info.py
@Time    : 2021/12/26 17:11
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
import platform

def getSystemInfo():
    system=platform.system()
    plat_version=platform.platform()
    return 0 if system == 'Windows' else 1

if __name__ == '__main__':
    info = getSystemInfo()
    print(info)