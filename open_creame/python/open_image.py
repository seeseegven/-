import cv2

# 指定图片文件的路径
image_path = '111.webp'  # 替换为你的图片文件路径

# 使用cv2.imread()函数读取图片
image = cv2.imread(image_path)

# 检查图片是否成功加载
if image is not None:
    # 使用cv2.imshow()函数显示图片
    cv2.imshow('Image', image)
    
    # 等待键盘事件，参数为0表示无限等待直到有键盘输入
    cv2.waitKey(0)
    
    # 关闭所有OpenCV创建的窗口
    cv2.destroyAllWindows()
else:
    print("图片加载失败，请检查路径是否正确")