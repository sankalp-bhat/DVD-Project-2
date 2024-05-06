from eda_script import GateEDA
import matplotlib.pyplot as plt

class GateComparison:
    def __init__(self, gate_objects):
        self.gate_objects = gate_objects

    def scaling(self):
        for gate in self.gate_objects:
            gate.scaling()

    def compare_gates_visualization(self, gates, visualization_type):
        for i, gate_info in enumerate(gates):
            gate_name = gate_info['gate']
            print(f"Visualization for gate: {gate_name}")
            
            if visualization_type == 'pca':
                self.gate_objects[i].pca_analysis()
                self.gate_objects[i].plot_pca()

            elif visualization_type == 'pca_leakage':
                self.gate_objects[i].plot_pca_3d()

            elif visualization_type == 'pca_delay':
                if gate_name == 'NOT':
                    self.gate_objects[i].plot_pca_3d_not()
                else:
                    self.gate_objects[i].plot_pca_3d_2()

            elif visualization_type == 'correlation':
                self.gate_objects[i].correlation_analysis()

            elif visualization_type == '2d_plot_delay':
                self.gate_objects[i].scatter_plot('cqload', 'delay_LH_NodeA', 'CQload','Delay', '2D plot: Delay vs CQload')
            
            elif visualization_type == '2d_plot_leakage':
                self.gate_objects[i].scatter_plot('toxe_p', 'leakage', 'Oxide Thickness', 'Leakage', '2D plot: Leakage vs Tox')
            
            elif visualization_type == '3d_plot':
                self.gate_objects[i].plot_3d('delay_LH_NodeA', 'temp', 'cqload', 'Delay', 'Temperature', 'CQload', '3D Plot: Delay vs Temperature vs CQload')

        plt.tight_layout()
        plt.show()
