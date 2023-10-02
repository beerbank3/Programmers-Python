def solution(picture, k):
    rows = len(picture)
    cols = len(picture[0])

    new_picture = []

    for row in picture:
        new_row = []
        for pixel in row:
            new_row.append(pixel * k)
        for i in range(k):
            new_picture.append(''.join(new_row))

    return new_picture