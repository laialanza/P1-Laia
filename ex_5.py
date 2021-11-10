from scipy.fftpack import dct, idct
#Need to install scipy in terminal: pip install scipy

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

#Need to install scikit-image in terminal: pip install scikit-image
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt

# read lena RGB image and convert to grayscale
directory = input("Introduce the directory of your image:  \n")
im = rgb2gray(imread(directory))
imF = dct2(im)
im1 = idct2(imF)

# plot original and reconstructed images with matplotlib.pylab
plotting = input("Do you want to print the image and the reconstructed one? Y or N: \n")
if (plotting.upper() == "Y"):
    plt.gray()
    plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('original image', size=20)
    plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('reconstructed image (DCT+IDCT)', size=20)
    plt.show()

