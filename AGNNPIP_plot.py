import numpy as np
import pandas as pd
import os

indicators = 'Specificity'
root_path = "./Performance2/"+ indicators +"/"

Both_path = root_path + "AGNN.csv"
sequence_path = root_path + "sequence.csv"
network_path = root_path + "network.csv"


Both = pd.read_csv(Both_path,index_col=[0],encoding='gbk')
sequence = pd.read_csv(sequence_path,index_col = [0],encoding='gbk')
network = pd.read_csv(network_path,index_col = [0],encoding='gbk')



import matplotlib.pyplot as plt


# plot
plt.figure(dpi=300,figsize=(5,3))

plt.rc('font',family='Times New Roman')

size = 6
x = np.arange(size)  # 0 1 2 3 4 5

total_width, n = 0.6, 3
width = total_width / n
x = x - (total_width - width) / 2

# 误差棒配置
config = {'ecolor' : '#808080', 'capsize' : 2.5, 'capthick' : 0.5, 'elinewidth' : 1 }


# AGNN
Both_mean = np.array(Both.loc['mean'])
Both_err = np.array(Both.loc['std'])
plt.bar(x, Both_mean,  width=width, label='AGNN',color='#E47271')

# DeepTrio
sequence_mean = np.array(sequence.loc['mean'])
sequence_err = np.array(sequence.loc['std'])
plt.bar(x + width, sequence_mean, width=width, label='Salp',color='#497CB3')

# DeepFE
network_mean = np.array(network.loc['mean'])
DeepFE_err = np.array(network.loc['std'])
plt.bar(x + 2 * width, network_mean, width=width, label='Squirrel',color='#61C480')






plt.ylim((0.5,1.05))
# plt.yticks(np.arange(0.8,1.01,0.05))
# plt.ylabel('Fitness')
# plt.xlabel('Dataset')

plt.xticks(range(6),['S.cere','C.elegan','E.coli','Drosophila','HPRD','Oryza'],fontsize=9)
plt.yticks(np.arange(0, 1.01, 0.2), fontsize=11)
plt.title(indicators,fontsize=11)
plt.savefig('./indicators_bar2/'+indicators+'.tif',bbox_inches='tight')
plt.savefig('./indicators_bar2/'+indicators+'.png',bbox_inches='tight')

# plt.show()

# plt.savefig('./barSwarm/barFitness.png',bbox_inches = 'tight')