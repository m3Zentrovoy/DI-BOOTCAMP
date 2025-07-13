class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

def main():
    calc = Calculator()
    self.add(10,5)

    # Задание: Вызови методы add, subtract, multiply и divide
    # 1. Сложи числа 10 и 5, выведи результат
    # 2. Вычти из 20 число 8, выведи результат
    # 3. Умножь 6 на 4, выведи результат
    # 4. Раздели 15 на 3, выведи результат
    # 5. Попробуй разделить 10 на 0, выведи результат

if __name__ == "__main__":
    main()