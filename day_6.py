import networkx as nx


class MapData(object):
    def __init__(self, orbits):
        self.orbits = orbits
        self.map = nx.DiGraph()

    def add_orbit(self, orbit):
        primary, secondary = orbit.split(")")
        self.map.add_edge(secondary, primary)

    def get_orbits(self, obj):
        return nx.algorithms.dag.descendants(self.map, obj)

    def populate(self):
        for orbit in self.orbits:
            self.add_orbit(orbit)


def test_case():
    orbits = "COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L".split(" ")
    md = MapData(orbits)
    md.populate()
    print(sum(len(md.get_orbits(obj)) for obj in md.map.__iter__()))


def main():
    print("Part 1\n------")
    with open("inputs/day_6", "r") as f:
        orbits = [orbit.rstrip("\n") for orbit in f.readlines()]
    md = MapData(orbits)
    md.populate()
    print(
        "Answer for part 1: {}\n".format(
            sum(len(md.get_orbits(obj)) for obj in md.map.__iter__())
        )
    )

    print("Part 2\n------")
    print(
        "Answer for part 2: {}\n".format(
            nx.algorithms.shortest_path_length(
                md.map.to_undirected(),
                source=next(md.map.neighbors("YOU")),
                target=next(md.map.neighbors("SAN")),
            )
        )
    )


if __name__ == "__main__":
    main()
