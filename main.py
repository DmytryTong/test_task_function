import re
from collections import defaultdict


def word_frequency(paragraph_to_work_with: list) -> dict:
    frequency_to_work_with = defaultdict(int)

    for sentence in paragraph_to_work_with:
        # Розбиваємо речення на слова
        words = re.findall(r'\b\w+\b', sentence.lower())

        # Оновлюємо частоти слів
        for word in words:
            frequency_to_work_with[word] += 1

    return dict(frequency_to_work_with)


if __name__ == '__main__':
    paragraph = [
        "The quick brown fox",
        "jumps over the lazy dog.",
        "The dog barks,",
        "and the fox runs away."
    ]

    frequency = word_frequency(paragraph)
    print(frequency)

    # Нижче навів кейси зі зміненним paragraph
    # для перевірки корректності роботи функції
    paragraph = [
        "The, quick, brown, fox",
        "jumps, over, the, lazy, dog.",
        "The. dog. barks,",
        "and. the. fox. runs. away."
    ]

    frequency = word_frequency(paragraph)
    print(frequency)

    paragraph = [
        "The, quick brown fox jumps over the lazy dog.",
        "The dog barks,",
        "and the fox runs away."
    ]

    frequency = word_frequency(paragraph)
    print(frequency)

    paragraph = [
        "The, quick brown fox jumps over the lazy dog."
        " The dog barks, and the fox runs away."
    ]

    frequency = word_frequency(paragraph)
    print(frequency)
