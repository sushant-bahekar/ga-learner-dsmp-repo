import numpy as np
# Adjacency matrix
adj_mat = np.array([[0,0,0,0,0,0,1/3,0],
                   [1/2,0,1/2,1/3,0,0,0,0],
                   [1/2,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0],
                  [0,0,1/2,1/3,0,0,1/3,0],
                   [0,0,0,1/3,1/3,0,0,1/2],
                   [0,0,0,0,1/3,0,0,1/2],
                   [0,0,0,0,1/3,1,1/3,0]])

# Compute eigenvalues and eigencevectrs
eigenvalues, eigenvectors =np.linalg.eig(adj_mat)

# Eigen vector corresponding to 1
eigen_1 = abs(eigenvectors[:,0]) / np.linalg.norm(eigenvectors[:,0],1)

print(eigen_1)
# most important page

page = np.where(np.max(eigen_1) == eigen_1) [0][0]+1
print(page)

# Initialize stationary vector I
init_I = np.array([1,0,0,0,0,0,0,0])
# Perform iterations for power method
for _ in range(10):
    init_I = np.dot(adj_mat, init_I)
    init_I /= np.linalg.norm(init_I, 1)
print(init_I)
power_page = np.where(np.max(init_I) == init_I)[0][0]+1
print(power_page)

# New Adjancency matrix
new_adj_mat = np.array([[0,0,0,0,0,0,0,0],
                   [1/2,0,1/2,1/3,0,0,0,0],
                  [1/2,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0],
                   [0,0,1/2,1/3,0,0,1/2,0],
                   [0,0,0,1/3,1/3,0,0,1/2],
                   [0,0,0,0,1/3,0,0,1/2],
                   [0,0,0,0,1/3,1,1/2,0]])

# Initialize stationary vector I
new_init_I = np.array([1,0,0,0,0,0,0,0])

# Perform iterations for power method
for _ in range(10):
    new_init_I = np.dot(new_adj_mat, new_init_I)
    new_init_I /= np.linalg.norm(new_init_I, 1)
print(new_init_I)
print('='*20)
# Alpha value
alpha = 0.85
# Code starts here
G = (alpha + new_adj_mat) + (1-alpha) * (1/len (new_adj_mat))*np.ones(new_adj_mat.shape)
print(G)
final_init_I = np.array([1,0,0,0,0,0,0,0])
# Perform iterations for power method
for _ in range(1000):
    final_init_I = np.dot(G, final_init_I)
    final_init_I /= np.linalg.norm(final_init_I, 1)
print(final_init_I)
print('='*20)
# Code ends here


