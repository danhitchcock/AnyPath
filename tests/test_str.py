from anypath import AnyPath

a = AnyPath("/home/files.jpg")
print(str(a), a.suffix, a.is_root, a.is_dir)

a = AnyPath("http://home//files.jpg")
print(str(a), a.suffix, a.is_root, a.is_dir)

a = AnyPath("s3://home/files.jpg")
print(str(a), a.suffix, a.is_root, a.is_dir)

a = AnyPath("home/files.jpg")
print(str(a), a.suffix, a.is_root, a.is_dir)

a = AnyPath(r"C:\home\files.jpg")
print(str(a), a.suffix, a.is_root, a.is_dir)

a = AnyPath(r"home\files.jpg")
print(str(a), a.suffix, a.is_root, a.is_dir)

a = AnyPath(r"/home/files")
print(str(a), a.suffix, a.is_root, a.is_dir)

a = AnyPath(r"/home/files/")
print(str(a), a.suffix, a.is_root, a.is_dir)

b = AnyPath(r"some/more/folders/pic.jpg")
print("Summating: ", a + b)
print("Summation by path slash: ", a / b)
print("Sum method: ", sum([a, b, a, b]))
