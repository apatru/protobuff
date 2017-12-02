#! /usr/bin/env python

from __future__ import print_function
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

# This function adds Quaternion message to the Array from existing array
def AddFromExistingQuaternion(quaternion, quat):
  quaternion.n1 = quat[0]
  quaternion.n2 = quat[1]
  quaternion.n3 = quat[2]
  quaternion.n4 = quat[3]

def Parse(array):
  try:
    with open(sys.argv[1], "rb") as f:
      array.ParseFromString(f.read())
  except IOError:
    print(sys.argv[1] + ": File not found.  Creating a new file.")

def Serialize(array):
  with open(sys.argv[1], "wb") as f:
    f.write(array.SerializeToString())

def Size(array):
  size = array.ByteSize()
  return size

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

def OverwriteQuaternion(quaternion, quat, number):
  quaternion[number].n1 = quat[0]
  quaternion[number].n2 = quat[1]
  quaternion[number].n3 = quat[2]
  quaternion[number].n4 = quat[3]



## TESTING ##

# Creates a file with nb+1 quaternions and assigns value quat to the j one

# Existing quaternions
quat_ex = [10,20,30,40]
quat = [0,0,0,0]

# Number of quaterion to add
nb = 3

# Quaternion to overwrite
j = 2

# Check input arguments
if len(sys.argv) != 2:
  print("Usage:", sys.argv[0], "TestFile")
  sys.exit(-1)

array = array_pb2.Array()

# Add i quaternion to the array / creates file if doesn't exist
for i in range(0, nb):
  Parse(array)
  AddFromExistingQuaternion(array.orientation.add(), quat_ex)
  Serialize(array)

# Add Quaternion by entering values / creates file if doesn't exist
Parse(array)
PromptForQuaternion(array.orientation.add())
Serialize(array)

# Overwrite quaternion 
Parse(array)
OverwriteQuaternion(array.orientation, quat, j-1)
Serialize(array)

# Print message file information
Parse(array)
ListOrientation(array)
Serialize(array)