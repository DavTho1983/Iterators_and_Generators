def range_2d(width, height):
    """Produce a stream of 2d coordinates"""
    for y in range(height):
        for x in range(width):
            yield x, y

#Change nested loop into single loop with iterator
for col, row in range_2d(width, height):
    value = spreadsheet.get_value(col, row)
    do_something(value)

    if this_is_my_value(value):
        break
