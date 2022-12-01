import os
import setuptools
from setuptools import setup

# The version of this library at the time of forking it
_version = '1.11.0'

requirements = list(open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), 'r').readlines())

print(setuptools.find_packages('src'))

setup(name='zato-ext-python-tds',
      version=_version,
      description='Python DBAPI driver for MSSQL using pure Python TDS (Tabular Data Stream) protocol implementation',
      author='Mikhail Denisenko',
      author_email='denisenkom@gmail.com',
      url='https://github.com/denisenkom/pytds',
      license="MIT",
      packages=['pytds'],
      package_dir={'': 'src'},
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ],
      zip_safe=True,
      install_requires=requirements,
      )
