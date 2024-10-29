import argparse
import logging
import os

from tree_generator import TreeGenerator
from tree_visualizer import TreeVisualizer


__author__ = "Timur Galimov"
__mail__ = "tuimazy2@gmail.com"
__tool__ = "Tree Generator"
__version__ = "0.1"


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate a non-binary tree with specified total nodes and leaf nodes")
    parser.add_argument(
        '--total_nodes',
        type=int,
        default=8,
        help='Total number of nodes in the tree (default: 100)'
    )
    parser.add_argument(
        '--leaf_nodes',
        type=int,
        default=3,
        help='Number of leaf nodes in the tree (default: 20)'
    )
    args = parser.parse_args()
    return args.total_nodes, args.leaf_nodes


def logger_init(output_log_path='log_file.log'):
    verbose_format = '%(asctime)s.%(msecs)03d %(levelname)5s %(lineno)4d %(module)20s: %(message)s'
    if folder := os.path.dirname(output_log_path):
        os.makedirs(folder, exist_ok=True)

    logging.basicConfig(filename=output_log_path,
                        filemode='a',
                        format=verbose_format,
                        datefmt='%d-%H:%M:%S',
                        level=logging.DEBUG)

    # Create a console handler with the same format
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(verbose_format)
    console_handler.setFormatter(console_formatter)
    logging.getLogger('').addHandler(console_handler)


# Example usage
if __name__ == "__main__":
    total_nodes, leaf_nodes = parse_arguments()
    logger_init()
    logging.info(f"Total Nodes: {total_nodes}, Leaf Nodes: {leaf_nodes}")
    generator = TreeGenerator(total_nodes, leaf_nodes)
    root = generator.create_tree()

    visualizer = TreeVisualizer(root)

    visualizer.draw_tree()  # For 2D visualization
    visualizer.visualize_graph()  # For 3D visualization
