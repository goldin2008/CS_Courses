#!/usr/bin/python
# -*- coding: utf-8 -*-
# palindrome.py

from sys import argv
import numpy as np
import math


# CSCE 310
# yuleinku@gmail.com
#
# This python script parses a file given as
# a command line argument that represents an
# undirected graph as per the formatting specified
# in assignment 1.  The reprsentation is an
# n x n 0-1 integer adjacency matrix
#
# Improvements Welcome

def readFile(file_name):
    i = -1;
    for line in open(file_name,'r').readlines():
        line = line.strip()
        if(i==-1):
            string = line
    n = len(string)

    return n, string

'''
Longest Palindromic Subsequence
'''
def lps(string):
    n = len(string)
    # Create a table to store results of subproblems
    t = np.zeros( (n,n) )
    # print 'test = ', t
    R = []
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        t[i][i] = 1

	# Build the table. Note that the lower diagonal values of table are
	# useless and not filled in the process.
	# cl is length of substring
    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            if string[i] == string[j] and L == 2:
                t[i][j] = 2
            elif string[i] == string[j]:
                t[i][j] = t[i+1][j-1] + 2
            else:
                # t[i][j] = max( t[i][j-1], t[i+1][j] )
                if t[i][j-1] < t[i+1][j]:
                    t[i][j] = t[i+1][j] # move ith element to right, do not include ith element
                else:
                    t[i][j] = t[i][j-1] # move jth element to left, do not include jth element

    i = n-1
    j = n-1
    while i >=0 and j >=0:
        while i >=0 and t[i][j]==t[i-1][j]:
            i = i - 1

        # if i>0:
        #     S.append(i)
        #     S.append(j)
        #     j = j - 1
        #     i = i - 1
        R.append(i)
        R.append(j)
        j = j - 2
        i = i - 1
    R = sorted(R)
    R = set(R)
    R = np.array(R)
    return t, R

def construct(i,j,R,store):
    # print 'R = ', R
    n = len(R)
    # print 'store = ', store
    if R[i,j]==0:
        return
    if R[i,j]==1:
        store.append(i)
        return

    if R[i,j] == R[i+1][j]:
        construct(i+1,j,R, store)
    elif R[i,j] == R[i][j-1]:
        construct(i,j-1,R, store)
    elif R[i,j] == R[i+1][j-1] + 2:
        store.append(i)
        store.append(j)
        construct(i+1, j-1, R, store)

    return

def main():
    n, string = readFile(argv[1])
    table, root = lps(string)
    store = []

    # print 'table = \n', table

    print '\nThe original input sequence: \n', string

    print '\nTLength Of longest palindromic sequence: \n', table[0][n-1]

    '''
    Construct the longest palindromic sequence
    by using store list to add their index
    and then sort the index, and finally get the corresponding string
    via index.
    '''
    construct(0, n-1, table, store)
    store = sorted(store)
    result = ''
    for i in store:
        result = result + string[i]

    print '\nLongest palindromic sequence: \n', result


if __name__ == "__main__":
    main()
