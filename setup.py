import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name="Modular GUI",
    version="0.0.1",
    packages=find_packages(),
    install_requires=['PySide', ],
    author="David Martinez",
    author_email="david.martinez.anim@gmail.com",
    description="Modular GUI using PySide and Yapsy",
    url="https://github.com/davidmartinezanim/Modular_GUI",
)
