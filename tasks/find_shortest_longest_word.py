__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    words = text.split()
    shortest_word, longest_word = None, None
    if words:
        shortest_word, longest_word = min(words, key=len), max(words, key=len)
    return shortest_word, longest_word
