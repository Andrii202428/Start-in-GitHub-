import time
import sys

def typewriter_print(text, delay=0.05):
    """
    Выводит текст в консоль по одному символу с заданной задержкой.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Принудительно выводим символ в консоль
        time.sleep(delay)
    print()  # Переход на новую строку в конце

# Пример использования
message = "Привет! Я твой AI-помощник Gemini. Давай создадим что-нибудь крутое на Python!"
typewriter_print(message)
