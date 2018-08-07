def answer(l):
    node_l = [Node(i) for i in l]

    #Creates the DAG
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                node_l[i].connect(node_l[j])
    cnt = 0
    for i in node_l:
        for j in i.adj:
            cnt += len(j.adj)
    return cnt

#Represents our DAG
class Node:
    def __init__(self, val):
        self.adj = []
        self.val = val
        self.dist = [1]
        self.three = 0
    def connect(self, other):
        self.adj.append(other)
        # new_dist = []
        # hold_dist = [i + 1 for i in self.dist]
        # while(len(hold_dist) > 0 and len(other.dist) > 0):
        #     if hold_dist[0] == 3:
        #         other.three += 1
        #     if hold_dist[0] < other.dist[0]:
        #         new_dist.append(hold_dist.pop(0))
        #     elif hold_dist[0] > other.dist[0]:
        #         new_dist.append(other.dist.pop(0))
        #     else:
        #         other.dist.pop(0)
        #         new_dist.append(hold_dist.pop(0))
        # for i in hold_dist:
        #     if i == 3:
        #         other.three += 1
        #     new_dist.append(i)
        # for i in other.dist:
        #     if i == 3:
        #         other.three += 1
        #     new_dist.append(i)
        # other.dist = new_dist
    #def topological_sort(self):
