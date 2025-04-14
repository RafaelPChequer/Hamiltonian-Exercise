# Implementação do Algoritmo para Caminho Hamiltoniano

## Descrição do Projeto

Este projeto implementa um algoritmo para encontrar um Caminho Hamiltoniano em um grafo, utilizando a linguagem Python. Um Caminho Hamiltoniano é um caminho em um grafo que visita cada vértice exatamente uma vez. O algoritmo utiliza uma abordagem de backtracking para explorar todas as possibilidades de caminhos até encontrar uma solução válida ou determinar que não existe tal caminho.

### Lógica do Algoritmo (Explicação Linha a Linha)

#### main.py
- **`is_valid(v, pos, path, graph)`**:
  - Verifica se o vértice `v` pode ser adicionado na posição `pos` do caminho.
  - Linha `if graph[path[pos-1]][v] == 0`: Confere se existe uma aresta entre o vértice anterior e o vértice atual.
  - Linha `if v in path`: Garante que o vértice não foi visitado anteriormente.
  - Retorna `True` se o vértice é válido, `False` caso contrário.

- **`hamiltonian_util(graph, path, pos)`**:
  - Função recursiva que constrói o caminho hamiltoniano.
  - Linha `if pos == len(graph)`: Caso base, retorna `True` quando todos os vértices foram incluídos.
  - Loop `for v in range(len(graph))`: Tenta cada vértice como próximo no caminho.
  - Linha `path[pos] = -1`: Remove o vértice se ele não leva a uma solução (backtracking).
  - Retorna `True` se um caminho é encontrado, `False` caso contrário.

- **`hamiltonian_path(graph)`**:
  - Inicializa o caminho com `-1` e define o primeiro vértice como 0.
  - Chama `hamiltonian_util` para encontrar o caminho.
  - Retorna o caminho encontrado ou `None` se não houver solução.

- **Bloco principal**:
  - Define um grafo exemplo como matriz de adjacência.
  - Executa o algoritmo e imprime o resultado.

#### view.py (Ponto Extra)
- **`visualize_hamiltonian(graph, path, output_file)`**:
  - Usa NetworkX para criar um grafo e Matplotlib para visualização.
  - Adiciona nós e arestas com base na matriz de adjacência.
  - Desenha o grafo completo com nós em azul claro.
  - Destaca as arestas do caminho hamiltoniano em vermelho.
  - Salva a imagem como PNG na pasta `assets`.

## Como Executar o Projeto

### Pré-requisitos
- Python 3.8+
- Bibliotecas:
  - Para executar apenas `main.py`: Nenhuma biblioteca adicional é necessária.
  - Para executar `view.py`:
    ```bash
    pip install networkx matplotlib
    ```

