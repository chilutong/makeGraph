import numpy as np
import pandas as pd
import os

dataset = 'Oryza'
root_path = "./mean_std_plot2/"+ dataset +"/"

AGNN_path = root_path + "AGNN.csv"
DeepFE_path = root_path + "DeepFE.csv"
DeepTrio_path = root_path + "DeepTrio.csv"
GAT_path = root_path + "GAT.csv"
PIPR_path = root_path + "PIPR.csv"
# SymLMF_path = root_path + "SymLMF.csv"

AGNN = pd.read_csv(AGNN_path,index_col=[0])
DeepFE = pd.read_csv(DeepFE_path,index_col = [0])
DeepTrio = pd.read_csv(DeepTrio_path,index_col = [0])
GAT = pd.read_csv(GAT_path,index_col = [0])
PIPR = pd.read_csv(PIPR_path,index_col = [0])
# SymLMF = pd.read_csv(SymLMF_path,index_col = [0])


import matplotlib.pyplot as plt


# plot
plt.figure(dpi=300,figsize=(6,3))

plt.rc('font',family='Times New Roman')

size = 7
x = np.arange(size)  # 0 1 2 3 4 5

total_width, n = 0.8, 5
width = total_width / n
x = x - (total_width - width) / 2

# 误差棒配置
# config = {'ecolor' : '#808080', 'capsize' : 2.5, 'capthick' : 0.5, 'elinewidth' : 1 }


# AGNN
AGNN_mean = np.array(AGNN.loc['mean'])
AGNN_err = np.array(AGNN.loc['std'])
plt.bar(x, AGNN_mean,  width=width, label='AGNN',color='#E47271')

# DeepTrio
DeepTrio_mean = np.array(DeepTrio.loc['mean'])
DeepTrio_err = np.array(DeepTrio.loc['std'])
plt.bar(x + width, DeepTrio_mean, width=width, label='Salp',color='#497CB3')

# DeepFE
DeepFE_mean = np.array(DeepFE.loc['mean'])
DeepFE_err = np.array(DeepFE.loc['std'])
plt.bar(x + 3 * width, DeepFE_mean, width=width, label='Squirrel',color='#CF7CB0')



# SymLMF
# SymLMF_mean = np.array(SymLMF.loc['mean'])
# SymLMF_err = np.array(SymLMF.loc['std'])
# plt.bar(x + 3 * width, SymLMF_mean, width=width, label='GA',color='#CF7CB0')
#PIPR
PIPR_mean = np.array(PIPR.loc['mean'])
PIPR_err = np.array(PIPR.loc['std'])
plt.bar(x + 2 * width, PIPR_mean, width=width, label='GA',color='#61C480')
# GCN
GAT_mean = np.array(GAT.loc['mean'])
GAT_err = np.array(GAT.loc['std'])
plt.bar(x + 4 * width, GAT_mean, width=width, label='ABC',color='#FC9303')


plt.ylim((0,1.05))
# plt.yticks(np.arange(0.8,1.01,0.05))
# plt.ylabel('Fitness')
# plt.xlabel('Dataset')

plt.xticks(range(7),['Accuracy','Precision','Recall','F1-score','Mcc','AUROC','AP'],fontsize=9)
plt.yticks(np.arange(0, 1.01, 0.2), fontsize=11)
plt.title(dataset,fontsize=11)
plt.savefig('./bar2/'+dataset+'.tif',bbox_inches='tight')
plt.savefig('./bar2/'+dataset+'.png',bbox_inches='tight')

# plt.savefig('./barSwarm/barFitness.png',bbox_inches = 'tight')