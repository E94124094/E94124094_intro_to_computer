import cv2

# 讀取原始照片
original_image = cv2.imread("TW.jpg")

# 使用函式灰階照片
gray_image_with_function = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# 不使用函式灰階照片
gray_image_without_function = (original_image[:, :, 0] + original_image[:, :, 1] + original_image[:, :, 2]) // 3

# 二值化照片
_, binary_image = cv2.threshold(gray_image_with_function, 246, 255, cv2.THRESH_BINARY)

# 顯示原始照片
cv2.imshow("Original Image", original_image)

# 顯示使用函式灰階照片
cv2.imshow("Gray Image with Function", gray_image_with_function)

# 顯示不使用函式灰階照片
cv2.imshow("Gray Image without Function", gray_image_without_function)

# 顯示二值化照片
cv2.imshow("Binary Image", binary_image)

# 等待使用者按下任意鍵，然後關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()