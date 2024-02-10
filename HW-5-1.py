def caching_fibonacci():
    cache = {}  # Створюємо порожній словник для кешування результатів

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache: # Якщо результат вже збережений у кеші, повертаємо його
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Обчислюємо результат рекурсивно та зберігаємо його у кеш
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

# Використовуємо функцію для обчислення чисел Фібоначчі
print(fib(10))  #  55
print(fib(15))  #  610
