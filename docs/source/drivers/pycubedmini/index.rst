Pycubed-Mini Drivers
====================

PyCubed.py
----------

IMU Interface Functions
***********************

.. py:function:: acceleration()

    return the accelerometer reading from the IMU in m/s^2 

.. py:function:: magnetometer()

    return the magnetometer reading from the IMU in µT

.. py:function:: gyro()

    return the gyroscope reading from the IMU in deg/s

.. py:function:: temperature_imu()

    return the thermometer reading from the IMU in celsius

Coil Driver Interface Functions
*******************************

.. py:function:: coildriver_vout(driver_index, projected_voltage)

    Set a given voltage for a given coil driver

    :param driver_index: the index of the coil driver to set the voltage for
    :type driver_index: str
    :param projected_voltage: the voltage to set the coil driver to
