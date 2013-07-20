from setuptools import setup

setup(
    name='Vicar2Png',
    version='0.2dev',
    author='Jessica McKellar',
    author_email='jesstess@mit.edu',
    scripts=['bin/vicar2png'],
    license='LICENSE.txt',
    description='VICAR-to-png image file converter.',
    long_description=open('README.md').read(),
    url='http://pypi.python.org/pypi/Vicar2Png/',
    install_requires=[
        "pypng",
        ],
)
