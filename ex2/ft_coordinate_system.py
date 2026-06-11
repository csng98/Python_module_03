import math


def get_player_pos():
    while True:
        pos = input("Enter new coordinates as floats in format 'x,y,z': ")
        current_number = ""
        parsed_parts = []
        for char in pos:
            if char == ",":
                parsed_parts = parsed_parts + [current_number]
                current_number = ""
            elif char != " ":
                current_number = current_number + char
        parsed_parts = parsed_parts + [current_number]
        if len(parsed_parts) != 3 or "" in parsed_parts:
            print("Invalid syntax")
            continue
        try:
            x = float(parsed_parts[0])
            y = float(parsed_parts[1])
            z = float(parsed_parts[2])
            return (x, y, z)
        except ValueError:
            for part in parsed_parts:
                try:
                    float(part)
                except ValueError:
                    print(f"Error on parameter '{part}': could not "
                          f"convert string to float: '{part}'")
                    break


