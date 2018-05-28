from random import *

def simulate_improved(n = 20, i = 1000, x = 4):
    perc = 0
    for it in range(i):
        iterations = 1
        array = [False] * n                                     # empty list - MAIN LIST
        infected = []                                           # list of new nodes - WHILE NOT EMPTY -> SPREAD
        first_node = randint(0, n - 1)                          # 1st random node
        array[first_node] = True                                # insert first node
        nodes_start = rand_nodes(x, n, first_node)              # next 4 random nodes

        fill_array(array, nodes_start, infected)                #

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

    print("In " + str(perc / i * 100) + '%' + " cases all nodes received the packet")



def rand_nodes(x, n, f):
    '''
    returns list of
    '''
    nodes = sample(range(0, n), x)                                  # get x new nodes
    while f in nodes and not equalizer(nodes, x):                                               # must choose not parent nodes only
        nodes = sample(range(0, n), x)

    return nodes

def fill_array(array, nodes, infected):
    '''
    if node is empty -> fill in, and add as new node to spread, otherwise do nothing
    '''
    for new_node in nodes:
        if array[new_node] == False:
            array[new_node] = True
            infected.append(new_node)
        else:
            pass


'''POSSIBLE IMPROVEMENT'''
def equalizer(list, x):
    '''
    checks if odds == evens (+-1)
    '''
    count = 0

    for item in list:
        if item % 2 == 0 and count < x // 2:
            count += 1
        else:
            return False

    return True

# simulate_improved()














