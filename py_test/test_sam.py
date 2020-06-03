from sam import nearest_square

# a = [int(x) for x in range(0,500)]

def test_5():
    assert(nearest_square(5) == 4)

def test_12():
    assert(nearest_square(-12) == 0)

def test_9():
    assert(nearest_square(9) == 9)

def test_23():
    assert(nearest_square(23) == 25)