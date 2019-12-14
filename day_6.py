import networkx as nx


class MapData(object):
    def __init__(self, orbits):
        self.orbits = orbits
        self.objects = set()
        self.map = nx.DiGraph()

    def add_orbit(self, orbit):
        primary, secondary = orbit.split(")")
        self.objects.update([primary, secondary])
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
    print(sum(len(md.get_orbits(obj)) for obj in md.objects))


def main():
    print("Part 1\n------")
    with open("inputs/day_6", "r") as f:
        orbits = [orbit.rstrip("\n") for orbit in f.readlines()]
    md = MapData(orbits)
    md.populate()
    print(
        "Answer for part 1: {}\n".format(
            sum(len(md.get_orbits(obj)) for obj in md.objects)
        )
    )

    print("Part 2\n------")
    print("Answer for part 2: {}\n".format(None))


if __name__ == "__main__":
    main()
