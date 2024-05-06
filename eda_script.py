import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from mlxtend.frequent_patterns import apriori, association_rules
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from statsmodels.stats.outliers_influence import variance_inflation_factor

class GateEDA:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.scaled_data = None
        self.pca_df = None
        self.tsne_df = None
        self.frequent_itemsets = None
        self.association_rules_df = None
        self.correlation_matrix = None
        self.vif = None

    def data_exploration(self):
        print("Data Shape:", self.data.shape)
        print("Column Names:", self.data.columns)
        print("\nDataset information:")
        print(self.data.info())
        print("\nSummary statistics:")
        print(self.data.describe())

    def data_cleaning(self):
        print("Missing Values:\n", self.data.isnull().sum())
        print("Duplicates:", self.data.duplicated().sum())

    def preprocessing_not(self):
        # Convert to binary for pattern mining
        self.data['Vin'] = self.data['Vin'].astype(int)
        print("\nData types after preprocessing:")
        print(self.data.dtypes)
        
    def preprocessing(self):
        # Convert to binary for pattern mining
        self.data['Vin_A'] = self.data['Vin_A'].astype(int)
        self.data['Vin_B'] = self.data['Vin_B'].astype(int)
        print("\nData types after preprocessing:")
        print(self.data.dtypes)

    def scaling(self):
        scaler = StandardScaler()
        self.scaled_data = scaler.fit_transform(self.data)

    def data_visualization(self):
        # Histograms of preprocessed scaled_data
        plt.figure(figsize=(15, 10))
        for i, column in enumerate(self.data.columns):
            plt.subplot(4, 6, i + 1)
            sns.histplot(self.data[column], kde=True)
            plt.title(column)
        plt.tight_layout()
        plt.show()

    def line_plot(self, x, y, xlabel, ylabel, title):
        plt.figure(figsize=(8, 6))
        plt.plot(self.data[x], self.data[y])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

    def plot_3d(self, x, y, z, xlabel, ylabel, zlabel, title):
        fig = plt.figure(figsize=(15, 15))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.data[x], self.data[y], self.data[z])
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)
        plt.title(title)
        plt.show()

    def pca_analysis(self):
        pca = PCA(n_components=3)
        X_pca = pca.fit_transform(self.scaled_data)
        self.pca_df = pd.DataFrame(data=X_pca, columns=[f'PCA_{i+1}' for i in range(X_pca.shape[1])])
        print("Explained Variance Ratio:")
        print(pca.explained_variance_ratio_)

    def plot_pca(self):
        # 3d scatter plot
        fig = plt.figure(figsize=(15, 15))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.pca_df['PCA_1'], self.pca_df['PCA_2'], self.pca_df['PCA_3'])
        ax.set_xlabel('PCA_1')
        ax.set_ylabel('PCA_2')
        ax.set_zlabel('PCA_3')
        plt.title("PCA Analysis")
        plt.show()

    def plot_pca_3d(self):
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        scatter = ax.scatter(self.pca_df['PCA_1'], self.pca_df['PCA_2'], self.pca_df['PCA_3'], c=self.data['leakage'], cmap='viridis')
        plt.colorbar(scatter, label='Leakage')
        ax.set_xlabel('PCA Component 1')
        ax.set_ylabel('PCA Component 2')
        ax.set_zlabel('PCA Component 3')
        plt.title('PCA 3D Scatter Plot (Leakage)')
        plt.show()

    def plot_pca_3d_not(self):
        fig = plt.figure(figsize=(12, 8))
        ax1 = fig.add_subplot(111, projection='3d')
        scatter1 = ax1.scatter(self.pca_df['PCA_1'], self.pca_df['PCA_2'], self.pca_df['PCA_3'], c=self.data['delay_LH_NodeA'], cmap='viridis')
        plt.colorbar(scatter1, ax=ax1, label='Delay LH NodeA')
        ax1.set_title('PCA 3D Scatter Plot (delay_LH_NodeA)')
        ax1.set_xlabel('PCA Component 1')
        ax1.set_ylabel('PCA Component 2')
        ax1.set_zlabel('PCA Component 3')

    def plot_pca_3d_2(self):
        fig = plt.figure(figsize=(12, 8))

        # Subplot 1
        ax1 = fig.add_subplot(121, projection='3d')
        scatter1 = ax1.scatter(self.pca_df['PCA_1'], self.pca_df['PCA_2'], self.pca_df['PCA_3'], c=self.data['delay_LH_NodeA'], cmap='viridis')
        plt.colorbar(scatter1, ax=ax1, label='Delay LH NodeA')
        ax1.set_title('PCA 3D Scatter Plot (delay_LH_NodeA)')
        ax1.set_xlabel('PCA Component 1')
        ax1.set_ylabel('PCA Component 2')
        ax1.set_zlabel('PCA Component 3')

        # Subplot 2
        ax2 = fig.add_subplot(122, projection='3d')
        scatter2 = ax2.scatter(self.pca_df['PCA_1'], self.pca_df['PCA_2'], self.pca_df['PCA_3'], c=self.data['delay_LH_NodeB'], cmap='viridis')
        plt.colorbar(scatter2, ax=ax2, label='Delay LH NodeB')
        ax2.set_title('PCA 3D Scatter Plot (delay_LH_NodeB)')
        ax2.set_xlabel('PCA Component 1')
        ax2.set_ylabel('PCA Component 2')
        ax2.set_zlabel('PCA Component 3')
        plt.tight_layout()
        plt.show()

    def pca_corr(self):
        scaled_data_df = pd.DataFrame(self.scaled_data, columns=self.data.columns)
        pca_corr = pd.concat([self.pca_df, scaled_data_df], axis=1).corr()
        plt.figure(figsize=(16, 12))
        sns.heatmap(pca_corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("PCA Correlation Matrix")
        plt.show()


    def most_correlated(self):
        most_correlated_pca1 = self.pca_df.corr()['PCA_1'].abs().sort_values(ascending=False).head(5)
        most_correlated_pca2 = self.pca_df.corr()['PCA_2'].abs().sort_values(ascending=False).head(5)
        most_correlated_pca3 = self.pca_df.corr()['PCA_3'].abs().sort_values(ascending=False).head(5)
        print("Most Correlated with PCA_1:")
        print(most_correlated_pca1)
        print("\nMost Correlated with PCA_2:")
        print(most_correlated_pca2)
        print("\nMost Correlated with PCA_3:")
        print(most_correlated_pca3)


    def tsne_analysis(self):
        tsne = TSNE(n_components=3, perplexity=30, random_state=42)
        tsne_result = tsne.fit_transform(self.scaled_data)
        self.tsne_df = pd.DataFrame(data=tsne_result, columns=['tsne_1', 'tsne_2', 'tsne_3'])

    def pattern_mining_not(self):
        binary_df = self.data[['Vin']]
        self.frequent_itemsets = apriori(binary_df, min_support=0.1, use_colnames=True)
        self.association_rules_df = association_rules(self.frequent_itemsets, metric="confidence", min_threshold=0.7)
        # plot
        plt.figure(figsize=(10, 6))
        plt.barh(range(len(self.frequent_itemsets)), self.frequent_itemsets['support'], tick_label=self.frequent_itemsets['itemsets'])
        plt.xlabel('Support')
        plt.ylabel('Itemsets')
        plt.title('Frequent Itemsets')
        plt.show()

    def pattern_mining(self):
        binary_df = self.data[['Vin_A', 'Vin_B']]
        self.frequent_itemsets = apriori(binary_df, min_support=0.1, use_colnames=True)
        self.association_rules_df = association_rules(self.frequent_itemsets, metric="confidence", min_threshold=0.7)
        # plot
        plt.figure(figsize=(10, 6))
        plt.barh(range(len(self.frequent_itemsets)), self.frequent_itemsets['support'], tick_label=self.frequent_itemsets['itemsets'])
        plt.xlabel('Support')
        plt.ylabel('Itemsets')
        plt.title('Frequent Itemsets')
        plt.show()

    def regression_analysis_not(self):
        scaled_data_df = pd.DataFrame(self.scaled_data, columns=self.data.columns)
        X = scaled_data_df.drop(columns=['leakage', 'delay_LH_NodeA', 'delay_HL_NodeA'])
        y = scaled_data_df[['leakage', 'delay_LH_NodeA', 'delay_HL_NodeA']]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        y_pred = regressor.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print("Mean Squared Error:", mse)

    def regression_analysis(self):
        scaled_data_df = pd.DataFrame(self.scaled_data, columns=self.data.columns)
        X = scaled_data_df.drop(columns=['leakage', 'delay_LH_NodeA', 'delay_HL_NodeA', 'delay_LH_NodeB', 'delay_HL_NodeB'])
        y = scaled_data_df[['leakage', 'delay_LH_NodeA', 'delay_HL_NodeA', 'delay_LH_NodeB', 'delay_HL_NodeB']]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        y_pred = regressor.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print("Mean Squared Error:", mse)


    # def interpretability_analysis(self):
    #     rf_model = RandomForestRegressor(n_estimators=100, random_state=0)
    #     rf_model.fit(X_train, y_train)
    #     explainer = shap.Explainer(rf_model)
    #     shap_values = explainer.shap_values(X_train)
    #     shap.summary_plot(shap_values, X_train)

    def correlation_analysis(self):
        scaled_data_df = pd.DataFrame(self.scaled_data, columns=self.data.columns)
        self.correlation_matrix = scaled_data_df.corr()
        plt.figure(figsize=(16, 12))
        sns.heatmap(self.correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Matrix")
        plt.show()


    def vif_analysis(self):
        numerical_features = pd.DataFrame(self.scaled_data, columns=self.data.columns).select_dtypes(include=[np.number])
        vif_data = pd.DataFrame()
        vif_data["feature"] = numerical_features.columns
        vif_data["VIF"] = [variance_inflation_factor(numerical_features.values, i) for i in range(len(numerical_features.columns))]
        self.vif = vif_data
        print("VIF Scores:")
        print(vif_data)



# usage
# gate_eda = GateEDA("data.csv")
# gate_eda.data_exploration()
# gate_eda.data_cleaning()
# gate_eda.preprocessing()
# gate_eda.scaling()
# gate_eda.data_visualization()
# gate_eda.line_plot('Vin_A', 'Vin_B', 'Vin_A', 'Vin_B', 'Vin_A vs Vin_B')
# gate_eda.plot_3d('Vin_A', 'Vin_B', 'temp', 'Vin_A', 'Vin_B', 'Temperature', '3D Scatter Plot')
# gate_eda.pca_analysis()
# gate_eda.plot_pca()
# gate_eda.plot_pca_3d()
# gate_eda.plot_pca_3d_2()
# gate_eda.tsne_analysis()
# gate_eda.pattern_mining()
# gate_eda.regression_analysis()
# gate_eda.correlation_analysis()
# gate_eda.vif_analysis()

