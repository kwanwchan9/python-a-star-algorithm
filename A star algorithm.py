# List the map graph as a tree structure with the cost and path for each node
tree = {'V0': [['V1', 1], ['V2', 6], ['V3', 6]],
        'V1': [['V0', 1], ['V4', 25], ['V6', 21]],
        'V2': [['V0', 6], ['V4', 24], ['V5', 21]],
        'V3': [['V0', 6], ['V5', 16], ['V6', 63]],
        'V4': [['V1', 25], ['V2', 24], ['V7', 44]],
        'V5': [['V2', 21], ['V3', 16], ['V7', 12]],
        'V6': [['V1', 21], ['V3', 63], ['V7', 13]],
        'V7': [['V4', 44], ['V5', 12], ['V6', 13]],
        }

def A_Star(start_node, goal_node):
    opened_list = set([start_node])      # list for nodes that have been visited
    closed_list = set([])                # list for nodes and all next node that have visted

    g = {}                              # cost from start nodes to other nodes
    g[start_node] = 0

    parents = {}
    parents[start_node] = start_node

    while len(opened_list) > 0:
        n = None

        # find the next node with lowest cost 
        heur = {'V0': 0, 'V1': 0, 'V2': 0, 'V3': 0, 'V4': 0, 'V5': 0, 'V6': 0, 'V7': 0}  # heuristic function (set 0 for for all nodes in this case)

        for v in opened_list:
            if n == None or g[v] + heur[v] < g[n] + heur[n]:
                n = v

        # if the current node reach the goal_node, reverse the optimal sequence
        if n == goal_node:
            reverse_path = []

            while parents[n] != n:
                reverse_path.append(n)
                n = parents[n]
            reverse_path.append(start_node)

            reverse_path.reverse()
            
            print('optimal nodes sequence: {}'.format(reverse_path))
            print('total cost for travel : {}'.format(g[m]))
            return reverse_path

        # for all neighbors of the current node do
        for (m, weight) in tree[n]:
            # add current nodes to open_list and it's parents
            if m not in opened_list and m not in closed_list:
                opened_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            # update parent data and g data, and moved the nodes from closed_list to open_list
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        opened_list.add(m)

        opened_list.remove(n)
        closed_list.add(n)

    return None

if __name__ == '__main__':  
    shortest_path = A_Star('V0', 'V7')

