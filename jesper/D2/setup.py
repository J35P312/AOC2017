from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(
           ["D2_1.pyx", "D2_2.pyx"],               
           language="c++",
      ))
