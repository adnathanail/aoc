def combine_maps(map1, map2):
    combined_map = []
    for start1, end1, value1 in map1:
        s1p = start1 + value1
        e1p = end1 + value1
        for start2, end2, value2 in map2:
            # Case 1
            #    s1|   e1|
            # s2|   e2|
            # Case 2
            # s1|         e1|
            #    s2|   e2|
            # Case 3
            # s1|   e1|
            #    s2|   e2|
            # Case 4
            #    s1|   e1|
            # s2|         e2|
            if (start2 <= s1p and s1p < end2 < e1p) or (s1p < end2 and end2 < e1p) or (s1p <= start2 and start2 < e1p) or (start2 <= s1p and e1p <= end2):
                combined_map.append(
                    [
                        max(s1p, start2) - value1,
                        min(e1p, end2) - value1,
                        value1 + value2,
                    ]
                )
    combined_map.sort(key=lambda x: x[0])  # Sort the combined map by the start of the range
    return combined_map
