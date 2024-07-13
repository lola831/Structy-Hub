Watch the Approach video first!

Write a function sumNumbersRecursive that takes in an array of numbers and returns the sum of all the numbers in the array. All elements will be integers. Solve this recursively.

test_00

sum_numbers_recursive([5, 2, 9, 10]); # -> 26

test_01

sum_numbers_recursive([1, -1, 1, -1, 1, -1, 1]); # -> 1

test_02

sum_numbers_recursive([]); # -> 0

test_03

sum_numbers_recursive([1000, 0, 0, 0, 0, 0, 1]); # -> 1001

test_04

sum_numbers_recursive([700, 70, 7]); # -> 777

test_05

sum_numbers_recursive([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]); # -> -55

test_06

sum_numbers_recursive([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]); # -> 0

test_07

sum_numbers_recursive([123456789, 12345678, 1234567, 123456, 12345, 1234, 123, 12, 1, 0]); # -> 137174205