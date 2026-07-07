"""
Visualization Utilities
"""

import matplotlib.pyplot as plt
import seaborn as sns

from config import CHART_DIR

sns.set_theme(style="whitegrid", palette="viridis")

plt.rcParams.update({

    "figure.figsize": (12,6),

    "axes.titlesize":18,

    "axes.labelsize":14,

    "xtick.labelsize":11,

    "ytick.labelsize":11

})


def save_chart(filename):

    plt.tight_layout()

    plt.savefig(

        CHART_DIR / f"{filename}.png",

        dpi=300,

        bbox_inches="tight"

    )

    plt.show()