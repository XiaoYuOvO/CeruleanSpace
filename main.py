from multiprocessing.shared_memory import SharedMemory


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    SharedMemory()

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
