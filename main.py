# Необходимо реализовать класс Stack со следующими методами:
class Stack():
    def __init__(self):  # Создаем пустой список
        self.stack = []

    def isEmpty(self):  # проверка стека на пустоту. Метод возвращает True или False.
        return len(self.stack) == 0

    def push(self, item):  # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.stack.append(item)

    def pop(self):  # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        return self.stack.pop()

    def peek(self):  # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def size(self):  # возвращает количество элементов в стеке.
        return len(self.stack)


# необходимо решить задачу на проверку сбалансированности скобок
s = input()
stack = []
is_good = True
for i in s:
    if i in '({[':
        stack.append(i)
    elif i in ')}]':
        if not stack:
            is_good = False
            break
        op_br = stack.pop()
        if op_br == '(' and i == ')':
            continue
        if op_br == '{' and i == '}':
            continue
        if op_br == '[' and i == ']':
            continue
        is_good = False
        break
if is_good and len(stack) == 0:
    print('Сбалансированно')
else:
    print('Несбалансированно')

# примеры для input сбалансироанных строк:     (((([{}]))))     [([])((([[[]]])))]{()}     {{[()]}}
# примеры для input  несбалансированных строк:    }{}     {{[(])]}}     [[{())}]

s = Stack()

print(s.isEmpty())
s.push(5)
s.push('cap')
print(s.peek())
s.push(False)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
