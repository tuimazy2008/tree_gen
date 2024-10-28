import matplotlib.pyplot as plt
import networkx as nx
import plotly.graph_objects as go
import random

from tree_generator import TreeNode


class TreeVisualizer:
    def __init__(self, root):
        self.root = root
        self.G = self.build_graph(root)

    @staticmethod
    def build_graph(root: TreeNode):
        tree_graph = nx.DiGraph()

        def add_edges(node):
            for child in node.children:
                tree_graph.add_edge(node.value, child.value)
                add_edges(child)

        add_edges(root)
        return tree_graph

    def draw_tree(self):
        pos = nx.spring_layout(self.G)
        plt.figure(figsize=(12, 8))
        nx.draw(self.G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold",
                arrows=False)
        plt.title("Tree Structure")
        plt.show()

    def randomize_3d_positions(self):
        return {node: (random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)) for node in self.G.nodes()}

    def create_visualization_data(self, pos):
        data = []
        node_x, node_y, node_z, node_text = [], [], [], []
        for node in self.G.nodes():
            x, y, z = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_z.append(z)
            node_text.append(f'Node {node}')

        node_trace = go.Scatter3d(
            x=node_x, y=node_y, z=node_z,
            mode='markers+text',
            marker=dict(size=5, color='skyblue', opacity=0.8),
            text=node_text,
            textposition="top center",
            hoverinfo='text',
            name="Nodes"
        )
        data.append(node_trace)

        for node in self.G.nodes():
            edge_x, edge_y, edge_z = [], [], []
            for neighbor in self.G.neighbors(node):
                x0, y0, z0 = pos[node]
                x1, y1, z1 = pos[neighbor]
                edge_x += [x0, x1, None]
                edge_y += [y0, y1, None]
                edge_z += [z0, z1, None]

            edge_trace = go.Scatter3d(
                x=edge_x, y=edge_y, z=edge_z,
                line=dict(width=2, color='gray'),
                mode='lines',
                hoverinfo='none',
                visible=True,
                name=f"Children of Node {node}"
            )
            data.append(edge_trace)
        return data

    def get_update_menus(self, data):
        update_menus = [
            {
                "type": "buttons",
                "direction": "right",
                "buttons": [
                    {
                        "label": "Check All",
                        "method": "update",
                        "args": [{"visible": [True] * len(data)}, {"title": "All Connections Visible"}]
                    },
                    {
                        "label": "Uncheck All",
                        "method": "update",
                        "args": [{"visible": [True] + [False] * (len(data) - 1)}, {"title": "No Connections Visible"}]
                    }
                ],
                "showactive": True,
                "x": 0.1,
                "xanchor": "left",
                "y": 1.15,
                "yanchor": "top"
            },
            {
                "buttons": [
                    {
                        "label": f"Node {node}",
                        "method": "update",
                        "args": [
                            {"visible": [True] + [i == idx for i in range(1, len(data))]},
                            {"title": f"3D Graph - Connections of Node {node}"}
                        ],
                        "args2": [
                            {"visible": [True] + [False] * (len(data) - 1)},
                            {"title": "No Connections Visible"}
                        ]
                    }
                    for idx, node in enumerate(self.G.nodes(), start=1)
                ],
                "direction": "down",
                "showactive": True,
                "x": 0.1,
                "xanchor": "left",
                "y": 1.05,
                "yanchor": "top",
                "type": "dropdown",
            }
        ]
        return update_menus

    def visualize_graph(self):
        pos = self.randomize_3d_positions()
        data = self.create_visualization_data(pos)
        fig = go.Figure(data=data)
        fig.update_layout(
            title="Select nodes to show child elements",
            showlegend=False,
            updatemenus=self.get_update_menus(data),
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
            ),
        )
        fig.show()
