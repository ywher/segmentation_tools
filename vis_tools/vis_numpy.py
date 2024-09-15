import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def visualize_arrays(confidence_arr, entropy_arr):
    # 创建子图和画布
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

    # 可视化预测置信度数组
    im1 = ax1.imshow(confidence_arr, cmap='viridis')
    ax1.set_title('Confidence')
    ax1.set_xlabel('Width')
    ax1.set_ylabel('Height')
    ax1.axis('off')
    # fig.colorbar(im1, ax=ax1, shrink=1.0)
    divider1 = make_axes_locatable(ax1)
    cax1 = divider1.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im1, cax=cax1)

    # 可视化预测熵值数组
    im2 = ax2.imshow(entropy_arr, cmap='viridis') #'hot
    ax2.set_title('Entropy')
    ax2.set_xlabel('Width')
    ax2.set_ylabel('Height')
    ax2.axis('off')
    divider2 = make_axes_locatable(ax2)
    cax2 = divider2.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im2, cax=cax2)
    # fig.colorbar(im2, ax=ax2, shrink=1.0)  # shrink=1.0表示颜色条的长度和图像一样长

    # 保存图像
    plt.savefig('visualization.png', dpi=300, bbox_inches='tight')

    # 显示图像
    plt.show()
    
    # 关闭图像
    plt.close()

# 示例输入数据
confidence = np.random.rand(10, 10)
entropy = np.random.rand(10, 10)

# 进行可视化并保存图像
visualize_arrays(confidence, entropy)
