from collections import defaultdict
import numpy as np

def find_scc(n, graph):
    """Encontra Componentes Fortemente Conexas (SCCs) usando o algoritmo de Tarjan."""
    index = 0
    stack = []
    indices = [-1] * n
    lowlink = [-1] * n
    on_stack = [False] * n
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for v in range(n):
        if indices[v] == -1:
            strongconnect(v)

    return sccs

def solve(input_data):
    """Resolve o problema dado o input como uma lista de strings."""
    data = input_data
    case = 0
    i = 0

    while i < len(data):
        n = int(data[i])
        if n == 0:
            break

        case += 1
        i += 1
        graph = defaultdict(list)

        # Lendo as arestas
        while True:
            start, end = map(int, data[i].split())
            if start == 0 and end == 0:
                break
            graph[start - 1].append(end - 1)
            i += 1

        # Consultas
        i += 1
        q = int(data[i])
        queries = []
        for _ in range(q):
            i += 1
            queries.append(int(data[i]) - 1)
        i += 1

        # Encontrar SCCs
        sccs = find_scc(n, graph)
        infinite_nodes = set()
        
        for scc in sccs:
            if len(scc) > 1 or any(w in scc for v in scc for w in graph[v]):
                infinite_nodes.update(scc)

        # Criar a matriz de transição
        P = np.zeros((n, n))
        for u in range(n):
            if graph[u]:
                prob = 1 / len(graph[u])
                for v in graph[u]:
                    P[u][v] = prob

        # Resolver para estados finitos
        finite_nodes = [i for i in range(n) if i not in infinite_nodes]
        F = None
        if finite_nodes:
            Q = P[np.ix_(finite_nodes, finite_nodes)]
            I = np.eye(len(Q))
            try:
                F = np.linalg.inv(I - Q)
            except np.linalg.LinAlgError:
                F = None

        # Calcular os valores esperados
        expectations = [0] * n
        if F is not None:
            for idx, node in enumerate(finite_nodes):
                expectations[node] = F[0, idx]

        # Imprimir resultados
        print(f"Case #{case}:")
        for query in queries:
            if query in infinite_nodes:
                print("infinity")
            else:
                print(f"{expectations[query]:.3f}")

def main():
    """Função principal para executar o programa."""
    # Exemplo de entrada:
    input_data = [
        "3",
        "1 2",
        "2 3",
        "2 1",
        "0 0",
        "3",
        "1",
        "2",
        "3",
        "3",
        "1 2",
        "2 3",
        "3 1",
        "0 0",
        "3",
        "3",
        "2",
        "1",
        "0"
    ]
    solve(input_data)

if __name__ == "__main__":
    main()
