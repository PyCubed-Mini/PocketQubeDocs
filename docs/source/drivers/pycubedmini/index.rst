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


HardwareInitException
***********************

raised when initializing a piece of hardware on the cubesat fails

class _Satellite
***********************

internal to the driver file
    
.. py:function:: __new__(cls)
    
    override the built-in __new__ function
    ensure only one instance of this class can be made per process
    
    :param cls: class variable

.. py:function:: __init__(self)
    
    big init routine as the whole board is brought up
    
    :param self: instance variable
    
.. py:function:: _init_i2c1(self)
    
    initialize I2C1 bus
    
    :param self: instance variable

.. py:function:: _init_i2c2(self)
    
    initialize I2C2 bus
    
    :param self: instance variable

.. py:function:: _init_i2c3(self)
    
    initialize I2C3 bus
    
    :param self: instance variable

.. py:function:: _init_spi(self)
    
    initialize SPI bus
    
    :param self: instance variable

.. py:function:: _init_sdcard(self)
    
    define SD Parameters and initialize SD Card
    
    :param self: instance variable

.. py:function:: _init_neopixel(self)
    
    define neopixel parameters and initialize
    
    :param self: instance variable

.. py:function:: _init_imu(self)
    
    define IMU parameters and initialize
    
    :param self: instance variable

.. py:function:: _init_radio(self)
    
    define radio parameters and initialize UHF radio
    
    :param self: instance variable

.. py:function:: _init_sun_minusy(self)
    
    initialize the -Y sun sensor on I2C2
    
    :param self: instance variable

.. py:function:: _init_sun_minusz(self)
    
    initialize the -Z sun sensor on I2C2
    
    :param self: instance variable

.. py:function:: _init_sun_minusx(self)
    
    initialize the -X sun sensor on I2C1
    
    :param self: instance variable

.. py:function:: _init_sun_plusy(self)
    
    initialize the +Y sun sensor on I2C1
    
    :param self: instance variable

.. py:function:: _init_sun_plusz(self)
    
    initialize the +Z sun sensor on I2C1
    
    :param self: instance variable

.. py:function:: _init_sun_plusx(self)
    
    initialize the +X sun sensor on I2C2
    
    :param self: instance variable

.. py:function:: _init_coildriverx(self)
    
    initialize Coil Driver X on I2C3, set default modes and voltages
    
    :param self: instance variable

.. py:function:: _init_coildrivery(self)
    
    initialize Coil Driver Y on I2C3, set default modes and voltages
    
    :param self: instance variable

.. py:function:: _init_coildriverz(self)
    
    initialize Coil Driver Z on I2C3, set default modes and voltages
    
    :param self: instance variable

.. py:function:: _init_burnwire1(self)
    
    initialize Burnwire1 on PA19 (BURN1)
    
    :param self: instance variable

.. py:function:: _init_burnwire2(self)
    
    initialize Burnwire2 on PA18 (BURN2)
    
    :param self: instance variable

