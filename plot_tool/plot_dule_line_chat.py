import matplotlib.pyplot as plt

# 数据
ratio_values = [0.005, 0.008, 0.01, 0.02, 0.03, 0.05]
str_ratio_values = [str(i) for i in ratio_values]
training_mIoU = [70.25, 70.48, 70.47, 70.44, 70.50, 70.42]
validation_mIoU = [69.74, 69.39, 70.43, 70.12, 70.09, 69.91]
x = [i+1 for i in range(len(training_mIoU))]
text1_x_shift = [0, 0, 0, 0, 0, 0]
text1_y_shift = [0, 0, 0, 0, 0, 0]
text2_x_shift = [0, 0, 0, 0, 0, 0]
text2_y_shift = [0, 0, 0, 0, 0, 0]

# 绘制折线图
plt.figure(figsize=(10, 4))

# 绘制训练集mIoU折线
plt.plot(x, training_mIoU, marker='o', label='Training mIoU', color='blue')

# 绘制验证集mIoU折线
plt.plot(x, validation_mIoU, marker='s', label='Validation mIoU', color='green')

# 添加数据标签
for i in range(len(ratio_values)):
    plt.text(x[i] + text1_x_shift[i], training_mIoU[i] + text1_y_shift[i], f'{training_mIoU[i]:.2f}', ha='center', va='bottom', fontsize=12)
    plt.text(x[i] + text2_x_shift[i], validation_mIoU[i] + text2_y_shift[i], f'{validation_mIoU[i]:.2f}', ha='center', va='top', fontsize=12)

# 设置x轴刻度
plt.xticks(x, str_ratio_values)
plt.xlabel('area ratio threshold', fontsize=14)
plt.ylabel('mIoU', fontsize=14)

# 添加图例
# plt.legend(loc='lower right', fontsize=12)
plt.legend(fontsize=12)

# 显示图像
# plt.title('Training and Validation mIoU Over Different Ratios', fontsize=16)
plt.grid(True)
plt.tight_layout()
plt.savefig('dule_line_chat.pdf', bbox_inches='tight')
# plt.show()
