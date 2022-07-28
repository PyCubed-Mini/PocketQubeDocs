Overview
========

.. _Explanation:
.. _Dependencies:
.. _Building:

Explanation
------------
The folder `frame/` contains the `main.py` (entry point for our software) and a custom state machine implementation.
This code is minimal enough that no changes should be required regardless of if you are targeting pycubedmini, pycubed, or emulating hardware.

The `drivers` folder contains libaries allowing one to interface with the target hardware.
We currently have the example emulator, pycubedmini driver and pycubedmini emulation. 

The `applications` folder contains the programs that utilize the drivers to achieve the specific mission objective. 
It contains the state machine configuration and tasks such as detumbling, beacon transmisions, logging and power management.

Dependencies 
------------

The required packages for this project are:
   - `python3 <https://python.org>`_
   - `numpy <https://www.numpy.org/>`_
   - `ImageMagick <https://www.imagemagick.org/>`_
   - `graphviz <https://www.graphviz.org/>`_

Numpy is used for running the emulated sattelite and is therefore not required for building.
ImageMagick and graphviz are used to create a state machine diagram along with your built files.

Building
------------

To build the flight software you run `sh build.sh {driver} {application}`.
The `{driver}` is the part of the software that interfaces with the hardware (or emulates it).
The `{application}` is what the software attempts to achieve the mission objective (by utilizing the driver to communicate with the hardware).
This allows us to easily test and develop flight software localy by emulating the hardware.

