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


def calculate_distance(p1, p2=(0.0, 0.0, 0.0)):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    return math.sqrt(dx**2 + dy**2 + dz**2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    point1 = get_player_pos()
    print(f"Got a first tuple: {point1}")
    print(f"It includes: X={point1[0]}, Y={point1[1]}, Z={point1[2]}")
    dist_center = calculate_distance(point1)
    print(f"Distance to center: {round(dist_center, 4)}")
    print("Get a second set of coordinates")
    point2 = get_player_pos()
    dist_between = calculate_distance(point1, point2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_between, 4)}")
