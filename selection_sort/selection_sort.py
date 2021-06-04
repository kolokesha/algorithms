def findBiggest (arr):
    return(max(arr))

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        biggest = findBiggest(arr)
        newArr.append(biggest)
        arr.remove(biggest)
    return newArr

def main():
    user_arr = input().split()
    arr = list(map(int, user_arr))
    print(selectionSort(arr))

if __name__ == '__main__':
    main()

