def draw_diamond(n):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
    n_index = alphabet.index(n)
    i = 0
    space = " "
    space_count = n_index
    middle_space = n_index
    result = f"""
"""

    while i < n_index:
        if i == 0:
            result += f"""{space * (space_count+1)}{alphabet[i]}{space * space_count}
"""
        else:
            result += f"""{space*space_count}{alphabet[i]}{(space*(middle_space+i-1))}{alphabet[i]}{space*space_count}
"""
        i+=1
        space_count -=1
        middle_space +=1
    i = n_index
    while i >= 0:
        if i == 0:
            result += f"""{space * (space_count+1)}{alphabet[i]}{space * space_count}
            """
        else:
            result += f"""{space * space_count}{alphabet[i]}{(space * (middle_space+i-1))}{alphabet[i]}{space * space_count}
"""
        i -= 1
        space_count += 1
        middle_space -= 1
    return result


draw = draw_diamond("C")
print(draw)
