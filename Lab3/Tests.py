import BST
import Node
import time
from random import randint, seed
import fungerar as b
import matplotlib.pyplot as plt

def testBBSTGraph(c, nodes, low = -1500, high = 1500):
    seed(0)
    bst = b.BST(c)

    lst = []
    dups = []
    se = 0
    while len(lst) < nodes:
        se += 1
        seed(se)
        ri = randint(low, high)
        if ri in lst:
            dups.append(ri)
        else:
            lst.append(ri)
    test = lst

    start_time = time.time()
    for i in test:
        bst.insert(i)
    end_time = time.time()
    insert_time = end_time - start_time
    print("Insert time", insert_time)

    sorts = sorted(lst)
    
    lst.sort(reverse=True)
    start_time = time.time()

    for i in lst:
        if not bst.lookUp(i, bst.head):
            print("fel")
    end_time = time.time()
    lookup_time = end_time - start_time
    print("Lookup time", lookup_time)

    left_size, right_size = bst.head_subtree_sizes()
    print(f"Left subtree size: {left_size}, Right subtree size: {right_size}")
    
    start_time = time.time()
    for i in sorts:
        bst.insert(i)
    end_time = time.time()
    worst_insert_time = end_time - start_time
    print("Insert time", worst_insert_time)

    return insert_time, lookup_time, worst_insert_time


def main():
    look = []
    c_val = []
    ins = []
    wins = []
    for j in range(51, 99, 1):
        c_val.append(j/100)
        inset_time, lookup_time, worstins_time = testBBSTGraph(j/100, 10000, -10000, 10000)
        look.append(lookup_time)
        ins.append(inset_time)
        wins.append(worstins_time)
    print(look)
    print(c_val)
    print(ins)
    print(worstins_time)
    plt.plot(c_val, wins)
    plt.title("Insert worst case")
    plt.xlabel("C value")
    plt.ylabel("Time (s)")
    plt.show()
    plt.plot(c_val, look)
    plt.title("Lookup case")
    plt.xlabel("C value")
    plt.ylabel("Time (s)")
    plt.show()
    plt.plot(c_val, ins)
    plt.title("Insert random case")
    plt.xlabel("C value")
    plt.ylabel("Time (s)")
    plt.show()

if __name__ == '__main__':
    main()
