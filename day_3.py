import math

with open("inputs/day_3", "r") as f:
    wires = [line.rstrip("\n").split(",") for line in f.readlines()]

sign_x = {"U": 0, "D": 0, "L": -1, "R": 1}

sign_y = {"U": 1, "D": -1, "L": 0, "R": 0}


def get_coords(wire):
    coords = set()
    coords_with_steps = set()
    curr_pos = (0, 0)
    step_counter = 0

    for path in wire:
        dir = path[0]
        steps = int(path[1:])

        coords.update(
            (curr_pos[0] + sign_x[dir] * step, curr_pos[1] + sign_y[dir] * step)
            for step in range(1, steps + 1)
        )

        coords_with_steps.update(
            (
                curr_pos[0] + sign_x[dir] * step,
                curr_pos[1] + sign_y[dir] * step,
                step_counter + step,
            )
            for step in range(1, steps + 1)
        )

        curr_pos = (
            curr_pos[0] + sign_x[dir] * steps,
            curr_pos[1] + sign_y[dir] * steps,
        )
        step_counter = step_counter + steps

    return coords, sorted(coords_with_steps, key=lambda x: x[2])


def get_intersections(wire_1, wire_2):
    coords_1, _ = get_coords(wire_1)
    coords_2, _ = get_coords(wire_2)

    return coords_1.intersection(coords_2)


def get_min_distance(wire_1, wire_2):
    intersections = get_intersections(wire_1, wire_2)
    return min(abs(coord[0]) + abs(coord[1]) for coord in intersections)


def get_min_steps(wire_1, wire_2):
    _, coords_ws_1 = get_coords(wire_1)
    _, coords_ws_2 = get_coords(wire_2)
    intersections = get_intersections(wire_1, wire_2)

    import math

    min_steps = math.inf
    for intersection in intersections:
        steps_1 = next(c for c in coords_ws_1 if c[:-1] == intersection)[2]
        steps_2 = next(c for c in coords_ws_2 if c[:-1] == intersection)[2]
        min_steps = min(min_steps, steps_1 + steps_2)

    return min_steps


def main():
    print("Part 1\n------")
    # Sanity check
    test_wire_1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
    test_wire_2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")
    test_min_distance = get_min_distance(test_wire_1, test_wire_2)
    print("Test case (expected 159): {}".format(test_min_distance))

    min_distance = get_min_distance(wires[0], wires[1])
    print("Answer for part 1: {}\n".format(min_distance))

    print("Part 2\n------")
    test_min_steps = get_min_steps(test_wire_1, test_wire_2)
    print("Test case (expected 610): {}".format(test_min_steps))
    min_steps = get_min_steps(wires[0], wires[1])
    print("Answer for part 2: {}\n".format(min_steps))


if __name__ == "__main__":
    main()
