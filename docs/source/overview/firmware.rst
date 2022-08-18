Firmware
=================================

Updating PyCubedMini Firmware
-----------------------------

Based on `these instructions <https://github.com/PyCubed-Mini/avionics-motherboard/blob/zac-updates/firmware/README.md>`_.
Instructions written for PycubedMiniV02.

#. Connect the PyCubed-Mini board to your computer via USB.
#. Quickly double click the "RESET" button on the board (only small black button on the board).
   When the board boots into BOOTLOADER mode, the LED should be bright and white.
   The board should also mount as `PYCUBEDBOOT`.
#. Then drag and drop the `update_bootloader.uf2 <https://github.com/PyCubed-Mini/avionics-motherboard/blob/zac-updates/firmware/pycubedminiv02/update_bootloader.uf2>`_ into the the `PYCUBEDBOOT` drive (do this). 
   However, renaming it to `CURRENT.uf2` and replacing the current `CURRENT.uf2` file in the drive also worked. 
   The board should automatically reboot and update.
#. Wait for the board to unmount, then remount in bootloader mode again. 
#. Copy over `firmware.uf2 <https://github.com/PyCubed-Mini/avionics-motherboard/blob/zac-updates/firmware/pycubedminiv02/firmware.uf2>`_
#. The board should automatically reboot, and remount as `CIRCUITPY`
#. If the libraries/code require updating also update the `lib` directory and the relevant python files.
