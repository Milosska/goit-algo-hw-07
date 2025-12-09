from src.decorators import handle_errors
from src.handlers import insert, min_value_node, max_value_node, get_total


@handle_errors
def main():
    root = None
    keys = [
        10,
        20,
        30,
        40,
        50,
        -10,
        -20,
    ]

    for key in keys:
        root = insert(root, key)

    print(root)

    min_value = min_value_node(root)
    print(min_value.__str__(prefix="Мінімальне значення: "))

    max_value = max_value_node(root)
    print(max_value.__str__(prefix="Максимальне значення: "))

    total = get_total(root)
    print(f"Сума значень вузлів дерева: {total}")


if __name__ == "__main__":
    main()
