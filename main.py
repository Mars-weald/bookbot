import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as book:
        contents = book.read()
    return contents

from stats import words_in_book, characters_in_book, sordid

def main():
    x = get_book_text(sys.argv[1])
    y = words_in_book(x)
    z = characters_in_book(x)
    aa = sordid(z)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ---------- ")
    print(f"Found {y} total words")
    print("--------- Character Count -------")
    for item in aa:
        print(f"{item["character"]}: {item["number"]}")
    print("============= END ===============")
main()