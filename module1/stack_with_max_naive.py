import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []  # Main stack to store the actual values
        self.__max_stack = []  # Auxiliary stack to keep track of the maximum values

    def Push(self, value):
        # Push the value onto the main stack
        self.__stack.append(value)

        # Update the max stack
        if not self.__max_stack or value >= self.__max_stack[-1]:
            self.__max_stack.append(value)

    def Pop(self):
        assert(len(self.__stack))
        value = self.__stack.pop()

        # If the popped value is the current max, pop it from the max stack as well
        if value == self.__max_stack[-1]:
            self.__max_stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__max_stack[-1]  # The current maximum is the top of the max stack


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)  # Handle unexpected input
