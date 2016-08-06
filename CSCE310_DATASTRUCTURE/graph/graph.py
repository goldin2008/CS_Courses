#!/usr/bin/python
# -*- coding: utf-8 -*-
# graph.py

from sys import argv
import numpy as np
import heapq
import sys
import operator

# CSCE 310 Assignment 3
# yuleinku@gmail.com
#
#
# Improvements welcome

# graph_lyu_input_001.txt is the same as the one in the paper
#
# graph_lyu_input_002.txt
# /* Let us create following weighted graph
#          10
#     0--------1
#     |  \     |
#    6|   5\   |15
#     |      \ |
#     2--------3
#         4       */

'''
Vertex Class
'''
class Vertex:
    def __init__(self, node):
        self.id = node
        self.neighbor = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def __str__(self):
        return str(self.id) + ' neighbor: ' + str([x.id for x in self.neighbor])

    def add_neighbor(self, neighbor, weight=0):
        self.neighbor[neighbor] = weight

    def get_connections(self):
        return self.neighbor.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.neighbor[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

'''
Graph Class
'''
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

'''
Stack Class for DFS
'''
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

'''
Queue Class For BFS
'''
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

'''
Priority Queue Class For PrimMST
'''
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def isEmpty(self):
        return self._queue == []

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

'''
Read file and construct Graph
'''
def getGraph(file_name):
    g = Graph()
    i = -1;
    for line in open(file_name,'r').readlines():
        if(i==-1):
            n = int(line.strip());
            for j in range(n):
                '''
                Note: must use str(), it would consider i and str(i) as diff
                parameters, where i is integer, and str(i) is string.
                '''
                g.add_vertex( str(j) )
                # print 'g.get = ', g.get_vertex( str(j) )
        else:
            tokens = line.strip().split(" ");
            g.add_edge( tokens[0], tokens[1], float(tokens[2]) )
        i=i+1;
    return g

# DFS - Depth First Search Tree
# Data Structure: Stack
def dfs(graph, start_vertex, path):

    if not path:
        visited_path = []
    else:
        visited_path = path

    if start_vertex.visited:
        return visited_path

    s = Stack()
    s.push(start_vertex)
    visited_path.append( int( start_vertex.get_id() ) )
    count = 1
    start_vertex.set_visited()

    while not s.isEmpty():
        count = count + 1
        vertex = s.peek()
        min_value = sys.maxint
        white_id = ''

        for v in vertex.get_connections():
            if not v.visited and int(v.get_id()) < min_value:
                min_value = int(v.get_id())
                white_id = v.get_id()

        if not white_id:
            s.pop()
        else:
            next_vertex = graph.get_vertex(white_id)
            s.push(next_vertex)
            next_vertex.set_visited()
            visited_path.append( int( next_vertex.get_id() ) )

    return visited_path

# BFS - Breadth First Search Tree
# Data Structure: Queue
def bfs(graph, start_vertex, path):

    if not path:
        visited_path = []
    else:
        visited_path = path

    if start_vertex.visited:
        return visited_path

    q = Queue()
    q.enqueue(start_vertex)
    visited_path.append( int( start_vertex.get_id() ) )
    count = 1
    start_vertex.set_visited()

    while not q.isEmpty():
        vertex = q.dequeue()
        min_value = sys.maxint
        white_id = ''
        '''
        The diff between list and tuple is list = [], and tuple = list()
        '''
        order_tuple = list()
        '''
        sort the white vertex by weight from x to y
        '''
        for v in vertex.get_connections():
            if not v.visited:
                v_weight = vertex.get_weight( v )
                v_id = v.get_id()
                order_tuple.append( (v_weight, v_id) )

        order_tuple.sort()

        '''
        foreach y in neighbor of x
        '''
        for t in order_tuple:
            t_id = t[1]
            t_vertex = graph.get_vertex(t_id)
            count = count + 1
            q.enqueue(t_vertex)
            t_vertex.set_visited()
            visited_path.append( int( t_id ) )

        count = count + 1

    # print '\nstart_vertex = ', start_vertex
    # print 'path = ', visited_path

    return visited_path

# Kruskal's Algorithm - Minimum Spanning Tree
def kruskalMST():

    return 0

# Prim's Algorithm - Minimum Spanning Tree
# find a minimum spanning tree for a connected weighted undirected graph
# def primMST(graph, start_vertex):
def primMST(graph):

    start_vertex = graph.get_vertex('0')
    # print start_vertex.get_id()
    '''
    Edges tuple For MST : (edge, start_vertex, end_vertex)
    '''
    E_T = list()

    '''
    Vertices list For MST : vertex_id
    '''
    V_T = [ start_vertex.get_id() ]

    '''
    Edges tuple For Fringe Vertices : (edge, start_vertex, end_vertex)
    '''
    E = list()

    for u in start_vertex.neighbor:
        weight = start_vertex.get_weight(u)
        E.append( (weight, start_vertex.get_id(), u.get_id()) )

    n = graph.num_vertices

    heapq.heapify(E)

    for i in range(n-1):
        heapq.heapify(E)
        if not E:
            for v in graph.vert_dict:
                if v not in V_T:
                    start_vertex = graph.get_vertex(v)

            E = list()
            for u in start_vertex.neighbor:
                weight = start_vertex.get_weight(u)
                E.append( (weight, start_vertex.get_id(), u.get_id()) )
                heapq.heapify(E)

        e = heapq.heappop(E)

        edge, u_node, v_node  = e[0], e[1], e[2]

        if u_node in V_T and v_node not in V_T:

            '''
            1. v is not in V_T and put it in V_T
            '''
            V_T.append( v_node )
            '''
            Note: the right bracket missing would always result problems.
            '''
            E_T.append( (edge, u_node, v_node ) )
            # print 'E_T = ', E_T
            # print 'V_T = ', V_T

            v = graph.get_vertex(v_node)

            '''
            2. Put the edges coming from v in the E.
            '''
            for x in v.neighbor:
                weight = v.get_weight(x)
                E.append( (weight, v.get_id(), x.get_id()) )

            '''
            3. Check and remove the edges from two vertices already in V_T
            from fringe edges set E
            '''
            for t in E:
                if t[1] in V_T and t[2] in V_T:
                    E.remove(t)


        elif (u_node not in V_T and v_node in V_T):
            V_T.append( u_node )
            E_T.append( (edge, u_node, v_node ) )
            u = graph.get_vertex(u_node)
            for x in u.neighbor:
                weight = u.get_weight(x)
                E.append( (weight, u.get_id(), x.get_id()) )
            for t in E:
                if t[1] in V_T and t[2] in V_T:
                    E.remove(t)

    return V_T, E_T

# Dijkstra's Algorithm - Single Source Shortest Path
# rovides us with the shortest path from one particular
# starting node (0 in our case) to all other nodes in the graph
# Note: This is similar to the results of a breadth first search.
# The algorithm iterates once for every vertex in the graph;
# however, the order that we iterate over the vertices is controlled
# by a priority queue (actually, in the code, I used heapq).
# The value that is used to determine the order of the objects in the
# priority queue is dist. When a vertex is first created dist is set
# to a very large number.
def dijkstra(graph, start_vertex):
    # Set the distance for the start vertex to zero
    start_vertex = graph.get_vertex(start_vertex)
    start_vertex.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in graph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.neighbor:
        for next in current.neighbor:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                # print 'updated : current = %s next = %s new_dist = %s' \
                #         %(current.get_id(), next.get_id(), next.get_distance())
            # else:
                # print 'not updated : current = %s next = %s new_dist = %s' \
                #         %(current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in graph if not v.visited]
        heapq.heapify(unvisited_queue)
    return 0

# Floyd's Algorithm - All Pairs Shortest Path
def floyd():

    return 0

# def constructPath(graph, current_vertex, path):
#     current_vertex = graph.get_vertex(current_vertex)
#     if current_vertex.previous:
#         path.append( current_vertex.previous.get_id() )
#         constructPath(graph, current_vertex.previous, path)
#     return 1
#
# def printShortestPath(graph, start_vertex, end_vertex):
#     end_vertex = graph.get_vertex(end_vertex)
#     path = [end_vertex]
#     constructPath(graph, end_vertex, path)
#     # print '%s -> %s = (%s, %s, %3.2f) '
#     print 'The shortest path for %s : %s' %(end_vertex, path[::-1])

def shortest(current_vertex, path):
    ''' make shortest path from v.previous'''
    if current_vertex.previous:
        path.append(current_vertex.previous.get_id())
        shortest(current_vertex.previous, path)
    return 1

def printTraversal(path):
    for i in range( len(path)-1 ):
        print '%s, ' % path[i]

def main():

    '''#######################################################
    DFS
    #######################################################'''
    print 'Depth First Search Traversal: '
    g = getGraph(argv[1])
    path = []
    path = dfs(g, g.get_vertex('0'), path)
    '''
    Note: convert string to integer in order to sort by id
    I am not sure what's wrong with the Graph Data Structure, which
    can not store the vertex id in increasing order.
    '''
    vertex_list = g.get_vertices()
    vertex_list = [int(v) for v in vertex_list]

    # for v in sorted( vertex_list ):
    #     print v, type(v)

    if len(path) is g.num_vertices:
        print path
    else:
        for v in sorted( vertex_list ):
            if v is not 0:
                dfs( g, g.get_vertex( str(v) ), path )
        print path


    '''#######################################################
    BFS
    #######################################################'''
    print '\nBreadth First Search Traversal: '
    g = getGraph(argv[1])
    path = []
    path = bfs(g, g.get_vertex('0'), path)
    '''
    Note: convert string to integer in order to sort by id
    I am not sure what's wrong with the Graph Data Structure, which
    can not store the vertex id in increasing order.
    '''
    vertex_list = g.get_vertices()
    vertex_list = [int(v) for v in vertex_list]

    if len(path) is g.num_vertices:
        print path
    else:
        for v in sorted( vertex_list ):
            if v is not 0:
                bfs( g, g.get_vertex( str(v) ), path )
        print path



    '''#######################################################
    Minimum Spanning Tree
    #######################################################'''
    print '\nMinimum Spanning Tree: '
    g = getGraph(argv[1])
    vertex_list = g.get_vertices()
    vertex_list = [int(v) for v in vertex_list]

    print 'V = ', sorted( vertex_list )

    # V_T, E_T = primMST( g, g.get_vertex('0') )
    V_T, E_T = primMST( g )

    print 'E = '

    total_weight = 0
    for edge in E_T:
        print '(%s, %s, %3.2f)' %(edge[1], edge[2], edge[0] )
        total_weight = total_weight + edge[0]

    print 'Total Weight: ', total_weight





    '''#######################################################
    Shortest Paths
    #######################################################'''
    # print '\nShortest Paths: '
    # g = getGraph(argv[1])
    #
    # for i in range(g.num_vertices):
    #     g = getGraph(argv[1])
    #     start = g.get_vertex(str(i)).get_id()
    #     print '\nSOURCE Vertex = ', start
    #     dijkstra(g, start)
    #     end_list = g.get_vertices()
    #
    #     '''
    #     Note: convert string to integer in order to sort by id
    #     I am not sure what's wrong with the Graph Data Structure, which
    #     can not store the vertex id in increasing order.
    #     '''
    #     end_list = [int(x) for x in end_list if x != start]
    #     print 'TARGET Vertex = ', sorted(end_list)
    #     for t in sorted(end_list):
    #         t = str(t)
    #         end_vertex = g.get_vertex(t)
    #         path = [t]
    #         shortest(end_vertex, path)
    #         print '\n%s -> %s = ' %(start, t)
    #         n = len(path)
    #         total = 0
    #         for i in range(n-1):
    #             current = g.get_vertex( path[n-i-1] )
    #             next = g.get_vertex( path[n-i-2] )
    #             # print 'current.get_weight(next) = ', current.get_weight(next)
    #             total = total + current.get_weight(next)
    #             # print 'total = ', total
    #             # if total is not 0:
    #             if current.get_weight(next):
    #                 print '( %s , %s, %3.2f)'  % ( current.get_id(), next.get_id(), \
    #                         current.get_weight(next))
    #             else:
    #                 print 'No way.'
    #
    #         if total is not 0:
    #             print 'Path Weight = ', total
    #         else:
    #             print 'No Path.'



    # for v in g:
    #     print v.get_id()
    #
    # for v in sorted(g.vert_dict.values()):
    #     print v

    # print g.get_vertices(), type(g.get_vertices())
    # print sorted(g.get_vertices()), type(g.get_vertices()), type(sorted(g.get_vertices()))


    # print 'graph: ', g.num_vertices

    # print 'test = ', sorted(g.vert_dict.items(), key=operator.itemgetter(0))
    # g = sorted(g.vert_dict.items(), key=operator.itemgetter(0))

    # for v in g:
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print '( %s , %s, %3.2f)'  % ( vid, wid, v.get_weight(w))
    #
    # for v in g:
    #     print 'g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()])



if __name__ == "__main__":
    main()
