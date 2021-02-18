def countTriplets(arr, r):
    if len(arr) <= 2:
        return 0
    map_arr = {}
    map_doubles = {}
    count = 0
    # Traversing the array from rear, helps avoid division
    for x in arr[::-1]:
        r_x = r * x
        r_r_x = r * r_x

        # case: x is the first element (x, x*r, x*r*r)
        count += map_doubles.get((r_x, r_r_x), 0)

        # case: x is the second element (x/r, x, x*r)
        map_doubles[(x, r_x)] = map_doubles.get((x, r_x), 0) + map_arr.get(r_x, 0)

        # case: x is the third element (x/(r*r), x/r, x)
        map_arr[x] = map_arr.get(x, 0) + 1

    return count


arr = [1, 3, 9, 9, 27, 81]
countTriplets(arr,3)