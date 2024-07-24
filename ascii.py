import random

def print_square(size):
    for _ in range(size):
        print('* ' * size)

def print_triangle(size):
    for i in range(1, size + 1):
        print('* ' * i)

def print_diamond(size):
    for i in range(size):
        print(' ' * (size - i - 1) + '* ' * (i + 1))
    for i in range(size - 2, -1, -1):
        print(' ' * (size - i - 1) + '* ' * (i + 1))

def print_car():
    car = [
        "    ______",
        "  __/__|__\\___",
        " |  _     _  |",
        " '-(_)---(_)--'"
    ]
    for line in car:
        print(line)

def print_bee():
    bee = [
        "  \\     /",
        "   \\   /",
        "   /   \\",
        "  |  O  |",
        "   \\___/"
    ]
    for line in bee:
        print(line)

def print_tree():
    tree = [
        "    ^",
        "   ^^^",
        "  ^^^^^",
        " ^^^^^^^",
        "    |"
    ]
    for line in tree:
        print(line)

def print_star_pattern(size):
    for i in range(size):
        print(' '.join(['*' for _ in range(i + 1)]))

def print_hash_pattern(size):
    for i in range(size):
        print('# ' * size)

def print_dots_pattern(size):
    for i in range(size):
        print('. ' * (size - i))

def print_heart():
    heart = [
        "  **     **  ",
        " *  *   *  * ",
        "*    * *    *",
        " *           *",
        "  *         * ",
        "   *       *  ",
        "    *     *   ",
        "     *   *    ",
        "      * *     ",
        "       *      "
    ]
    for line in heart:
        print(line)

def print_random_pattern(size):
    patterns = [
        'square', 'triangle', 'diamond', 
        'car', 'bee', 'tree', 
        'star', 'hash', 'dots', 'heart'
    ]
    pattern = random.choice(patterns)

    if pattern in ['square', 'triangle', 'diamond']:
        print(f"Generating a {pattern} pattern of size {size}:\n")
        if pattern == 'square':
            print_square(size)
        elif pattern == 'triangle':
            print_triangle(size)
        elif pattern == 'diamond':
            print_diamond(size)
    elif pattern == 'car':
        print("Generating a car pattern:\n")
        print_car()
    elif pattern == 'bee':
        print("Generating a bee pattern:\n")
        print_bee()
    elif pattern == 'tree':
        print("Generating a tree pattern:\n")
        print_tree()
    elif pattern == 'star':
        print(f"Generating a star pattern of size {size}:\n")
        print_star_pattern(size)
    elif pattern == 'hash':
        print(f"Generating a hash pattern of size {size}:\n")
        print_hash_pattern(size)
    elif pattern == 'dots':
        print(f"Generating a dots pattern of size {size}:\n")
        print_dots_pattern(size)
    elif pattern == 'heart':
        print("Generating a heart pattern:\n")
        print_heart()

if __name__ == "__main__":
    size = int(input("Enter the pattern (1-10): "))
    print_random_pattern(size)
