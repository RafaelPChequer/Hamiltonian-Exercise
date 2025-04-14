import networkx as nx
import matplotlib.pyplot as plt


def visualize_hamiltonian(graph, path, output_file="hamiltonian_path.png"):
    G = nx.Graph()
    n = len(graph)

    # Adiciona nós
    for i in range(n):
        G.add_node(i)

    # Adiciona arestas
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)

    # Desenha o grafo completo
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=500, font_size=12)

    # Destaca o caminho hamiltoniano
    if path:
        hamiltonian_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=hamiltonian_edges,
                               edge_color='red', width=2)

    plt.savefig(output_file)
    plt.close()


if __name__ == "__main__":
    # Exemplo
    graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ]
    from main import hamiltonian_path

    path = hamiltonian_path(graph)
    visualize_hamiltonian(graph, path)