from scipy.fftpack import dct, idct
#Need to install scipy in terminal: pip install scipy

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

#Need to install scikit-image in terminal: pip install scikit-image
#from skimage.io import imread
#from skimage.color import rgb2gray
#import numpy as np
#import matplotlib.pylab as plt

# read lena RGB image and convert to grayscale
#im = rgb2gray(imread('C:/Users/laiai/OneDrive/Desktop/UNI/Encoding Systems Audio and Video/Lenna_(test_image).png'))
#imF = dct2(im)
#im1 = idct2(imF)

# check if the reconstructed image is nearly equal to the original image
#np.allclose(im, im1)
# True

# plot original and reconstructed images with matplotlib.pylab
#plt.gray()
#plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('original image', size=20)
#plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('reconstructed image (DCT+IDCT)', size=20)
#plt.show()