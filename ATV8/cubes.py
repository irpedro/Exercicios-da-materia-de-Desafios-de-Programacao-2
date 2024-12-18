def solve():
    import sys

    case_number = 1

    while True:

        N = int(input().strip())
        if N == 0:
            break
        
        cubes = []
        for i in range(N):
            cubes.append(list(map(int, input().strip().split())))

        dp = [[(0, -1, -1)] * 6 for _ in range(N)]

        opposite_face = {
            0: 1,
            1: 0,
            2: 3,
            3: 2,
            4: 5,
            5: 4
        }

        for i in range(N):
            for top_face in range(6): 
                for j in range(i): 
                    for bottom_face in range(6):
                        if cubes[j][bottom_face] == cubes[i][opposite_face[top_face]]:
                            if dp[j][bottom_face][0] + 1 > dp[i][top_face][0]:
                                dp[i][top_face] = (dp[j][bottom_face][0] + 1, j, bottom_face)

        max_height = 0
        last_cube = -1
        last_face = -1
        for i in range(N):
            for face in range(6):
                if dp[i][face][0] > max_height:
                    max_height = dp[i][face][0]
                    last_cube = i
                    last_face = face

        sequence = []
        while last_cube != -1:
            sequence.append((last_cube + 1, last_face)) 
            last_cube, last_face = dp[last_cube][last_face][1], dp[last_cube][last_face][2]

        print(f"Case #{case_number}")
        print(max_height + 1)
        for cube_index, top_face in reversed(sequence):
            faces = ["front", "back", "left", "right", "top", "bottom"]
            print(cube_index, faces[top_face])
        print()

        case_number += 1

solve()
