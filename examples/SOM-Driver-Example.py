# Driver example file for running SOM
import sys
import os

import pandas

import somutils

# Directory to save outputs to
workspace_dir = os.path.join(
    'C:', os.sep, 'Users', 'username', 'Workspace', 'SOM')
# Make directory if it doesn't exist
if not os.path.isdir(workspace_dir):
    os.mkdir(workspace_dir)

# Path to data
data_path = os.path.join(
    'C:', os.sep, 'Users', 'username', 'Workspace', 'data', 
    'SedRegDataV2g.csv')

# Read data into a Pandas Dataframe
# index_col should be the index (0 starting) of the ID of the table, this 
# is also what will be used when printing the sample ID onto the SOM grid
data_dataframe = pandas.read_csv(data_path, index_col=0)

# List of columns to include as input into SOM
selected_features = ["S", "VC", "VC_rat", "ER", "WtoD", "IR", "d50", 
                     "d84_d16", "nBars", "nFCs", "pArmor", "SSP", "SSP_bal"]

# check that the features wanted match columns in the loaded dataframe
desired_features_set = set(selected_features)
csv_columns_set = set(data_dataframe.columns)
if desired_features_set.issubset(csv_column_set):
    raise ValueError("Some selected features were not found in CSV")

# The number of features for the SOM                     
num_feats = len(selected_features)  

# Get only the data from the features of interest
selected_data_feats_df = data_dataframe.loc[:, selected_features]

# Drop rows with NaN
selected_data_feats_df.dropna(axis=0, inplace=True)

# NORMALIZE DATA by min, max normalization approach
selected_feats_df_norm = somutils.normalize(selected_data_feats_df)

# Display statistics on our normalized data
print(selected_feats_df_norm.describe())

# Initial learning rate for SOM. Will decay to 0.01 linearly
init_learning_rate = 0.05

# The number of rows for the grid and number of columns. This dictates 
# how many nodes the SOM will consist of. Currently not calculated 
# using PCA or other analyses methods.
nrows = 6
ncols = 12
# Create the SOM grid (which initializes the SOM network)
som_grid = somutils.create_grid(nrows, ncols, grid_type='hex')

# Initial neighbourhood radius is defaulted to 2/3 of the longest distance
# Should be set up similar to R package Kohonen
# https://cran.r-project.org/web/packages/kohonen/kohonen.pdf
# Radius will decay to 0.0 linearly
init_radius = somutils.default_radius(som_grid)

# Get the data as a matrix dropping the dataframe wrapper
data = selected_feats_df_norm.values

# Number of iterations to run SOM
niter = 900

# Run SOM
som_weights, object_distances = somutils.run_som(
    data, som_grid, 'hex', niter, init_radius, init_learning_rate)

# It's possible that some data samples were not selected for training, thus do
# do not have a latest bmu
object_distances = somutils.fill_bmu_distances(
    data, som_weights, object_distances)

# Number of clusters to cluster SOM
nclusters = 7
# Cluster SOM nodes
clustering = somutils.cluster_som(som_weights, nclusters)

# Let's save the clusters corresponding to the samples now
results_path = os.path.join(workspace_dir, 'cluster_results.csv')

# To help track clusters to original ID, say ID column of SGAT_PID_P2
data_id = data_dataframe.loc[:, ['SGAT_PID_P2']]
merged_df = pandas.merge(
    selected_data_feats_df, data_id, left_index=True, right_index=True)

somutils.save_cluster_results(
    merged_df, results_path, clustering.labels_, (nrows, ncols), 
    object_distances)

# Display the SOM, coloring the nodes into different clusters from 
# 'clustering' above
# Optional: pass in original dataframe to plot 
# the IDs onto their respective nodes
save_fig_path = os.path.join(workspace_dir, "som_figure.png")
somutils.basic_som_figure(data, som_weights, som_grid, clustering.labels_,
                            'hex', save_fig_path, dframe=data_dataframe)
                            

print("Finished")

