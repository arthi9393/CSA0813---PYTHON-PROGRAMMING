from datetime import datetime

def save_returns(books, log_path="returns.log"):
    with open(log_path, "a", encoding="utf-8") as log:
        for book in books:
            if book.strip():
                log.write(book.strip() + "\n")

def process(day_file):
    try:
        with open(day_file, "r", encoding="utf-8") as source:
            books = source.read().splitlines()
        save_returns(books)
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, OSError) as error:
        with open("errors.log", "a", encoding="utf-8") as log:
            log.write(f"{datetime.now().isoformat()} | {day_file} | "
                      f"{type(error).__name__}: {error}\n")

if __name__ == "__main__":
    for filename in ("day1.txt", "day2.txt", "day3.txt"):
        process(filename)
    with open("returns.log", encoding="utf-8") as f:
        print(f.read())
