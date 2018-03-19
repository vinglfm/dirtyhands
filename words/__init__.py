import sys
from urllib.request import urlopen


def fetch(url):
    with urlopen(url) as story:
        words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                words.append(word)
        return words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])