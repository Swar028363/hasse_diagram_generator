from hasse import Hasse

if __name__ == "__main__":
    # Test 1: Divisibility Relation
    print("Divisibility Relation:")
    elements = [1, 2, 3, 4, 6, 8, 12, 24]
    hasse_div = Hasse(elements, Hasse.divisibility_relation)
    hasse_div.draw()

    # Test 2: Subset Relation
    print("Subset Relation:")
    elements = [{1}, {1, 2}, {1, 2, 3}, {2}, {2, 3}]
    hasse_sub = Hasse(elements, Hasse.subset_relation)
    hasse_sub.draw()

    # Test 3: Less Than or Equal Relation
    print("Less Than or Equal Relation:")
    elements = [1, 2, 3, 4, 5]
    hasse_leq = Hasse(elements, Hasse.less_equal_relation)
    hasse_leq.draw()

    # Test 4: Greater Than or Equal Relation
    print("Greater Than or Equal Relation:")
    elements = [1, 2, 3, 4, 5]
    hasse_geq = Hasse(elements, Hasse.greater_equal_relation)
    hasse_geq.draw()
