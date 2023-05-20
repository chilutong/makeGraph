import matplotlib.pyplot as plt
import numpy as np

plt.figure(dpi=300,figsize=(5,3))
# 五组数据
data = [[0.3891, 0.1353, 0.2349],
        [0.4848, 0.2791, 0.3555],
        [0.6880, 0.5257, 0.540],
        [0.5029, 0.3183, 0.3450],
        [0.4580, 0.2008, 0.5378]]

# 每组数据的颜色
colors = ['r', 'g', 'b', 'c', 'm']
colors = ['#E47271', '#497CB3', '#61C480', '#CF7CB0', '#FC9303']
# 每组数据的标签
# labels = ['局部采样', '相似度采样', '锚点式随机采样', '锚点式局部采样', '锚点式相似度采样']
labels = ['local', 'similar', 'Anchor(k=2)', 'local(k=2)', 'similar(k=2)']

# 每组数据的位置
x = np.arange(3)

# 每组数据的宽度
width = 0.1

# 画图
for i in range(5):
    plt.bar(x + i * width, data[i], width, color=colors[i], label=labels[i])

# 设置x轴标签
plt.xticks(x + width * 2, ['AGNNPIP', 'DeepFE-PPI', 'GAT'])

# 设置图例
# plt.legend()

# 显示图像
# plt.show()
plt.savefig('sampleCompare.tif',bbox_inches='tight')
plt.savefig('sampleCompare.png',bbox_inches='tight')