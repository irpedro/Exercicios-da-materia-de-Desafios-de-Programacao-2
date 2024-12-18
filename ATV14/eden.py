MAX = 35
STATES = 8

def dfs(n, curr, id, N, state, visited, first):
    if n == N - 1:
        return ((curr >> 1) & 1) == ((first >> 2) & 1) and (curr & 1) == ((first >> 1) & 1)

    visited[n][curr] = True
    for i in range(STATES):
        if ((id >> i) & 1) == int(state[n + 1]) and ((curr >> 1) & 1) == ((i >> 2) & 1) and (curr & 1) == ((i >> 1) & 1):
            if n < N - 1 and not visited[n + 1][i] and dfs(n + 1, i, id, N, state, visited, first):
                return True
    return False

def main():
    while True:
        # Read inputs
        line = input()
        if line.lower() == 'exit':
            break
        
        # Parse input line
        parts = line.split()
        id = int(parts[0])
        N = int(parts[1])
        state = parts[2]
        
        found = False
        visited = [[False] * STATES for _ in range(N)]
        first = 0

        # Try each possible initial state configuration
        for i in range(STATES):
            if ((id >> i) & 1) == int(state[0]):
                first = i
                for j in range(N):
                    for k in range(STATES):
                        visited[j][k] = False
                if dfs(0, i, id, N, state, visited, first):
                    found = True
                    break

        print("REACHABLE" if found else "GARDEN OF EDEN")

if __name__ == "__main__":
    main()
