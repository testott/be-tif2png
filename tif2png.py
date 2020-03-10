import cv2
import os

from glob import glob


print("tif2png v1.1.0\n//////////////")

while True:
  mode = input("Subfolders mode? (Y/N):")

  if mode.lower() in ("y","yes"):
    tifs = glob('./**/*.tif', recursive=True)
    break

  elif mode.lower() in ("n","no"):
    tifs = glob('./*.tif')
    break

  elif mode.lower() in ("quit","exit","stop","q"):
    quit()

  else:
    print("Please answer y/yes or n/no")


if tifs == []:
  print("No tif files found!")

else:
  for filename in tifs:
    img = cv2.imread(filename)
    cv2.imwrite(filename[:-3] + 'png', img, [int(cv2.IMWRITE_PNG_COMPRESSION), 6])
    os.remove(filename)
    print("Converted " + filename)

  print("Conversion from tif/tiff to png completed!")