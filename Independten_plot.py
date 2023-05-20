import numpy as np
import matplotlib.pyplot as plt
plt.figure(dpi=300,figsize=(2.5,2))
ATT_LSTM = [0.9960,0.9966]
MATT_CNN = [0.7988,0.8103]
ATT_RLSTM = [0.7755,0.7949]
CNN_RLSTM = [0.6824,0.7043]
#x = ['REST','LAPT','AUTO']
x = np.arange(2) #总共有几组，就设置成几，我们这里有三组，所以设置为3
# x = np.array([0,0.5])
total_width, n = 0.6, 4    # 有多少个类型，只需更改n即可，比如这里我们对比了四个，那么就把n设成4
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x, ATT_LSTM, color = "#E47271",width=width,label='AGNN ')
plt.bar(x + width, MATT_CNN, color = "#497CB3",width=width,label='DeepTrio')
plt.bar(x + 2 * width, ATT_RLSTM , color = "#61C480",width=width,label='PIPR')
plt.bar(x + 3 * width, CNN_RLSTM , color = "#FC9303",width=width,label='DeepFE-PPI')
# a=0.25
# b=0.25
# plt.bar(np.array([-0.15+a,0.85-b]), ATT_LSTM, color = "#E47271",width=width,label='AGNN ')
# plt.bar(np.array([-0.15+a,0.85-b]) + width, MATT_CNN, color = "#497CB3",width=width,label='DeepTrio')
# plt.bar(np.array([-0.15+a,0.85-b])+ 2 * width, ATT_RLSTM , color = "#61C480",width=width,label='PIPR')
# plt.bar(np.array([-0.15+a,0.85-b]) + 3 * width, CNN_RLSTM , color = "#FC9303",width=width,label='DeepFE-PPI')
print(x)
# plt.xlabel("dataset")
# plt.ylabel("accuracy")
# plt.legend(loc='upper right',frameon=False)

# plt.legend(bbox_to_anchor=(1.01, 1),prop=legend_font,frameon=False)
plt.xticks([0.0,1.0],['AUROC','AP'],fontsize=9)
# plt.xticks([0.3625,0.8125],['AUROC','AP'],fontsize=8)
my_y_ticks = np.arange(0, 1.2, 0.2)
# plt.ylim((0.8, 0.95))
plt.yticks(my_y_ticks,fontsize=8)
# fig.subplots_adjust(right=0.8)
# plt.show()
plt.title('Virus-human PPI dataset',fontsize=8)
plt.savefig('independent.tif')