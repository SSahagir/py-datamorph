from setuptools import setup, find_packages

setup(
    name='py-datamorph',
    version='1.0.0',
    author='Sk Sahagir',
    description='A high-performance data conversion, cleaning, and statistics library.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[], 
    entry_points={
        'console_scripts': [
            'datamorph=py_datamorph.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    python_requires='>=3.6',
)