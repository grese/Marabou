import setuptools
from pathlib import Path

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

version = '0.0.1'

setuptools.setup(
    name='maraboupy-neuralnetworkverification', # Replace with your own username
    version=version,
    author='Marabou',
    author_email='',
    description='Marabou Neural Network Verification Framework for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # url='https://github.com/NeuralNetworkVerification/Marabou',
    url='https://github.com/grese/Marabou',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Modified BSD License',
        'Operating System :: Linux',
        'Operating System :: Mac OS',
        # 'Operating System :: Windows'
    ],
    python_requires='>=3.5',
    install_requires=['pybind11 >= 2.3.0'],
    dependency_links=[]
)
