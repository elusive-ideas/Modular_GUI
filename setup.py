from setuptools import setup, find_packages

setup(
    name="modular-gui",
    version="0.0.1",
    packages=find_packages(),
    install_requires=['PySide', ],
    author="David Martinez",
    author_email="david.martinez.anim@gmail.com",
    description="Modular GUI using PySide",
    url="https://github.com/davidmartinezanim/Modular_GUI",
    entry_points={'gui_scripts': ['modular-gui = modular_gui.main', ]}
)
