import os
import seaborn as sns
import matplotlib.pyplot as plt

from Visualisation.Gradients import (b_gradient, t_gradient, myelin_gradient,
                                     neuron_gradient)
from Visualisation.Constants import virus_color


class Plots():
    def __init__(self, datacollector):
        self.datacollector = datacollector
        self.data = self.datacollector.get_model_vars_dataframe()
        self.Plots = {}
        self.folder = "test"
        self.folder_path = os.path.join(os.getcwd(), "test")

    def Plot(self):
        colors = [t_gradient[len(t_gradient)-1],
                  b_gradient[len(b_gradient)-1],
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

    def Plot_realtime(self):
        colors = [t_gradient[len(t_gradient)-1],
                  b_gradient[len(b_gradient)-1],
                  neuron_gradient[len(neuron_gradient)-1],
                  myelin_gradient[len(myelin_gradient)-1],
                  virus_color]
        i = 0
        for key in self.data:
            plot = sns.lineplot(data=self.data[key], color=colors[i], label=key)
            i += 1
        plot.set(title=key, ylabel="Number of agents", xlabel="Step")
        

