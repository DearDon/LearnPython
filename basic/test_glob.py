import glob

for filename in sorted(glob.glob('*')):
    if not filename.replace("test", '').startswith('_'):
        print(filename.replace("test", "Don"))
        print(filename)
