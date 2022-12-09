import numpy as np

with open("./data/input8.txt") as f:
    contents = f.read().splitlines()

forest_list = [[int(tree) for tree in row] for row in contents]
forest = np.array(forest_list)


def scenic_score(forest, i, j):
    tree = forest[i, j]
    n_rows, n_cols = forest.shape

    if i == 0 or j == 0 or i == n_rows - 1 or j == n_cols - 1:
        return 0

    v_dist_right = np.amin(np.argwhere(forest[i, j + 1 :] >= tree) + 1, initial=n_cols - j - 1)
    v_dist_bottom = np.amin(np.argwhere(forest[i + 1 :, j] >= tree) + 1, initial=n_rows - i - 1)
    v_dist_left = np.amin(np.argwhere(np.flip(forest[i, :j]) >= tree) + 1, initial=j)
    v_dist_top = np.amin(np.argwhere(np.flip(forest[:i, j]) >= tree) + 1, initial=i)

    return v_dist_right * v_dist_bottom * v_dist_left * v_dist_top


best_scenic_score = 0
for i in range(forest.shape[0]):
    for j in range(forest.shape[1]):
        if (candidate_score := scenic_score(forest, i, j)) > best_scenic_score:
            best_scenic_score = candidate_score

print(best_scenic_score)
