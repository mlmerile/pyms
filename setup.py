from setuptools import setup

setup(name='pyms',
      version='0.1',
      description='Ms Wrapper',
      author='Thomas Dias-Alves',
      packages=['pyms'],
      install_requires=[
          'numpy'
      ]
      test_suite='pyms.test',
      zip_safe=False)
