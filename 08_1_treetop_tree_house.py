import numpy as np

with open("./data/input8.txt") as f:
    contents = f.read().splitlines()

forest_list = [[int(tree) for tree in row] for row in contents]
forest = np.array(forest_list)


def tree_visible(forest, i, j):
    tree = forest[i, j]
    if i == 0 or j == 0 or i == forest.shape[0] - 1 or j == forest.shape[1] - 1:
        return True
    elif tree > min(
        max(forest[i, :j]), max(forest[:i, j]), max(forest[i, j + 1 :]), max(forest[i + 1 :, j])
    ):
        return True
    return False


n_visible_trees = 0
for i in range(forest.shape[0]):
    for j in range(forest.shape[1]):
        if tree_visible(forest, i, j):
            n_visible_trees += 1

print(n_visible_trees)
