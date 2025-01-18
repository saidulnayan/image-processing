import cv2
image=cv2.imread("img.jpg")   # task 1 (get image)
print(image.shape)   # task 2 (resolution)

y,x,z= image.shape
x=int((x*29)/100)       # task 3 (resize x-axis)
y=int((y*16)/100)       # task 4 (resize y-axis)
image=cv2.resize(image,(x,y))

cv2.imshow("Icon",image)    # task 5 (show resized image)
cv2.waitKey()
cv2.destroyAllWindows()

print(image.shape)
MB= (x*y*3)/(1024*1024)     # task 6 (calculate MB)
print("{0:.2f} MB".format(MB))

image=cv2.rotate(image,cv2.ROTATE_180)      # task 7 (rotate 180 deg)
cv2.imshow("Icon",image)
cv2.waitKey()
cv2.destroyAllWindows()


