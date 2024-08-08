#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# minOperations(4) should return 4

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# minOperations(12) should return 7

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# minOperations(9) should return 6

n = 7
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# minOperations(7) should return 7

n = 1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# minOperations(1) should return 0
