from typing import Optional, List


def _find_lines_matching_words(name: str, words: List[str]) -> List[str]:
    word_idx = 0
    letter_idx = 0
    started = False
    lines: List[str] = []
    block: List[str] = []

    while word_idx < len(words) and letter_idx < len(name):
        word = words[word_idx]
        letter = name[letter_idx]

        if letter in word.lower():
            if started:
                lines.append(' '.join(block))
                block = []
            else:
                started = True
            letter_idx += 1

        if started:
            block.append(word)

        word_idx += 1

    if letter_idx >= len(name):
        lines.append(' '.join(block))
        return lines

    return []


def _fill_whitespace(name: str, lines: List[str]) -> List[str]:
    indexes: List[int] = []
    largest_idx = 0
    for i, line in enumerate(lines):
        letter = name[i]
        idx = line.lower().index(letter)
        indexes.append(idx)
        if idx > largest_idx:
            largest_idx = idx

    adjusted_lines: List[str] = []
    for i, line in enumerate(lines):
        idx = indexes[i]
        offset = largest_idx - idx

        prefix = ''
        if offset > 0:
            prefix = ' ' * offset

        adjusted_lines.append(prefix + line)

    return adjusted_lines


def display_vertically(name: str, lyrics: str) -> Optional[str]:
    if not name:
        return

    name = name.lower()
    words = lyrics.split()

    if len(words) < len(name):
        return

    lines = _find_lines_matching_words(name, words)
    if lines:
        lines = _fill_whitespace(name, lines)
        return '\n'.join(lines)

    return None
