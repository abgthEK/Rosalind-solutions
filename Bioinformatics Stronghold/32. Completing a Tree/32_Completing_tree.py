'''
Problem:

Given: A positive integer n (n ≤ 1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.

Sample Dataset
10
1 2
2 8
4 10
5 9
6 10
7 9

Sample Output
3

'''

f = open('rosalind_tree.txt', 'r')

lines = f.read().splitlines()

def min_edges(lines):
    n = int(lines[0])
    adj_list = [x.split() for x in lines[1:]]
    return n - len(adj_list) - 1

print(min_edges(lines))