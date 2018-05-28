from random import *

def simulate(n = 20, i = 1000, x = 4):
    perc = 0
    for it in range(i):
        iterations = 1
        array = [False] * n                             # empty list - MAIN LIST
        infected = []                                   # list of new nodes - WHILE NOT EMPTY -> SPREAD
        first_node = randint(0, n - 1)                  # 1st random node
        array[first_node] = True                        # insert first node

        nodes_start = rand_nodes(x, n, first_node)

        fill_array(array, nodes_start, infected)

        while infected:
            iterations += 1
            for node in infected:
                nodes = rand_nodes(x, n, node)
                fill_array(array, nodes, infected)
                infected.remove(node)


        print("It took " + str(iterations) + " to finish")
        # print(array)
        if False not in array:
            perc += 1

    print("In " + str(perc/i * 100) + '%' + " cases all nodes received the packet")


def rand_nodes(x, n, f):
    nodes = sample(range(0, n), x)                      # get x new nodes
    while f in nodes:                                   # must choose not parent nodes only
        nodes = sample(range(0, n), x)

    return nodes

def fill_array(array, nodes, infected):
    for new_node in nodes:
        if array[new_node] == False:
            array[new_node] = True
            infected.append(new_node)


# simulate()











