from queue import PriorityQueue
from queue import Queue
from math import sqrt

class Node:
    def __init__(self, loc_x, loc_y, prev):
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.prev = prev
        if(prev != None):
            self.numOfMoves = prev.numOfMoves + 1
        else:
            self.numOfMoves = 0

def answer(src, dest):
    curr = src
    curr_x = src % 8
    curr_y = src // 8
    curr_node = Node(curr_x, curr_y, None)
    q = Queue()
    q.put(curr_node)
    while(True):
        curr_node = q.get()
        if (curr_node.loc_x + curr_node.loc_y * 8) == dest:
            return curr_node.numOfMoves
        moves = possible_moves(curr_node.loc_x, curr_node.loc_y)
        for i in range(len(moves)):
            x = moves[i] % 8
            y = moves[i] // 8
            h = Node(x, y, curr_node)
            # priority = h.numOfMoves + heur(moves[i], dest)
            # print(priority)
            q.put(h)


def possible_moves(src_x, src_y):
    moves_x = [-1, 1, -1, 1, 2, -2, 2, -2]
    moves_y = [-2, -2, 2, 2, 1, 1, -1, -1]
    output = []
    for i in range(len(moves_x)):
        if moves_x[i]+src_x >= 0 and moves_y[i]+src_y >= 0 and moves_x[i]+src_x <= 7 and moves_y[i]+src_y <= 7:
            output.append((moves_y[i] + src_y) * 8 + (moves_x[i] + src_x))
    return output

def heur(src, dest):
    src_x, src_y = src % 8, src // 8
    dest_x, dest_y = dest % 8, dest // 8
    return sqrt((dest_x - src_x) ** 2 + (dest_y - src_y) ** 2)
