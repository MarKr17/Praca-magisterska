import os
import seaborn as sns
import matplotlib.pyplot as plt

from Visualisation.Gradients import (myelin_gradient,
                                     neuron_gradient)
from Visualisation.Constants import (virus_color, B_cells_color,
                                     t_naive_cell_color, Plasma_color,
                                     Tpato17_color, Th_color,
                                     Th0_color, Treg17_color,
                                     Th1_color, Th2_color,
                                     APC_color)


class Plots():
    def __init__(self, datacollector, folder):
        self.datacollector = datacollector
        self.data = self.datacollector.get_model_vars_dataframe()
        self.Plots = {}
        self.folder = folder
        self.folder_path = os.path.join(os.getcwd(), "test")
        self.Cells_dict = {"B_cells": {"B-cell population": B_cells_color,
                                       "Plasma cell population": Plasma_color},
                           "T_cells": {"T-cell population": t_naive_cell_color,
                                       "Tpato17 population": Tpato17_color,
                                       "Treg17 population": Treg17_color},
                           "Th_cells": {"Th-cell population": Th_color,
                                        "Th0 population": Th0_color,
                                        "Th1 population": Th1_color,
                                        "Th2 population": Th2_color},
                           "Misc_cells": {"APC population": APC_color,
                                          "Virus population": virus_color}}
        self.Cytokines = ["Cytokine levels", "IFN levels", "TGF levels",
                          "IL-2 levels", "IL-4 levels", "IL-6 levels",
                          "IL-17 levels", "IL-21 levels", "IL-22 levels"]
        self.Proteins = ["MBP levels", "EBNA1 levels", "MBP antibody levels",
                         "EBNA1 antibody levels"]

        self.Demyelination = {"Neuron population": neuron_gradient[9],
                              "Myelin health": myelin_gradient[9]}

    def Plot(self):
        colors = [t_naive_cell_color,
                  B_cells_color,
                  neuron_gradient[len(neuron_gradient)-1],
                  myelin_gradient[len(myelin_gradient)-1],
                  virus_color]
        i = 0
        for key in self.data:
            plot = sns.lineplot(data=self.data[key], color=colors[i])
            plot.set(title=key, ylabel="Number of agents", xlabel="Step")
            filename = key + ".jpg"
            filepath = os.path.join(self.folder_path, filename)
            plt.savefig(filepath, dpi=300)
            plt.clf()
            i += 1

    def Plot_demyelination(self):
        for key in self.Demyelination.keys():
            plot = sns.lineplot(data=self.data[key],
                                color=self.Demyelination[key],
                                label=key)
        plot.set(title="Demyelination",
                 ylabel="Neuron number and Myelin helath", xlabel="Step")
        filepath = os.path.join(self.folder_path, "Demyelination.jpg")
        plt.savefig(filepath, dpi=300)
        plt.clf()

    def Plot_cells_by_category(self, cells_category):
        cells = self.Cells_dict[cells_category]
        for key in cells.keys():
            plot = sns.lineplot(data=self.data[key], color=cells[key],
                                label=key)
        plot.set(title=cells_category,
                 ylabel="Number of agents", xlabel="Step")
        filepath = os.path.join(self.folder_path, cells_category + ".jpg")
        plt.savefig(filepath, dpi=300)
        plt.clf()

    def Plot_cytokine_levels(self):
        for cytokine in self.Cytokines:
            plot = sns.lineplot(data=self.data[cytokine],
                                label=cytokine)
        plot.set(title="Cytokine levels",
                 ylabel="Amount", xlabel="Step")
        filepath = os.path.join(self.folder_path, "Cytokine levels.jpg")
        plt.savefig(filepath, dpi=300)
        plt.clf()

    def Plot_protein_levels(self):
        for protein in self.Proteins:
            plot = sns.lineplot(data=self.data[protein],
                                label=protein)
        plot.set(title="Protein levels",
                 ylabel="Amount", xlabel="Step")
        filepath = os.path.join(self.folder_path, "Protein levels.jpg")
        plt.savefig(filepath, dpi=300)
        plt.clf()

    def Plot_one(self, name):
        plot = sns.lineplot(data=self.data[name],
                            label=name)
        plot.set(title=name,
                 ylabel="Amount", xlabel="Step")
        filepath = os.path.join(self.folder_path, name + ".jpg")
        plt.savefig(filepath, dpi=300)
        plt.clf()

    def Plot_multiple(self, list):
        for name in list:
            plot = sns.lineplot(data=self.data[name],
                                label=name)
        plot.set(title=','.join(str(x) for x in list),
                 ylabel="Amount", xlabel="Step")
        filepath = os.path.join(self.folder_path,
                                ','.join(str(x) for x in list)+".jpg")
        plt.savefig(filepath, dpi=300)
        plt.clf()
