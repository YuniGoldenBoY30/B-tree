from btree import BTree


def main():
    B = BTree(3)
    
    for i in range(1, 10):
        B.insert((i, 2 * i))
    
    B.print_tree(B.root)
    
    if B.search_key(12) is not None:
        print("\nFound")
    else:
        print("\nNot Found")
    
    print(B.sum_values(B.root))


if __name__ == '__main__':
    main()
