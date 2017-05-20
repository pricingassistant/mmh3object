from distutils.core import setup
from distutils.extension import Extension
import os

if os.path.isfile("mmh3object.cpp"):

    ext_modules = [
        Extension(
            "mmh3object",
            ["mmh3object.cpp", "MurmurHash3.cpp"]
        )
    ]

else:

    from Cython.Build import cythonize

    ext_modules = cythonize([
        Extension(
            "mmh3object",
            ["mmh3object.pyx", "MurmurHash3.cpp"],
            include_dirs=[os.path.abspath("./")],
            language="c++"
        )
    ])


setup(
    name="mmh3object",
    version="0.1",
    ext_modules=ext_modules
)
