# Table of contents
## Background
I was advised by Dr. Junyuan Lin to work on the sequntial optimization of the 1/2 approximation path cover algorithm, and the project was used to compute the primary algorithm and optimized algorithm on Watts-Strogatz graph and Erdos-Renyi graph with different nodes number. The project is written in python, and the main data structure is dictionary due to its low time complexity to sort. The paper has been published on arxiv https://arxiv.org/pdf/2101.08947.pdf
## Install
To install NumPy: https://numpy.org/install/

To install line-profiler: https://pypi.org/project/line-profiler/#description

To install networkx: https://networkx.org/documentation/stable/install.html
## Usage
optimization_and_primary_algorithm.py is the formal project which produces computational time of both algorithms and results

tester.ipynb is a quick tester on a Watts-Strogatz graph with 128 nodes and 4 degree of nodes. At the end, it produces the path outcome which includes edges and their weights.

Note: The dictionary path_list contains the path cover, edges, and weights. Print path_list if you want to see results. All computational time results are included in the paper.
## Maintainer
@George-the-Ren
## Contributors
@George-the-Ren

Dr. Junyuan Lin
