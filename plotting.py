import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

output_filename = "fletchvbt.png"

table_for_analysis = pd.read_excel("CLEAR_corpus_final.xlsx")

figure, axis = plt.subplots(1, figsize = (16, 5))

axis.scatter(table_for_analysis["BT_easiness"].astype(float), table_for_analysis["Flesch-Reading-Ease"].astype(float))

axis.set_ylabel("BT Easiness", fontsize = 12)
axis.set_xlabel("Flesch-Reading-Ease", fontsize = 12)
plt.title("Flesch-Reading-Ease vs BT Easiness")
plt.tight_layout(pad = 1)
figure.savefig(output_filename, dpi = 300)
