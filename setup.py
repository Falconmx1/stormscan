from setuptools import setup, find_packages

setup(
    name="stormscan",
    version="0.1.0",
    author="Falconmx1",
    description="⚡ Escáner de red multithread más potente que nmap/zenmap",
    packages=find_packages(),
    install_requires=[
        'nmap',
        'python-nmap',
        'colorama',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'stormscan=main:main',
        ],
    },
)
