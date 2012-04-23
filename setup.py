from setuptools import setup

setup(
    name='Vicar2Png',
    version='0.1dev',
    author='Jessica McKellar',
    author_email='jesstess@mit.edu',
    scripts=['bin/vicar2png'],
    license='LICENSE.txt',
    description='VICAR-to-png image file converter.',
    long_description=open('README.txt').read(),
    url='http://pypi.python.org/pypi/Vicar2Png/',
    install_requires=[
        "pypng",
        ],
)
