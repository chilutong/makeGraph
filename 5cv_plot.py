import numpy as np
import pandas as pd
import os

dataset = 'Oryza'
root_path = "./mean_std_plot/"+ dataset +"/"

AGNN_path = root_path + "AGNN.csv"
DeepFE_path = root_path + "DeepFE.csv"
DeepTrio_path = root_path + "DeepTrio.csv"
GCN_path = root_path + "GAT.csv"
SymLMF_path = root_path + "SymLMF.csv"

AGNN = pd.read_csv(AGNN_path,index_col=[0])
DeepFE = pd.read_csv(DeepFE_path,index_col = [0])
DeepTrio = pd.read_csv(DeepTrio_path,index_col = [0])
GCN = pd.read_csv(GCN_path,index_col = [0])
SymLMF = pd.read_csv(SymLMF_path,index_col = [0])


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
config = {'ecolor' : '#808080', 'capsize' : 2.5, 'capthick' : 0.5, 'elinewidth' : 1 }


# AGNN 
AGNN_mean = np.array(AGNN.loc['mean'])
AGNN_err = np.array(AGNN.loc['std'])
plt.bar(x, AGNN_mean,  width=width, label='AGNN',color='#E47271',yerr=AGNN_err,error_kw=config)

# DeepTrio
DeepTrio_mean = np.array(DeepTrio.loc['mean'])
DeepTrio_err = np.array(DeepTrio.loc['std'])
plt.bar(x + width, DeepTrio_mean, width=width, label='Salp',color='#497CB3',yerr=DeepTrio_err,error_kw=config)

# DeepFE
DeepFE_mean = np.array(DeepFE.loc['mean'])
DeepFE_err = np.array(DeepFE.loc['std'])
plt.bar(x + 2 * width, DeepFE_mean, width=width, label='Squirrel',color='#61C480',yerr=DeepFE_err,error_kw=config)



# SymLMF
SymLMF_mean = np.array(SymLMF.loc['mean'])
SymLMF_err = np.array(SymLMF.loc['std'])
plt.bar(x + 3 * width, SymLMF_mean, width=width, label='GA',color='#CF7CB0',yerr=SymLMF_err,error_kw=config)
# GCN
GCN_mean = np.array(GCN.loc['mean'])
GCN_err = np.array(GCN.loc['std'])
plt.bar(x + 4 * width, GCN_mean, width=width, label='ABC',color='#FC9303',yerr=GCN_err,error_kw=config)


plt.ylim((0.5,1.05))
# plt.yticks(np.arange(0.8,1.01,0.05))
# plt.ylabel('Fitness')
# plt.xlabel('Dataset')

plt.xticks(range(7),['Accuracy','Precision','Recall','F1-score','Mcc','AUROC','AP'],fontsize=9)
plt.yticks(np.arange(0.5, 1.01, 0.1), fontsize=11)
plt.title(dataset,fontsize=11)
plt.savefig('./bar/'+dataset+'.tif',bbox_inches='tight')
plt.savefig('./bar/'+dataset+'.png',bbox_inches='tight')

# plt.savefig('./barSwarm/barFitness.png',bbox_inches = 'tight')