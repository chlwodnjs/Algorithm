def solution(phone_book):
    answer = True
    book = sorted(phone_book)
    xx = zip(book, book[1:])
    for c1, c2 in xx:
        if c2.startswith(c1):
            answer = False
    return answer
