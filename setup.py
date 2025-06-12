from setuptools import setup, find_packages

setup(
    name='aupyo',
    version='0.1.0',
    author='Etienne-bdt',
    author_email='aupyo@ebardet.fr',
    description='A package for audio processing utilities',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/aupyo',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'scipy',
        'librosa',
        'matplotlib',
        'soundfile',
    ],
)