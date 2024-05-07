# analysis_module.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from mpl_toolkits.mplot3d import Axes3D

def runEDA(file_path):
    data = load_data(file_path)
    # Preprocess the data
    scaled_data = preprocess_data(data)
    # Visualize histograms
    visualize_histograms(data)
    # Visualize scatter plots with regression
    visualize_scatter_regression(data)
    visualize_3d_plots(data)
    pca_df = visualize_3d_scatter_pca(scaled_data)
    # Perform PCA and elbow method
    pca_df, optimal_clusters = perform_elbow_method(pca_df)
    # Perform K-means clustering
    clustered_data = perform_kmeans_clustering(pca_df, optimal_clusters)
    # Visualize clustered data in 3D
    visualize_clustered_data_3d(clustered_data)
    # Correlation matrix
    correlation_matrix(data)
    
def load_data(file_path):
    """
    Load the data from a CSV file and return a DataFrame.
    """
    data = pd.read_csv(file_path)
    # print("\nDataset information:")
    # data.info()
    # print("\nSummary statistics:")
    # print(data.describe())
    return data

def preprocess_data(data):
    """
    Preprocess the data by standardizing it using StandardScaler.
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    scaled_data = pd.DataFrame(scaled_data, columns=data.columns)
    return scaled_data

def visualize_histograms(data):
    """
    Visualize histograms of preprocessed scaled data.
    """
    plt.figure(figsize=(15, 10))
    for i, column in enumerate(data.columns):
        plt.subplot(4, 6, i + 1)
        sns.histplot(data[column], kde=True)
        plt.title(column)
    plt.tight_layout()
    plt.show()

def visualize_scatter_regression(data):
    """
    Visualize scatter plots with regression lines for specific relationships.
    """
    # Set up the subplot grid
    fig, axs = plt.subplots(3, 2, figsize=(16, 12))

    # Scatter plot and regression line for leakage vs toxe_p
    sns.scatterplot(data=data, x='toxe_p', y='leakage', alpha=0.5, ax=axs[0, 0], color='green')
    sns.regplot(data=data, x='toxe_p', y='leakage', scatter=False, color='red', ax=axs[0, 0])
    axs[0, 0].set_title('Leakage vs Toxe_P')
    axs[0, 0].set_xlabel('Toxe_P')
    axs[0, 0].set_ylabel('Leakage')

    # Scatter plot and regression line for leakage vs toxe_n
    sns.scatterplot(data=data, x='toxe_n', y='leakage', alpha=0.5, ax=axs[0, 1], color='green')
    sns.regplot(data=data, x='toxe_n', y='leakage', scatter=False, color='red', ax=axs[0, 1])
    axs[0, 1].set_title('Leakage vs Toxe_N')
    axs[0, 1].set_xlabel('Toxe_N')
    axs[0, 1].set_ylabel('Leakage')

     # Scatter plot and regression line for leakage vs wmin
    sns.scatterplot(data=data, x='wmin', y='leakage', alpha=0.5, ax=axs[1, 0], color='pink')
    sns.regplot(data=data, x='wmin', y='leakage', scatter=False, color='red', ax=axs[1, 0])
    axs[1, 0].set_title('Leakage vs wmin')
    axs[1, 0].set_xlabel('wmin')
    axs[1, 0].set_ylabel('Leakage')

    # Scatter plot and regression line for leakage vs lmin
    sns.scatterplot(data=data, x='lmin', y='leakage', alpha=0.5, ax=axs[1, 1], color='pink')
    sns.regplot(data=data, x='lmin', y='leakage', scatter=False, color='red', ax=axs[1, 1])
    axs[1, 1].set_title('Leakage vs lmin')
    axs[1, 1].set_xlabel('lmin')
    axs[1, 1].set_ylabel('Leakage')

    # Scatter plot and regression line for delay vs temp
    
    sns.scatterplot(data=data, x='temp', y='leakage', alpha=0.5, ax=axs[2, 0], color = 'blue')
    sns.regplot(data=data, x='temp', y='leakage', scatter=False, color='red', ax=axs[2, 0])
    axs[2, 0].set_title('leakage vs Temp')
    axs[2, 0].set_xlabel('Temperature')
    axs[2, 0].set_ylabel('leakage')

    # Scatter plot and regression line for delay vs cqload
    if 'delay_LH_NodeB' in data.columns:
        sns.scatterplot(data=data, x='cqload', y='delay_LH_NodeB', alpha=0.5, ax=axs[2, 1], color = 'purple')
        sns.regplot(data=data, x='cqload', y='delay_LH_NodeB', scatter=False, color='red', ax=axs[2, 1])
        axs[2, 1].set_title('Delay vs Cqload')
        axs[2, 1].set_xlabel('Cqload')
        axs[2, 1].set_ylabel('Delay_LH_NodeB')

    plt.tight_layout()
    plt.show()

def visualize_3d_plots(scaled_data):
    # Create a figure and set of 3D axes
    fig = plt.figure(figsize=(18, 12))

    # leakage vs vdd vs temp
    ax1 = fig.add_subplot(321, projection='3d')
    ax1.scatter(scaled_data['leakage'], scaled_data['pvdd'], scaled_data['temp'], c='green')
    ax1.set_xlabel('Leakage')
    ax1.set_ylabel('vdd')
    ax1.set_zlabel('Temperature')
    ax1.set_title('Leakage vs vdd vs Temperature')

    # leakage vs lmin vs wmin
    ax2 = fig.add_subplot(322, projection='3d')
    ax2.scatter(scaled_data['leakage'], scaled_data['lmin'], scaled_data['wmin'], c='green')
    ax2.set_xlabel('Leakage')
    ax2.set_ylabel('Lmin')
    ax2.set_zlabel('wmin')
    ax2.set_title('Leakage vs L vs W')

    if 'delay_LH_NodeB' in scaled_data.columns:
        # delay vs temp vs W/L
        ax3 = fig.add_subplot(323, projection='3d')
        ax3.scatter(scaled_data['delay_LH_NodeB'], scaled_data['temp'], scaled_data['wmin']/scaled_data['lmin'], c='purple')
        ax3.set_xlabel('Delays')
        ax3.set_ylabel('Temperature')
        ax3.set_zlabel('W/L')
        ax3.set_title('Delays vs Temperature vs W/L')

        # delay vs temp vs cqload
        ax4 = fig.add_subplot(324, projection='3d')
        ax4.scatter(scaled_data['delay_HL_NodeB'], scaled_data['temp'], scaled_data['cqload'], c='purple')
        ax4.set_xlabel('Delays')
        ax4.set_ylabel('Temperature')
        ax4.set_zlabel('CQ Load')
        ax4.set_title('Delays vs Temperature vs CQ Load')

        # delay vs lmin vs wmin
        ax5 = fig.add_subplot(325, projection='3d')
        ax5.scatter(scaled_data['delay_LH_NodeB'], scaled_data['lmin'], scaled_data['wmin'], c='purple')
        ax5.set_xlabel('Delay')
        ax5.set_ylabel('Lmin')
        ax5.set_zlabel('wmin')
        ax5.set_title('Delay vs L vs W')

    # leakage vs temp vs W/L
    ax6 = fig.add_subplot(326, projection='3d')
    ax6.scatter(scaled_data['leakage'], scaled_data['temp'], scaled_data['wmin']/scaled_data['lmin'], c='green')
    ax6.set_xlabel('leakage')
    ax6.set_ylabel('Temperature')
    ax6.set_zlabel(' W/L')
    ax6.set_title('leakage vs Temperature vs  W/L')

    # Adjust layout
    plt.tight_layout()

    # Show the plots
    plt.show()

def visualize_3d_scatter_pca(scaled_data):
    """
    Visualize a 3D scatter plot using PCA results.
    """
    pca = PCA(n_components=3)
    X_pca = pca.fit_transform(scaled_data)
    pca_df = pd.DataFrame(data=X_pca, columns=[f'PCA_{i+1}' for i in range(X_pca.shape[1])])
     # Print explained variance ratio
    print("Explained Variance Ratio:")
    print(pca.explained_variance_ratio_)
    # Create a 3D scatter plot
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(pca_df['PCA_1'], pca_df['PCA_1'], pca_df['PCA_3'], c=scaled_data['temp'], cmap='viridis')
    ax.set_title('PCA 3D Scatter Plot')
    ax.set_xlabel('PCA Component 1')
    ax.set_ylabel('PCA Component 2')
    ax.set_zlabel('PCA Component 3')
    plt.colorbar(scatter, label='Temperature')
    plt.show()

    # Calculate the correlation matrix between PCA components and original features
    pca_original_corr = pd.concat([pca_df, scaled_data], axis=1).corr()
    # Find the columns with the highest absolute correlation with each PCA component
    most_correlated_pca1 = pca_original_corr['PCA_1'].abs().sort_values(ascending=False).head(5)
    most_correlated_pca2 = pca_original_corr['PCA_2'].abs().sort_values(ascending=False).head(5)
    most_correlated_pca3 = pca_original_corr['PCA_3'].abs().sort_values(ascending=False).head(5)

    print("Most correlated columns with PCA Component 1:")
    print(most_correlated_pca1)
    print("\nMost correlated columns with PCA Component 2:")
    print(most_correlated_pca2)
    print("\nMost correlated columns with PCA Component 3:")
    print(most_correlated_pca3)
    return pca_df

def perform_elbow_method(pca_df):
    """
    Perform the elbow method to determine the optimal number of clusters.
    """
    visualizer = KElbowVisualizer(KMeans(random_state=42), k=(2, 10))
    visualizer.fit(pca_df)
    visualizer.show()

    optimal_clusters = visualizer.elbow_value_
    return pca_df, optimal_clusters

def perform_kmeans_clustering(pca_df, optimal_clusters):
    """
    Perform K-means clustering with the optimal number of clusters.
    """
    kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(pca_df)
    pca_df['Cluster'] = cluster_labels
    return pca_df

def visualize_clustered_data_3d(pca_df):
    """
    Visualize the clustered data in 3D.
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    for cluster in range(pca_df['Cluster'].nunique()):
        cluster_data = pca_df[pca_df['Cluster'] == cluster]
        ax.scatter(cluster_data['PCA_1'], cluster_data['PCA_2'], cluster_data['PCA_3'], label=f'Cluster {cluster+1}')

    ax.set_title(f'K-means Clustering with PCA ({pca_df["Cluster"].nunique()} Clusters)')
    ax.set_xlabel('PCA Component 1')
    ax.set_ylabel('PCA Component 2')
    ax.set_zlabel('PCA Component 3')
    plt.legend()
    plt.show()

def correlation_matrix(scaled_data):
    # Correlation analysis
    correlation_matrix = scaled_data.corr()
    plt.figure(figsize=(16, 12))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

