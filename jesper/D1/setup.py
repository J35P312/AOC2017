from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(
           ["d1_a.pyx","d1_b.pyx"],               
           language="c++",
      ))
