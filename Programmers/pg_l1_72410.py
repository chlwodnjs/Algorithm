import re


def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)

    while 1:
        if '..' in new_id:
            new_id = new_id.replace('..', '.')
        else:
            break

    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]

    new_id = list(new_id)
    if len(new_id) == 0:
        new_id.append('a')

    if len(new_id) > 15:
        if new_id[14] == '.':
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]

    if len(new_id) < 3:
        while 1:
            new_id.append(new_id[-1])
            if len(new_id) == 3:
                break

    for i in new_id:
        answer += i

    return answer