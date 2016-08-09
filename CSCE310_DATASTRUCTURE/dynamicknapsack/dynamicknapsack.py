#!/usr/bin/python
# -*- coding: utf-8 -*-
# dynamicknapsack.py

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
        if(i==-1):
            tokens = line.strip().split(" ");
            n, W = int(tokens[0]), int(tokens[1])
            weights = []
            values = []

        elif(i == 0):
            tokens = line.strip().split(" ");
            for t in tokens:
                weights.append( int(t) )
        elif(i == 1):
            tokens = line.strip().split(" ");
            for t in tokens:
                values.append( int(t) )
        i=i+1;

    return n, W, weights, values


def dynamicknapsack(n, W, wt, val):
    '''
    tableau t
    '''
    # t = [[0 for x in range(W+1)] for x in range(n+1) ]
    t = np.zeros((n+1, W+1))
    '''
    S store included item
    '''
    S = []
    # optimal = set()

    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                t[i][w] = 0
            elif wt[i-1] <= w:

                # t[i][w] = max( val[i-1] + t[i-1][w-wt[i-1]], t[i-1][w] )
                if val[i-1] + t[i-1][w-wt[i-1]] <= t[i-1][w] :
                    t[i][w] = t[i-1][w] # not include the ith item
                else:
                    t[i][w] = val[i-1] + t[i-1][w-wt[i-1]]
                    # print i
                    # S.append( i ) # include the ith item
            else:
                t[i][w] = t[i-1][w] # not include

    i = n
    j = W
    while i >=1 and j >=1:
        while i >=1 and t[i][j]==t[i-1][j]:
            i = i-1

        if i>0:
            S.append(i)
            j = j - wt[i-1]
            i = i-1

    S=sorted(S)
    optimal_val = []
    optimal_wt = []
    if S:
        for s in S:
            optimal_val.append( val[s-1] )
            optimal_wt.append( wt[s-1] )
    return t, S, optimal_val, optimal_wt

def printSolution(items):
    n = len(items)
    '''
    print one line in for loop
    #
    print item, in Python 2.7
    print(item, end=" ") in Python 3
    #
    '''
    for i in range(n):
        print ''.join(str(items[i]))



def main():
    n, W, wt, val  = readFile(argv[1])
    table, S, optimal_val, optimal_wt = dynamicknapsack(n, W, wt, val)

    # print 'n = ', n
    # print 'W = ', W
    # print 'wt = ', wt
    # print 'val = ', val
    # print 'optimal_value = ', table[n][W]

    if not S:
        print 'No Optimal Knapsack Solution.'
        return 0

    print '\nResulting table: \n', table
    # printSolution(table)

    print '\nMaximum Capacity: ', W

    print '\nOptimal KnapSack Solution: ', S

    print '\nOptimal Values: ', optimal_val

    print '\nOptimal Weight: ', optimal_wt


    print '\nOptimal Value Taken : ', sum(optimal_val)

    print '\nOptimal Weight Taken: ', sum(optimal_wt)

    return 1

if __name__ == "__main__":
    main()
