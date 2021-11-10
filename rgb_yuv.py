def YUVfromRGB(R, G, B):
  Y =  0.257 * R + 0.504 * G + 0.098 * B + 16
  U = -0.148 * R - 0.291 * G + 0.439 * B + 128
  V =  0.439 * R - 0.368 * G - 0.071 * B + 128
  return Y,U,V

def RGBfromYUV(Y, U, V):
  Y -=16
  U-=128
  V -=128
  R = 1.164 * Y + 1.596 * V
  G = 1.164 * Y - 0.392 * U - 0.813 * V
  B = 1.164 * Y + 2.017 * U
  return (R,G,B)

R = int(input("Intorduce the R value\n"))
G = int(input("Intorduce the G value\n"))
B = int(input("Intorduce the B value\n"))
a = YUVfromRGB(R,G,B)

print("This are the new YUV values: ", a)
print("Double conversion to check it work properly: ", RGBfromYUV(a[0],a[1],a[2]))