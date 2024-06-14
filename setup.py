from setuptools import setup, find_packages

setup(
    name='textfinder',
    version='1.3.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'colorama',
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'textfinder=textfinder:main',
        ],
    },
    author='Cristotodev',
    author_email='cristom.estevez@gmail.com',
    description='TextFinder: Una herramienta para buscar texto en archivos dentro de directorios específicos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cristotodev/Text-Finder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
