
from pathlib import Path
import string
import sys


def count_words(text):
    """Return a dictionary like {"the": 42, "python": 7}."""
    counts = {}
    for word in text.lower().split():
        word = word.strip(string.punctuation)
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 word_counter.py <file> [top_n]")
        sys.exit(1)

    path = Path(sys.argv[1])
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    counts = count_words(path.read_text())
    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)

    for word, count in ranked[:top_n]:
        print(f"{word:<15} {count}")


if __name__ == "__main__":
    main()





