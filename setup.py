from setuptools import setup, find_packages

setup(name='pyms',
      version='0.1',
      description='Ms Wrapper',
      author='Thomas Dias-Alves',
      packages=find_packages(),
      install_requires=[
          'numpy'
      ],
      test_suite='pyms.test',
      zip_safe=False)
