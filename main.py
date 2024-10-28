import argparse

from tree_generator import TreeGenerator
from tree_visualizer import TreeVisualizer


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate a non-binary tree with specified total nodes and leaf nodes")
    parser.add_argument(
        '--total_nodes',
        type=int,
        default=100,
        help='Total number of nodes in the tree (default: 100)'
    )
    parser.add_argument(
        '--leaf_nodes',
        type=int,
        default=20,
        help='Number of leaf nodes in the tree (default: 20)'
    )
    args = parser.parse_args()
    return args.total_nodes, args.leaf_nodes


# Example usage
if __name__ == "__main__":
    total_nodes, leaf_nodes = parse_arguments()
    print(f"Total Nodes: {total_nodes}, Leaf Nodes: {leaf_nodes}")
    generator = TreeGenerator(total_nodes, leaf_nodes)
    root = generator.create_tree()

    visualizer = TreeVisualizer(root)

    visualizer.draw_tree()  # For 2D visualization
    visualizer.visualize_graph()  # For 3D visualization
