import numpy as np

def day8(input_str: str, num_connections: int) -> tuple[int, int]:
    """
    input_str: a list of 3d coordinates. Repeatedly connect the <num_connections> closest pairs. 
    Then multiply the size of the disconnected graph components (i.e ignore all singletons).
    
    kd tree?
    """
    arr = np.asarray([line.split(',') for line in input_str.split('\n')], dtype=int)
    dest = np.sqrt(((arr[:, np.newaxis] - arr) ** 2).sum(axis=-1))
    i, j = np.triu_indices(len(dest), k=1)
    upper_dists = dest[i, j]
    order = np.argsort(upper_dists)
    row_idx, col_idx = i[order], j[order]

    # now we have a list of edges. build the components.
    components = []
    part_1_components = []
    for i, (source, dest) in enumerate(zip(row_idx, col_idx)):
        source_comp = None
        dest_comp = None
        for component in components:
            if source in component:
                source_comp = component
            if dest in component:
                dest_comp = component
        
        if source_comp is None and dest_comp is None:
            components.append({source, dest})
        elif source_comp is dest_comp:
            source_comp.add(source)
            source_comp.add(dest)
        elif source_comp is None:
            dest_comp.add(source)
        elif dest_comp is None:
            source_comp.add(dest)
        else:  # both in different components — merge them
            source_comp.update(dest_comp)
            components.remove(dest_comp)

        if i == num_connections - 1:
            part_1_components = [x.copy() for x in components]
        
        # part 2 - return the last two junction boxes you need to connect to complete the circuit.
        if len(components) == 1 and len(components[0]) == len(arr):
            part_2 = (source, dest)
            break


    running_prod = 1
    comp_sizes = sorted((len(c) for c in part_1_components), reverse=True)[:3]
    for c in comp_sizes:
        running_prod *= c
    
    return running_prod, int(arr[source, 0] * arr[dest, 0])



if __name__ == "__main__":

    test_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

    assert day8(test_input, 10) == (40,25272)
    with open('inputs/day08.txt') as flines:
        input_str = flines.read()

    print("day 8: ", day8(input_str, 1000))

