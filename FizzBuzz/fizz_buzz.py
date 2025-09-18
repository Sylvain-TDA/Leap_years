def fizz():
    fizzbuzz_list = ""
    i = 1

    while i < 100:
        i_str = str(i)
        for i in i_str:
            if i % 3 == 0 and i % 5 == 0:
                fizzbuzz_list += "FizzBuzz "
            elif i % 5 == 0:
                fizzbuzz_list += "Buzz "
            elif i % 3 == 0 and i_str == 3:
                fizzbuzz_list += "Fizz "
            else:
                fizzbuzz_list += f"{i}"
            i += 1
    return fizzbuzz_list

d = fizz()
print(d)
