Software Architecture
=====================

.. _Overview:
.. _Hardware:
.. _Firmware:
.. _Drivers:
.. _Framework:
.. _Application:

Overview
------------
The flight software stack consists of the following blocks.
These are intended to be self contained and independent of each other.

This makes emulation of the hardware easier, and testing easier.

.. image:: software/hamburger.svg
    :width: 400

Hardware
--------

At the very bottom we have the hardware, this includes your PCB's, IMU, Microcontroller, etc...

Firmware
--------

Firmware includes the following:

* `CircuitPython <https://circuitpython.org>`_, which is a easy to use Python implementation meant to be run on a microcontroller.
* Various other bits of C/C++ to set up communication between the microcontroller and the CircuitPython VM.

Drivers
-------

The Driver Layer defines functions used to communicate with components such as the radio, IMU, magnetometer, sun sensors, etc...

Framework
---------

The Framework Layer is responsible for Scheduling and Running various tasks.
It does this by reading from a state machine config file, where each state contains a list of tasks and the frequencies they are run at.
It is also responsbile for switching between tasks while one is waiting on something (such as the radio to recieve something).

Application
-----------

The Application Layer defines the Tasks, and configures the state machine to run them at the desired frequencies.
It is also responsible for telling the framework to switch states.
This is where all the complex logic and mission specific details will go.

It is important that the Application Layer works independently of the underlying layers.
This enables swapping out the lower layers and thus easily emulating the opperations of the sattelite.
Thus the lower layers are made to be as simple as possible.