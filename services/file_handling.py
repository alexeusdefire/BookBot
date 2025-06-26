import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_signs = ',.!:;?'
    counter = 0
    if len(text) < start + size:
        size = len(text) - start
        text = text[start:start + size]
    else:
        if text[start + size] == '.' and text[start + size - 1] in end_signs:
            text = text[start:start + size - 2]
            size -= 2
        else:
            text = text[start:start + size]
        for i in range(size - 1, 0, -1):
            if text[i] in end_signs:
                break
            counter = size - i
    page_text = text[:size - counter]
    page_size = size - counter
    return page_text, page_size


def prepare_book(path: str) -> None:
    start = 0
    page_number = 1
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    while start < len(text):
        page_text, length = _get_part_text(text, start, PAGE_SIZE)
        if page_text:
            book[page_number] = page_text.lstrip()
            page_number += 1
            start += length

prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))