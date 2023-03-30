# Searching a key on a B-tree in Python


# Create a node
class BTreeNode:
    def __init__(self, leaf = False):
        self.leaf = leaf
        self.keys = []
        self.child = []


# Tree
class BTree:
    def __init__(self, min_order_tree):
        self.root = BTreeNode(True)
        self.min_order_tree = min_order_tree
        
        # Insert node
    
    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.min_order_tree) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)
        
        # Insert nonfull
    
    def insert_non_full(self, nodo, key):
        i = len(nodo.keys) - 1
        if nodo.leaf:
            nodo.keys.append((None, None))
            while i >= 0 and key[0] < nodo.keys[i][0]:
                nodo.keys[i + 1] = nodo.keys[i]
                i -= 1
            nodo.keys[i + 1] = key
        else:
            while i >= 0 and key[0] < nodo.keys[i][0]:
                i -= 1
            i += 1
            if len(nodo.child[i].keys) == (2 * self.min_order_tree) - 1:
                self.split_child(nodo, i)
                if key[0] > nodo.keys[i][0]:
                    i += 1
            self.insert_non_full(nodo.child[i], key)
        
        # Split the child
    
    def split_child(self, nodo, i):
        min_order_tree = self.min_order_tree
        y = nodo.child[i]
        z = BTreeNode(y.leaf)
        nodo.child.insert(i + 1, z)
        nodo.keys.insert(i, y.keys[min_order_tree - 1])
        z.keys = y.keys[min_order_tree: (2 * min_order_tree) - 1]
        y.keys = y.keys[0: min_order_tree - 1]
        if not y.leaf:
            z.child = y.child[min_order_tree: 2 * min_order_tree]
            y.child = y.child[0: min_order_tree - 1]
    
    # Print the tree
    def print_tree(self, x, l = 0):
        print("Level ", l, " ", len(x.keys), end = ":")
        for i in x.keys:
            print(i, end = " ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)
    
    # Search key in the tree
    def search_key(self, key, x = None):
        if x is not None:
            i = 0
            while i < len(x.keys) and key > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and key == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search_key(key, x.child[i])
        
        else:
            return self.search_key(key, self.root)
    
    def sum_values(self, node):
        s = 0
        for i in node.keys:
            s += i[1]
        
        if len(node.child) > 0:
            for i in node.child:
                s += self.sum_values(i)
        
        return s
