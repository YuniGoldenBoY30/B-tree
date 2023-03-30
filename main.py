from btree import BTree


def main():
    B = BTree(3)
    
    for i in range(50):
        B.insert((i, 2 * i))
    
    B.print_tree(B.root)
    
    if B.search_key(8) is not None:
        print("\nFound")
    else:
        print("\nNot Found")


if __name__ == '__main__':
    main()
