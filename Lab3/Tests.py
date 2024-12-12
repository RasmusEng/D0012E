import BST
import Node
import time
from random import randint, seed
import fungerar as b


def testBBSTGraph(c, nodes, low = -20000, high = 20000):
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
    test = lst + dups

    start_time = time.time()
    for i in test:
        bst.insert(i)
    end_time = time.time()
    print("Not balanced insert time", end_time - start_time)

    start_time = time.time()
    for i in lst:
        if not bst.lookUp(i, bst.head):
            print("fel")
    end_time = time.time()
    print("Not balanced lookup time", end_time - start_time)


    """ left_size, right_size = bbst.head_subtree_sizes()
    print(f"Left subtree size: {left_size}, Right subtree size: {right_size}") """
    left_size, right_size = bst.head_subtree_sizes()
    print(f"Left subtree size: {left_size}, Right subtree size: {right_size}")

    #bst.display()


def main():
    testBBSTGraph(0.51, 10000)

    """ for i in range(6, 11):
        print(i/10)
        testBBSTGraph(i/10, 5000000)
    """

if __name__ == '__main__':
    main()
