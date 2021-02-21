from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='maraboupy-NeuralNetworkVerification',
    version='0.0.0',
    description='Marabou Neural Network Verification Framework Python Interface',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NeuralNetworkVerification/Marabou',
    author='Marabou',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
    ],
    keywords='neural network, formal verification',
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=['pybind11 >=2.3.0'],
)
