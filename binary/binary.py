import time

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def main():
    start_time = time.time()
    list = [i for i in range(1, 101)]
    item = int(input('Введите искомое число\n'))
    print(binary_search(list, item))
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
