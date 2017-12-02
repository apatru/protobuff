#! /usr/bin/env python

import array_pb2
import sys
import inspect

# try:
#   raw_input          # Python 2
# except NameError:
#   raw_input = input  # Python 3


# This function fills in a Person message based on user input.
def PromptForQuaternion(quaternion):
  frame = inspect.currentframe()
  args, _, _, values = inspect.getargvalues(frame)
  # print 'function name "%s"' % inspect.getframeinfo(frame)[2]
  # print 'args = "%s"' % args[0]

  # if "add()" in [args[0]]:
  quaternion.n1 = float(raw_input("Enter x: "))
  quaternion.n2 = float(raw_input("Enter y: "))
  quaternion.n3 = float(raw_input("Enter z: "))
  quaternion.n4 = float(raw_input("Enter w: "))

def AddFromExistingQuaternion(quaternion):
  quaternion.n1 = quat_ex[0]
  quaternion.n2 = quat_ex[1]
  quaternion.n3 = quat_ex[2]
  quaternion.n4 = quat_ex[3]

def Parse(array, opened_file):
  array.ParseFromString(opened_file.read())

def ParseAll(array):
  try:
    with open(sys.argv[1], "rb") as f:
      array.ParseFromString(f.read())
  except IOError:
    print(sys.argv[1] + ": File not found.  Creating a new file.")

def Serialize(array, opened_file):
  opened_file.write(array.SerializeToString())

def SerializeAll(array):
  with open(sys.argv[1], "wb") as f:
    f.write(array.SerializeToString())

def Size(array):
  size = array.SizeBytes()

def OverwriteQuaternion(quaternion, quat, number):
  quaternion[number].n1 = quat[0]
  quaternion[number].n2 = quat[1]
  quaternion[number].n3 = quat[2]
  quaternion[number].n4 = quat[3]


# def Size():


# Existing quaternions
quat_ex = [10,20,30,40]
quat = [0,0,0,0]

# Main procedure:  Reads the entire array from a file,
#   adds one quaternion based on user input, then writes it back out to the same
#   file.
if len(sys.argv) != 2:
  print("Usage:", sys.argv[0], "TestFile")
  sys.exit(-1)

array = array_pb2.Array()

# Read the existing array.
ParseAll(array)
# try:
#   with open(sys.argv[1], "rb") as f:
#     # array.ParseFromString(f.read())
#     Parse(array,f)
# except IOError:
#   print(sys.argv[1] + ": File not found.  Creating a new file.")

# Add an Array
PromptForQuaternion(array.orientation.add())
# AddFromExistingQuaternion(array.orientation.add(),quat_ex)
# OverwriteQuaternion(array.orientation, quat, 0)

# Serialize Array


# Write the new quaternion back to disk.
SerializeAll(array)
# with open(sys.argv[1], "wb") as f:
#     # f.write(array.SerializeToString())
#     Serialize(array,f)


