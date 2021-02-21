import os, sys, stat, setuptools, urllib.request, zipfile
from pathlib import Path

# print('SETUP ARGS:', sys.argv)

def get_os_name():
    if sys.platform == 'linux' or sys.platform == 'linux2':
        return 'linux'
    elif sys.platform == "darwin":
        return 'macos'
    elif sys.platform == "win32":
        return 'windows'

def download_and_unzip(url, dest_dir='./'):
    zip_path, _ = urllib.request.urlretrieve(url)
    with zipfile.ZipFile(zip_path, 'r') as f:
        f.extractall(dest_dir)

def marabou_setup(os_name, version):
    # binary_url = f'https://github.com/NeuralNetworkVerification/Marabou/releases/download/{version}/marabou-{os_name}.zip'
    binary_url = f'https://github.com/grese/Marabou/releases/download/{version}/marabou-{os_name}.zip'
    binary_url = 'https://github.com/grese/actions-test/releases/download/v0.0.3/actions-test-macos.zip'
    binary_dir = './'
    # download and unzip marabou binary
    download_and_unzip(binary_url, dest_dir=binary_dir)
    binary_ext = '.exe' if os_name == 'windows' else ''
    binary_path = os.path.join(binary_dir, f'marabou-{os_name}{binary_ext}')
    # make binary executable
    st = os.stat(binary_path)
    os.chmod(binary_path, st.st_mode | stat.S_IEXEC)

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

version = '0.0.1'
os_name = get_os_name()
package_dir = os.path.dirname(os.path.abspath(__file__))
marabou_setup(os_name, package_dir)

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
