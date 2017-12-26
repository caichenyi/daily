# encoding: utf-8
# Author: Cai Chenyi
import re
import time

def exp(target_str):
    """
    """
    s1 = time.time()
    flaw_regex = re.compile('^(a+)+$')
    flaw_regex.match(target_str)
    s2 = time.time()
    print("Consuming time: %.4f" % (s2-s1))


if __name__ == '__main__':
    str_list = (
        'aaaaaaaaaaaaaaaaX',           # 2^16
        'aaaaaaaaaaaaaaaaaaX',         # 2^18
        'aaaaaaaaaaaaaaaaaaaaX',       # 2^20
        'aaaaaaaaaaaaaaaaaaaaaaX',     # 2^22
        'aaaaaaaaaaaaaaaaaaaaaaaaX',   # 2^24
        'aaaaaaaaaaaaaaaaaaaaaaaaaaX', # 2^26
        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaX', # 2^36
    )
    for evil_str in str_list:
        print('Current: %s' % evil_str)
        exp(evil_str)
        print('--'*40)
