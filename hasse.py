import networkx as nx
from typing import List, Callable, Dict, Any, Set
import matplotlib.pyplot as plt

class Hasse:
    
    def __init__(self, elements: List[Any], relation: Callable[[Any, Any], bool], show_arrows: bool = False):
        self.elements = [frozenset(e) if isinstance(e, set) else e for e in elements]
        self.relation = relation
        self.graph = nx.DiGraph()
        self.show_arrows = show_arrows


    @staticmethod
    def divisibility_relation(x: int, y: int) -> bool:
        return x != y and y % x == 0

    @staticmethod
    def subset_relation(x: Set[Any], y: Set[Any]) -> bool:
        return x != y and x.issubset(y)

    @staticmethod
    def less_equal_relation(x: int, y: int) -> bool:
        return x <= y and x != y

    @staticmethod
    def greater_equal_relation(x: int, y: int) -> bool:
        return x >= y and x != y

    def build_graph(self) -> None:
        self.graph.add_nodes_from(self.elements)

        for a in self.elements:
            for b in self.elements:
                if self.relation(a, b):
                    self.graph.add_edge(a, b)

        self.remove_transitive_edges()

    def remove_transitive_edges(self) -> None:
        edges_to_remove = set()
        
        for u, v in self.graph.edges():
            if any(nx.has_path(self.graph, u, w) and nx.has_path(self.graph, w, v)
                   for w in self.graph.nodes() if w != u and w != v):
                edges_to_remove.add((u, v))

        self.graph.remove_edges_from(edges_to_remove)

    def get_node_levels(self) -> Dict[Any, int]:
        levels = {}
        for node in nx.topological_sort(self.graph):
            predecessors = list(self.graph.predecessors(node))
            levels[node] = 0 if not predecessors else max(levels[p] for p in predecessors) + 1
        return levels

    def draw(self) -> None:
        self.build_graph()
        levels = self.get_node_levels()

        pos = {}
        level_nodes = {}
        
        for node, level in levels.items():
            level_nodes.setdefault(level, []).append(node)

        for level, nodes in level_nodes.items():
            for i, node in enumerate(nodes):
                pos[node] = (i - len(nodes) / 2, level)

        labels = {node: self.format_node_label(node) for node in self.graph.nodes}

        plt.figure(figsize=(10, 6))
        nx.draw(self.graph, pos,
                labels=labels,
                with_labels=True,
                node_color='skyblue',
                node_size=2500,
                font_size=12,
                font_weight='bold',
                arrows=self.show_arrows)
        plt.title("Hasse Diagram")
        plt.show()



    @staticmethod
    def format_node_label(node: Any) -> str:
        if isinstance(node, frozenset):
            return "{" + ", ".join(map(str, sorted(node))) + "}"
        return str(node)
