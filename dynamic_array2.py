import ctypes


class DynamicArray(object):

    def __init__(self, size=2):
        self.size = size # Total size of array
        self.n = 0 # elements in array.
        # Create empty array of initial size 2
        self.arr = (ctypes.py_object * self.size)()


    # Check if array is full
    def isFull(self):
        return (self.size == self.n)


    # Double size of array
    def resize(self):
        self.size *= 2
        newArr = (ctypes.py_object * self.size)()
        for i in range(self.n):
            newArr[i] = self.arr[i]
        self.arr = newArr


    # Append element to end of array
    def append(self, ele):
        if self.isFull():
            self.resize()

        self.arr[self.n] = ele
        self.n += 1


    # Remove last element in array
    def remove(self):
        if (self.n == 0):
            print('Error: Cannot remove from empty array')
            return

        self.arr[self.n-1] = 0
        self.n -=1


    # Append element at index
    def insertAt(self, index, ele):
        if (index < 0 or index >= self.n):
            print('Error: index ' + str(index) + ' out of bounds')
            return

        if self.isFull():
            self.resize()

        for i in range(self.n-1, index-1, -1):
            self.arr[i+1] = self.arr[i]

        self.arr[index] = ele
        self.n += 1


    # Delete element at index
    def deleteAt(self, index):
        # Check if valid input
        if (index < 0 or index >= self.n):
            print('Error: index ' + str(index) + ' out of bounds')
            return
        # Corner case (remove from tail)
        if (index == self.n-1):
            self.arr[index] = 0
        # General case
        for i in range(index, self.n-1):
            self.arr[i] = self.arr[i+1]
        self.n -= 1


    # Print all elements in array.
    def print(self):
        print('total size : ' + str(self.size))
        for i in range(self.n):
            print(self.arr[i])


def test1():
    da = DynamicArray()
    da.append('1')
    da.append('2')
    da.print()
    da.append('4')
    da.append('4')
    da.print()
    da.append('6')
    da.print()
    da.remove()
    da.print()
    da.insertAt(2, '3')
    da.insertAt(10, '3')
    da.print()
    da.deleteAt(1)
    da.print()


def main():
    test1()


if __name__ == "__main__":
    main()