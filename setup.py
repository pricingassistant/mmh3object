from distutils.core import setup
from distutils.extension import Extension
import os

if os.path.isfile("mmh3object.cpp"):

    setup(
        ext_modules=[
            Extension(
                "mmh3object",
                ["mmh3object.cpp", "MurmurHash3.cpp"]
            )
        ]
    )

else:

    from Cython.Build import cythonize

    setup(
        ext_modules=cythonize([
            Extension(
                "mmh3object",
                ["mmh3object.pyx", "MurmurHash3.cpp"],
                include_dirs=[os.path.abspath("./")],
                language="c++"
            )
        ])
    )
