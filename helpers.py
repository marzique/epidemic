from random import *

def simulate(n = 20, i = 1000, x = 4):
    perc = 0
    for it in range(i):
        array = [False] * n                             # empty list - MAIN LIST
        occupied = []                                   # list of occupied nodes - TO STOP
        infected = []                                   # list of new nodes - WHILE NOT EMPTY -> SPREAD
        first_node = randint(0, n - 1)                  # 1st random node
        array[first_node] = True                        # insert first node

        nodes_start = rand_nodes(x, n, first_node)

        fill_array(array, nodes_start, occupied, infected)

        while infected:
            for node in infected:
                nodes = rand_nodes(x, n, node)
                fill_array(array, nodes, occupied, infected)
                infected.remove(node)

        print(array)
        if False not in array:
            perc += 1

    print(str(perc/10) + ' %')



def rand_nodes(x, n, f):
    nodes = sample(range(0, n), x)                      # get x new nodes
    while f in nodes:                                   # must choose not parent nodes only
        nodes = sample(range(0, n), x)

    return nodes

def fill_array(array, nodes, occupied, infected):
    for new_node in nodes:
        if array[new_node] == False:
            occupied.append(new_node)
            array[new_node] = True
            infected.append(new_node)


simulate()











