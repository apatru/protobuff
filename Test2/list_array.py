#! /usr/bin/env python

from __future__ import print_function
import array_pb2
import sys

def Size(array):
  size = array.ByteSize()
  print(size)

# Iterates though all people in the Array and prints info about them.
def ListOrientation(array):
  counter = 1
  size = array.ByteSize()
  for quaternion in array.orientation:
    print("Quaternion n", counter)
    print("x = ", quaternion.n1)
    print("y = ", quaternion.n2)
    print("z = ", quaternion.n3)
    print("w = ", quaternion.n4)
    counter += 1
  print("File size = ", size, " bytes")
    


# Main procedure:  Reads the entire array from a file and prints all
#   the information inside.
if len(sys.argv) != 2:
  print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
  sys.exit(-1)

array = array_pb2.Array()

# Read the existing Array.
with open(sys.argv[1], "rb") as f:
  array.ParseFromString(f.read())


ListOrientation(array)