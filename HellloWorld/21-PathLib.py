from pathlib import Path

#Absolute Path
path = Path("ecommerce")
print(path.exists())

path = Path("Test")
print(path.mkdir()) #creates test
print(path.rmdir()) #removes Test

#glob - search for files and dir in current path
path = Path()
#print(path.glob('*.py'))
for file in path.glob('*.py'):
    print(file)

#Relative Path