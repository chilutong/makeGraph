# 导入所需的库
import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子
np.random.seed(0)

# 生成10次运行的结果，每次都有fpr和tpr
# 假设每次有100个点
fprs = []
tprs = []
for i in range(10):
    fpr = np.sort(np.random.rand(100)) # 随机生成fpr，并排序
    tpr = np.sort(np.random.rand(100)) # 随机生成tpr，并排序
    fprs.append(fpr)
    tprs.append(tpr)

# 计算每个点的平均值和标准差
mean_fpr = np.mean(fprs, axis=0)
mean_tpr = np.mean(tprs, axis=0)
std_fpr = np.std(fprs, axis=0)
std_tpr = np.std(tprs, axis=0)

# 绘制平均ROC曲线，并用plt.fill_between函数来填充误差范围
plt.plot(mean_fpr, mean_tpr, label='Mean ROC')
plt.fill_between(mean_fpr, mean_tpr - std_tpr,
                 mean_tpr + std_tpr,
                 alpha=0.2,
                 label='Error range')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.legend()
plt.show()