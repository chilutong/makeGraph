
import matplotlib.pyplot as plt
import numpy as np

# 生成一些测试数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)


x = [1, 2, 3, 4, 5]
#FPR
fpr_y1 = [0.24, 0.07, 0.09, 0.08,0.05]
fpr_y2 = [0.23, 0.07, 0.05, 0.02, 0.03]
fpr_y3 = [0.35, 0.15, 0.07, 0.05, 0.03]
fpr_y4 = [0.43, 0.17, 0.13, 0.10, 0.03]
fpr_y5 = [0.37, 0.13, 0.04, 0.05, 0]


#Recall
recall_y1 = [0.6821, 0.6245, 0.5886, 0.5565,0.5401]
recall_y2 = [0.6103, 0.4302, 0.3599, 0.3148, 0.3206]
recall_y3 = [0.6690, 0.5644, 0.5335, 0.4936, 0.4912]
recall_y4 = [0.7366, 0.5004, 0.4558, 0.3458, 0.2690]
recall_y5 = [0.7283, 0.4807, 0.3441, 0.2048, 0.0903]


#a
a_y1 = [0.5184, 0.5808, 0.5356, 0.5120,0.5131]
a_y2 = [0.4699, 0.4001, 0.3419, 0.3085, 0.3110]
a_y3 = [0.4349, 0.4797, 0.4980, 0.4689, 0.4765]
a_y4 = [0.4199, 0.4153, 0.3965, 0.3112, 0.2609]
a_y5 = [0.4588, 0.4182, 0.3303, 0.1946, 0.0903]


# a_y1 = [0.3940, 0.5401, 0.4874, 0.4710,0.4874]
# a_y2 = [0.3618, 0.3721, 0.3248, 0.3023, 0.3017]
# a_y3 = [0.2393, 0.3447, 0.3371, 0.2801, 0.2531]
# a_y4 = [0.2891, 0.3638, 0.3171, 0.1848, 0.0903]
# a_y5 = [0.2827, 0.4078, 0.4632, 0.4455, 0.4622]
# 创建一个画布
# plt.figure()
plt.figure(dpi=300,figsize=(6,8))
# 在第一个子区域绘制第一个折线图
plt.subplot(3, 1, 1) # 参数分别表示行数、列数和子区域编号


plt.plot(x, fpr_y1, label='AGNNPIP')
plt.plot(x, fpr_y2, label='DeepTrio')
plt.plot(x, fpr_y3, label='PIPR')
plt.plot(x, fpr_y4, label='DeepFE-PPI')
plt.plot(x, fpr_y5, label='GAT')
# plt.plot(x, y5, label='SymLMF')
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([0,0.1,0.2, 0.3, 0.4,0.5])

plt.xlabel('k',fontsize=14,fontdict={'fontstyle':'italic'})
plt.ylabel('FPR',fontsize=14)
# plt.title('FPR changes with K')

plt.legend(fontsize=9)

# 在第二个子区域绘制第二个折线图
plt.subplot(3, 1, 2)





plt.plot(x, recall_y1, label='AGNNPIP')
plt.plot(x, recall_y2, label='DeepTrio')
plt.plot(x, recall_y3, label='PIPR')
plt.plot(x, recall_y4, label='DeepFE-PPI')
plt.plot(x, recall_y5, label='GAT')

plt.xticks([1, 2, 3, 4, 5])
plt.yticks([0,0.1,0.2, 0.3, 0.4,0.5,0.6,0.7,0.8])
plt.xlabel('k',fontsize=14,fontdict={'fontstyle':'italic'})
plt.ylabel('Recall',fontsize=14)
# plt.title('Recall changes with K')
plt.legend(fontsize=9)


# 在第二个子区域绘制第二个折线图
plt.subplot(3, 1, 3)
plt.plot(x, a_y1, label='AGNNPIP')
plt.plot(x, a_y2, label='DeepTrio')
plt.plot(x, a_y3, label='PIPR')
plt.plot(x, a_y4, label='DeepFE-PPI')
plt.plot(x, a_y5, label='GAT')
# plt.plot(x, y5, label='SymLMF')
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([0,0.1,0.2, 0.3, 0.4,0.5,0.6])

plt.xlabel('k',fontsize=14,fontdict={'fontstyle':'italic'})
plt.ylabel('α',fontsize=14)
plt.legend(fontsize=9)
# 显示图形


plt.tight_layout()
plt.savefig('./Line/test5.tif',bbox_inches='tight')
plt.savefig('./Line/test5.png',bbox_inches='tight')
# plt.show()
