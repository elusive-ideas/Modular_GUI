Modular_GUI
===========

[![Code Health][landscape]][landscape_repo]

Modular GUI using PySide and Yapsy

## Current Status

Thanks for taking the time and check the project. Be aware that this is a Work-in-Progress project at the moment. None of the functionality is actually in place. Hopefully, I will start to get the basic functionality within the following weeks.

### Objectives

* 'Module Manager' to enable/disable modules.
* Modules can define widgets that live in the center of the window and/or in the dockable areas.
* Modules can be versioned so it is up to the user to load the latest version or one of the previous ones.
* Modules can be set to 'Auto-Load' so they get automatically loaded with the GUI.
* Modules can define new toolbars or add elements to the current ones.
* Modules can communicate with the elements defined in the main GUI. (E.g.: Using Status Bar).
* Modules can define information that will be accessible to both the main application and other plugins.
* Modules can add menus to the main GUI.
* Settings remember the position and state of elements of the GUI (Even the ones defined by the modules).
* The main application has a log and the modules use a child of such log.
* Main GUI should have a preferences window and modules can define new pages of preferences that hook to it in order to define preferences for the modules themselves.

## Installation

You can use PIP to install the application:

`pip install Modular_GUI`

You can also clone the repo using git:

`git clone https://github.com/davidmartinezanim/Modular_GUI.git`

Or you can download the zip file and install it manually.

[landscape]: https://landscape.io/github/davidmartinezanim/Modular_GUI/master/landscape.png
[landscape_repo]: https://landscape.io/github/davidmartinezanim/Modular_GUI/master
