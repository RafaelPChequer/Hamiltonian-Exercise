# Implementação do Algoritmo para Caminho Hamiltoniano
def is_valid(v, pos, path, graph):
    # Verifica se o vértice v pode ser adicionado na posição pos
    if graph[path[pos - 1]][v] == 0:  # Verifica se há aresta
        return False
    if v in path:  # Verifica se o vértice já foi visitado
        return False
    return True


def hamiltonian_util(graph, path, pos):
    # Caso base: se todos os vértices foram incluídos
    if pos == len(graph):
        return True

    # Tenta diferentes vértices como próximo
    for v in range(len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_util(graph, path, pos + 1):
                return True
            path[pos] = -1  # Remove vértice se não leva à solução

    return False


def hamiltonian_path(graph):
    n = len(graph)
    path = [-1] * n
    path[0] = 0  # Começa do vértice 0

    if not hamiltonian_util(graph, path, 1):
        return None
    return path


# Exemplo de uso
if __name__ == "__main__":
    # Grafo representado como matriz de adjacência
    graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ]

    result = hamiltonian_path(graph)
    if result:
        print("Caminho Hamiltoniano encontrado:", result)
    else:
        print("Não existe Caminho Hamiltoniano")
        