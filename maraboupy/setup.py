import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='maraboupy-neuralnetworkverification', # Replace with your own username
    version='0.0.1',
    author='Marabou',
    author_email='',
    description='Marabou Neural Network Verification Framework for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NeuralNetworkVerification/Marabou',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Modified BSD License',
        'Operating System :: Mac OS',
        'Operating System :: Linux',
        'Operating System :: Windows'
    ],
    python_requires='>=3.5',
    install_requires=['pybind11'],
    dependency_links=[]
)

# install_requires =
#     my_package_win_amd64 ; platform_system=="Windows" and platform_machine=="x86_64"
#     my_package_linux-x86_64 ; platform_system=="Linux" and platform_machine=="x86_64"
