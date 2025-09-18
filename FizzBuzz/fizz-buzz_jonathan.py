def fizzbuzz(maximum):
    result = []

    for number in range(1, maximum + 1):
        result.append(fizzbuzz_one(number))

    return result

def fizzbuzz_one(number: int) -> str:
    buzz, fizz = count_fizzbuzz(number)

    if fizz > 0 or buzz > 0:
        return "fizz" * fizz + "buzz" * buzz

    return number

def count_fizzbuzz(number: int) -> tuple[int, int]:
    fizz = 0
    buzz = 0
    if "3" in str(number):
        fizz += 1

    if "5" in str(number):
        buzz += 1

    if is_multiple_of(number, 3):
        fizz += 1
    if is_multiple_of(number, 5):
        buzz += 1
    return buzz, fizz

def is_multiple_of(number: int, divisor) -> bool:
    return number % divisor == 0

def test_xxx():
    assert fizzbuzz(1) == [1]
    assert fizzbuzz(2) == [1, 2]
    assert fizzbuzz(3) == [1, 2, "fizzfizz"]
    assert fizzbuzz(5) == [1, 2, "fizzfizz", 4, "buzzbuzz"]
    assert fizzbuzz(6) == [1, 2, "fizzfizz", 4, "buzzbuzz", "fizz"]
    assert fizzbuzz(10) == [1, 2, "fizzfizz", 4, "buzzbuzz", "fizz", 7, 8, "fizz", "buzz"]
    assert fizzbuzz(13) == [1, 2, 'fizzfizz', 4, 'buzzbuzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', "fizz"]
    assert fizzbuzz(15) == [1, 2, 'fizzfizz', 4, 'buzzbuzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', "fizz", 14, "fizzbuzzbuzz"]
    # assert fizzbuzz(53) == [1, 2, 'fizzfizz', 4, 'buzzbuzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', "fizz", 14, "fizzbuzzbuzz"]


# S - SRP - Single Responsability principle
# O
# L
# I
# D