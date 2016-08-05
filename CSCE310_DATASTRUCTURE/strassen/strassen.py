#!/usr/bin/python
# -*- coding: utf-8 -*-


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

def getMatrix(file_name):
    i = -1;
    for line in open(file_name,'r').readlines():
        if(i==-1):
            n = int(line.strip());
            '''
            padding matrices
            '''
            new_n = int(math.pow(2, (math.ceil(math.log(n, 2)))))
            matrix = np.zeros(new_n * new_n).reshape(new_n, new_n)  #initalize padded new martix
            # matrix = numpy.zeros((n, n));
        elif(i < n):
            tokens = line.strip().split(" ");
            for j in range(len(tokens)):
                matrix[i][j] = float(tokens[j]);
        i=i+1;
    return matrix, n

# def ikjMatrixProduct(A, B):
#     n = len(A)
#     C = [[0 for i in xrange(n)] for j in xrange(n)]
#     for i in xrange(n):
#         for k in xrange(n):
#             for j in xrange(n):
#                 C[i][j] += A[i][k] * B[k][j]
#     return C
#
# def add(A, B):
#     n = len(A)
#     C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
#     for i in xrange(0, n):
#         for j in xrange(0, n):
#             C[i][j] = A[i][j] + B[i][j]
#     return C
#
# def subtract(A, B):
#     n = len(A)
#     C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
#     for i in xrange(0, n):
#         for j in xrange(0, n):
#             C[i][j] = A[i][j] - B[i][j]
#     return C

def strassen(A, B):
    a = len(A)
    b = len(B)
    if a != b:
        raise ValueError("Wrong size of matrices.")

    size = len(A)
    if size == 1:
        return A * B
    elif size == 2:
        M1 = (A[0, 0] + A[1, 1])*(B[0, 0] + B[1, 1])
        M2 = (A[1, 0] + A[1, 1])*(B[0, 0] )
        M3 = (A[0, 0])*(B[0, 1] - B[1, 1])
        M4 = (A[1, 1])*(B[1, 0] - B[0, 0])
        M5 = (A[0, 0] + A[0, 1])*(B[1, 1])
        M6 = (A[1, 0] - A[0, 0])*(B[0, 0] + B[0, 1])
        M7 = (A[0, 1] - A[1, 1])*(B[1, 0] + B[1, 1])
        C = np.zeros(2*2).reshape(2, 2)
        C[0, 0] = M1 + M4 - M5 + M7
        C[0, 1] = M3 + M5
        C[1, 0] = M2 + M4
        C[1, 1] = M1 + M3 - M2 + M6
        return C
    else:
        A00, A01, A10, A11 = A[:size/2, :size/2], A[:size/2, size/2:], A[size/2:, :size/2], A[size/2:, size/2:]
        B00, B01, B10, B11 = B[:size/2, :size/2], B[:size/2, size/2:], B[size/2:, :size/2], B[size/2:, size/2:]
        #print A00, A01, A10, A11
        #print 'multi'
        #print B00, B01, B10, B11
        P1 = strassen((A00 + A11), (B00 + B11))
        P2 = strassen((A10 + A11), (B00))
        P3 = strassen((A00), (B01 - B11))
        P4 = strassen((A11), (B10 - B00))
        P5 = strassen((A00 + A01), (B11))
        P6 = strassen((A10 - A00), (B00 + B01))
        P7 = strassen((A01 - A11), (B10 + B11))
        C = np.zeros(size*size).reshape(size, size)
        C[:size/2, :size/2], C[:size/2, size/2:], C[size/2:, :size/2], \
                    C[size/2:, size/2:] = (P1 + P4 - P5 + P7), (P3 + P5), \
                        (P2 + P4), (P1 + P3 - P2 + P6)

        return C

def main():
    matrix_a, n = getMatrix(argv[1])
    matrix_b, n = getMatrix(argv[2])
    matrix_c = strassen(matrix_a, matrix_b)

    print 'matrix A = '
    printSolution(matrix_a, n)
    print
    print 'matrix B = '
    printSolution(matrix_b, n)
    print
    print 'matrix C = '
    printSolution(matrix_c, n)


def printSolution(matrix, n):
    '''
    print non padded matrix only here
    '''
    for i in range(n):
        print matrix[i][:n]

if __name__ == "__main__":
    main()
