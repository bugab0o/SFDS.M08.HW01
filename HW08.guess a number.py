if __name__ == '__main__':
    import numpy as np


def game_core_v3(hidden_number: int = 1) -> int:
    """Компьютер самостоятельно загадывает и угадывает число от 1 до 100.

    Args:
        hidden_number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: count. Число попыток. Defaults to 0.
    """
    high, low, count = 100, 0, 0  # верхняя граница, нижняя граница, счетчик
    attempt = np.random.randint(1, 101)  # случайная попытка компьютера угадать

    while True:
        count += 1
        if attempt == hidden_number:
            break
        else:
            attempt = (low + high) // 2
            if attempt < hidden_number:
                low = attempt + 1
            else:
                high = attempt - 1
    return count


print(f"Данный алгоритм угадывает случайное число за: {game_core_v3(hidden_number=np.random.randint(1, 101))} попыток")
