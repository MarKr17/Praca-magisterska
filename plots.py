import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def create_plots(model):

    agent_wealth = [a.wealth for a in model.schedule.agents]
    # Create a histogram with seaborn
    g = sns.histplot(agent_wealth, discrete=True)
    g.set(title="Wealth distribution", xlabel="Wealth",
          ylabel="Number of agents");
    # The semicolon is just to avoid printing the object representation
    plt.show()