### Instruções
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/nome_do_repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd nome_do_repositorio
   ```
3. Execute o programa principal:
   ```bash
   python main.py
   ```
4. (Opcional) Para visualizar o grafo:
   ```bash
   python view.py
   ```
   - A imagem será salva em `assets/hamiltonian_path.png`.

## Relatório Técnico

### Análise da Complexidade Computacional

#### Classes P, NP, NP-Completo e NP-Difícil
1. **Classificação do Problema**:
   - O problema do Caminho Hamiltoniano é **NP-Completo**.
   - **Justificativa**:
     - Pertence à classe **NP**: Dado um caminho candidato, é possível verificar em tempo polinomial (O(n)) se ele é um Caminho Hamiltoniano, conferindo se cada vértice é visitado exatamente uma vez e se as arestas existem.
     - É **NP-Completo**: O problema pode ser reduzido a outros problemas NP-Completos, como o Problema do Caixeiro Viajante (TSP). No TSP, busca-se um ciclo hamiltoniano com peso mínimo, enquanto no Caminho Hamiltoniano busca-se apenas a existência de um caminho. A redução do TSP para o Caminho Hamiltoniano pode ser feita em tempo polinomial.
     - Não é **P**, pois não existe um algoritmo conhecido que resolva o problema em tempo polinomial para todos os casos.
     - Não é **NP-Difícil** exclusivamente, pois está em NP (problemas NP-Difíceis podem estar fora de NP).

2. **Relação com o Problema do Caixeiro Viajante**:
   - O TSP é uma generalização do problema do Ciclo Hamiltoniano (que é semelhante ao Caminho Hamiltoniano, mas forma um ciclo).
   - Ambos são NP-Completos, e a existência de um algoritmo polinomial para o Caminho Hamiltoniano implicaria uma solução polinomial para o TSP, o que é improvável a menos que P = NP.

#### Análise da Complexidade Assintótica de Tempo
1. **Complexidade Temporal**:
   - O algoritmo utiliza backtracking, gerando todas as permutações possíveis dos vértices.
   - Para um grafo com `n` vértices, o algoritmo tenta até `(n-1)!` combinações no pior caso (considerando o primeiro vértice fixo).
   - Cada tentativa verifica a validade de um vértice em O(n) (verificar aresta e presença no caminho).
   - Portanto, a complexidade é **O(n!)** no pior caso.

2. **Método de Determinação**:
   - A complexidade foi determinada por **contagem de operações**:
     - O backtracking gera uma árvore de recursão com até `(n-1)!` folhas.
     - Cada nó da árvore realiza verificações em O(n).
     - O custo total é aproximadamente `(n-1)! * n`, que é dominado por O(n!).

#### Aplicação do Teorema Mestre
- O Teorema Mestre não é aplicável diretamente a este algoritmo.
- **Justificativa**:
  - O Teorema Mestre é usado para recorrências da forma `T(n) = aT(n/b) + f(n)`, onde a função é dividida em subproblemas de tamanho reduzido.
  - O algoritmo de backtracking para o Caminho Hamiltoniano não segue esse padrão, pois o número de chamadas recursivas depende do número de vértices válidos em cada etapa, resultando em uma complexidade fatorial, não exponencial ou polinomial divisível.
  - A recursão é mais semelhante a uma busca exaustiva, não a uma divisão balanceada de subproblemas.

#### Análise dos Casos de Complexidade
1. **Diferenças entre Pior Caso, Caso Médio e Melhor Caso**:
   - **Pior Caso (O(n!))**:
     - Ocorre quando o grafo não possui um Caminho Hamiltoniano ou quando a solução está na última permutação explorada.
     - O algoritmo testa quase todas as permutações possíveis.
   - **Caso Médio**:
     - Difícil de determinar precisamente sem suposições sobre a distribuição dos grafos.
     - Em grafos aleatórios densos, a probabilidade de existir um Caminho Hamiltoniano é alta, mas o algoritmo ainda pode explorar muitas permutações antes de encontrá-lo.
     - Estima-se que a complexidade média seja próxima de O(n!), mas com constante menor que no pior caso.
   - **Melhor Caso (O(n))**:
     - Ocorre quando o primeiro caminho testado é uma solução (por exemplo, em um grafo completo onde qualquer permutação é válida).
     - O algoritmo retorna após verificar uma única sequência de vértices.

2. **Impacto no Desempenho**:
   - No **pior caso**, o algoritmo é extremamente lento para grafos grandes (n > 15), tornando-o inviável para aplicações práticas em larga escala.
   - No **caso médio**, o desempenho depende da densidade do grafo. Grafos esparsos podem falhar rapidamente, enquanto grafos densos podem levar mais tempo devido ao maior número de escolhas válidas.
   - No **melhor caso**, o algoritmo é eficiente, mas essa situação é rara em grafos reais.

## Visualização (Ponto Extra)
- O arquivo `view.py` gera uma visualização do grafo com o Caminho Hamiltoniano destacado.
- **Instruções**:
  - Instale as bibliotecas: `pip install networkx matplotlib`.
  - Execute: `python view.py`.
  - A imagem é salva em `assets/hamiltonian_path.png`.
- **Exemplo**:
  ![Caminho Hamiltoniano](assets/hamiltonian_path.png)

## Estrutura do Repositório
- `main.py`: Implementação do algoritmo.
- `view.py`: Visualização do grafo (opcional).
- `assets/`: Pasta com imagens geradas.
- `README.md`: Documentação do projeto.
