from PIL import Image
import sys

if (len(sys.argv) != 4):
  print('Must specify input files and output file name.')
  sys.exit()

fname1 = sys.argv[1]
fname2 = sys.argv[2]
fnameOut = sys.argv[3]

# Load the two images.
im1 = Image.open(fname1)
pix1 = im1.load()
im2 = Image.open(fname2)
pix2 = im2.load()

# Save a copy of the second image to build the output from.
#im2.save(fnameOut)
#imOutput = Image.open(f)
#pixOut = imOutput.load()

# Assume the two images are identical in size.
width = im1.size[0]
height = im1.size[1]

for x in range(width):
  for y in range(height):
    #pixOut[x,y] = tuple([abs(pix1[x,y][channel] - pix2[x,y][channel]) for channel in range(3)])
    pix2[x,y] = tuple([abs(pix1[x,y][channel] - pix2[x,y][channel]) for channel in range(3)])

#imOutput.save('output.png')
im2.save(fnameOut)

