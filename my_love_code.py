import secrets
import string

def generate_secure_password(word_count=2):
    # Список простых слов для примера (в реальности можно взять из файла)
    words = ["python", "space", "pixel", "storm", "code", "neon", "delta", "frost"]
    
    # Выбираем случайные слова
    chosen_words = [secrets.choice(words).capitalize() for _ in range(word_count)]
    
    # Выбираем случайный спецсимвол
    symbol = secrets.choice("@#$%&*")
    
    # Генерируем случайное число
    number = secrets.randbelow(100)
    
    # Собираем всё вместе
    password = f"{symbol}".join(chosen_words) + str(number)
    return password

# Создаем пароль
new_password = generate_secure_password()
print(f"Твой новый безопасный пароль: {new_password}")
