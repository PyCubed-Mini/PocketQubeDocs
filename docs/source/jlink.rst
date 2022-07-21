Flashing With J-Link (incomplete/incorrect)
===========================================

Warning! This documentation is incomplete/incorrect.

.. _Ubuntu Setup:
.. _Flashing Pycubed-Mini V2:

Ubuntu Setup
------------
Download the J-Link DEB installer from `here <https://www.segger.com/downloads/jlink/>`_.
Install by running the following command:

.. code-block:: console

    sudo dpkg -i path/to/jlink_package.deb

To reflash the board run `JFlash` to launch the GUI J-Link flashing software.

Flashing Pycubed-Mini V2
------------------------

#. Connect pin 1 of the J-Link to pin1 one of the Pycubed-Mini V2 main board.

    .. image:: jlink/pycubed-miniv2.jpg
        :width: 400px

    Pin 1 of the Pycubed-Mini v2 board is the top right pin in this image, right next to the white line.

#. Set the board to `ATSAMD51J20A`

#. Click `Target->Connect`

#. "Failed to connect cannot connect to target"