import re
import copy
from cached_property import cached_property


class AnyPath:
    def __init__(self, path=None):

        self.sep = "/"
        self.prefix = "/"
        self.is_root = False
        self.flavor = "posix"

        # first check if it's a posix root path
        if path.startswith("/"):
            self.prefix = "/"
            self.is_root = True

        # now check if it's a url-like object
        elif path.find("://") > -1:
            self.prefix = re.search(".*://", path)[0]
            self.is_root = True
            self.sep = "/"
            self.flavor = "url"

        # if there is a backslash, it's a windows like object
        elif path.find("\\") > -1:
            re_result = re.search(".*:\\\\", path)
            if re_result:
                self.prefix = re_result[0]
                self.is_root = True
            self.flavor = "windows"
            self.sep = "\\"

        pre_len = len(self.prefix) if self.is_root else 0
        self.components = [p for p in path[pre_len:].split(self.sep) if p]
        self.is_dir = False
        if path.endswith(self.sep):
            self.is_dir = True

    def __str__(self):
        pathstr = self.sep.join(self.components)
        if self.is_root:
            pathstr = self.prefix + pathstr
        if self.is_dir:
            pathstr += self.sep
        return pathstr

    def __add__(self, other):
        if isinstance(other, str):
            other = type(self)(other)
        a = copy.deepcopy(self)
        a.components += other.components
        a.is_dir = other.is_dir
        return a

    def __radd__(self, other):
        if other is not 0:
            return self + other
        return self

    def __truediv__(self, other):
        return self + other

    def __fspath__(self):
        return str(self)

    @property
    def suffix(self):
        if self.components[-1].find(".") > -1:
            return self.components[-1].split(".")[-1]
        return None
