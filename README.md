# Tree Generator and Visualizer
This script generates a non-binary tree with a specified number of total nodes and leaf nodes. 
The tree is then visualized in both 2D and 3D formats. The 3D visualization includes interactive checkboxes to select nodes and view their child connections.
## Arguments
- `--total_nodes`: Total number of nodes in the tree (default: 100)
- `--leaf_nodes`: Number of leaf nodes in the tree (default: 20)
## Usage
To run the script, use the following command:
```sh
python main.py --total_nodes <total_nodes> --leaf_nodes <leaf_nodes>
```
For example, to generate a tree with 150 total nodes and 30 leaf nodes:
```sh
python main.py --total_nodes 150 --leaf_nodes 30
```
## Visualization
The script provides two types of visualizations:
1. **2D Visualization**: Displays the tree structure using `matplotlib`.
2. **3D Visualization**: Displays the tree structure in 3D using `plotly`, 
3. with interactive checkboxes to select nodes and view their child connections.
### 2D Visualization Example
![2D Visualization](docs/2d_visualization.png)
### 3D Visualization Example
![3D Visualization](docs/3d_visualization.png)

## Example
```sh
python main.py --total_nodes 100 --leaf_nodes 20
```
## Or run generated executable

This will generate a tree with 100 total nodes and 20 leaf nodes, and visualize it in both 2D and 3D formats.
