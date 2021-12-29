from ast import literal_eval as le
from pprint import pprint as pretty

myImage = open('../data/myImage').read().strip()
image = open('../data/image').read().strip()

print(len(myImage))
print(len(image))
