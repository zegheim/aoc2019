with open("inputs/day_3", "r") as f:
    wires = [line.rstrip("\n").split(",") for line in f.readlines()]

sign_x = {"U": 0, "D": 0, "L": -1, "R": 1}

sign_y = {"U": 1, "D": -1, "L": 0, "R": 0}


def get_coords(wire):
    coords = set()
    curr_pos = (0, 0)
    for path in wire:
        dir = path[0]
        steps = int(path[1:])

        coords.update(
            (curr_pos[0] + sign_x[dir] * step, curr_pos[1] + sign_y[dir] * step)
            for step in range(1, steps + 1)
        )

        curr_pos = (
            curr_pos[0] + sign_x[dir] * steps,
            curr_pos[1] + sign_y[dir] * steps,
        )

    return coords


def get_min_distance(wire_1, wire_2):
    coords_1 = get_coords(wire_1)
    coords_2 = get_coords(wire_2)
    intersections = coords_1.intersection(coords_2)

    return min(abs(coord[0]) + abs(coord[1]) for coord in intersections)


def main():
    # Sanity check
    wire_1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
    wire_2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")
    print("Test case (expected 159): {}".format(get_min_distance(wire_1, wire_2)))

    print("Answer for part 1: {}".format(get_min_distance(wires[0], wires[1])))


if __name__ == "__main__":
    main()
