from btree import BTree


def search(B: BTree):
    data = int(input("Entre el key a buscar: "))
    return print(f"Encontrado la key: {data}" if B.search_key(data) is not None else f"No encontrado la key {data}")


def show(B: BTree):
    return B.print_tree(B.root)


def sum_data(B):
    return print(f"La suma de los elementos es: {B.sum_values(B.root)}")


def create_tree():
    b_tree = BTree(3)
    for i in range(1, 16):
        b_tree.insert((i, 2 * i))
    return b_tree


def main():
    b_tree = create_tree()
    while True:
        print('La formación del arbol se realizo de forma automática, con 10 valores y con valor mínimo 3')
        print('Menú de opciones: ')
        print('1- Buscar nodo')
        print('2- Mostrar árbol b-tree')
        print('3- Calcular suma de los elementos')
        print('4- Salir')
        try:
            options = int(input("Selecciones una opción: "))
        except Exception:
            print('Pruebe de nuevo')
            options = int(input("Selecciones una opción: "))

        match options:
            case 1:
                search(b_tree)
            case 2:
                show(b_tree)
            case 3:
                sum_data(b_tree)
            case _:
                exit()


if __name__ == '__main__':
    main()
