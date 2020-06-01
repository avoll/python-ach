from distutils.core import setup

setup(
    name='openfolio-ach',
    author='Openfolio',
    author_email='alex.voll@gmail.com',
    version='0.4.5',
    packages=[
        'ach',
    ],
    url='https://github.com/avoll/python-ach',
    license='MIT License',
    description='Library to create and parse ACH files (NACHA)',
    long_description=open('README.rst').read(),
)