from PIL import Image
import re
import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
from tkinter import *
from tkinter import filedialog



if __name__ == "__main__":
    if len(sys.argv)> 1:
        filepath = sys.argv[1]
    else:
        filepath = filedialog.askopenfilename(initialdir="C:\\Users\\jandy")
    pass #end if
image = cv2.imread(filepath)
#plt.subplot(1,2,1)
#plt.title("original")
#plt.imshow(image)


rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
#sharpened_image = cv2.filter2D(rgb,-1,kernel)

plt.subplot(1,1,1)                # was 1,2,1
plt.title("rgb")
plt.imshow(rgb)
plt.show()

#print('Inspect a few pixels in the original image:')
#for y in np.arange(3):
#    for x in np.arange(3):
#        print(x, y, image.getpixel((x, y)))

# Modified for RGB images from: https://stackoverflow.com/a/60783743/11089932
img_np = np.array(rgb)
xy_coords = np.flip(np.column_stack(np.where(np.all(img_np >= 0, axis=2))), axis=1)
rgb = np.reshape(img_np, (np.prod(img_np.shape[:2]), 3))

# Add pixel numbers in front
pixel_numbers = np.expand_dims(np.arange(1, xy_coords.shape[0] + 1), axis=1)
value = np.hstack([pixel_numbers, xy_coords, rgb])
print('\nCompare pixels in result:')
for y in np.arange(3):
    for x in np.arange(3):
        print(value[(value[:, 1] == x) & (value[:, 2] == y)])

# Properly save as CSV
newfilepath = re.sub('\.\w*','.csv',filepath)
print (newfilepath)
np.savetxt(newfilepath, value, delimiter=',', fmt='%4d')



