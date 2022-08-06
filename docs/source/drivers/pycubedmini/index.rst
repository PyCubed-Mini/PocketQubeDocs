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

    set a given voltage for a given coil driver

    :param driver_index: the index of the coil driver to set the voltage for
    :type driver_index: str
    :param projected_voltage: the voltage to set the coil driver to

Sun Sensor Interface Functions
******************************

.. py:function:: sun_vector()

    returns the sun pointing vector in the body frame

Burnwire Interface Functions
****************************

.. py:function:: burn(burn_num, dutycycle, duration)

    given a burn wire number, a dutycycle, and a burn duration, control
    the voltage of the corresponding burnwire IC
    
    :param burn_num: the index of the burnwire to control the voltage of; default 1
    :param dutycycle: the proportion of total voltage (3.3 V) the burnwire IC will be run at
    :param duration: the amount of time (seconds) the burnwire IC will be run for, default 1

Miscellaneous Interface Functions
*********************************

.. py:function:: temperature_cpu()

    return the temperature reading from the CPU in celsius

.. py:function:: setRGB(v)
    
    set the RGB value
    
    :param v: the RGB value that is being set
 
.. py:function:: getRGB()
    
    return the current RGB value

.. py:function:: battery_voltage()
    
    return the battery voltage
    read the analog value of the board.BATTERY value 50 times as a digital value
    and find the average to get a more reliable battery voltage value

.. py:function:: timeon()
    
    return the time on a monotonic clock

.. py:function:: reset_boot_count()
    
    reset boot count in non-volatile memory (nvm)

.. py:function:: incr_logfail_count()
    
    increment logfail count in non-volatile memory (nvm)

.. py:function:: reset_logfail_count()
    
    reset logfail count in non-volatile memory (nvm)



