Framework
=========

How the framework works
-----------------------

Using tasko (now called `CircuitPyton Async <https://github.com/kvc0/CircuitPython_async>`_) a set of tasks read from a config file are run at set intervals. 
This means while a certain task is waiting for a response from something like the radio, other tasks are run.

A state machine is also defined in the config file. Each state has its own set of tasks to run (and their coresponding intervals).
All the details for transitions are handled by the state machine.

One can also define exit and enter functions for each state.

State Machine
-------------

.. automodule:: state_machine
    :members:

Tasko
-----

.. automodule:: tasko
    :members:

.. autofunction:: tasko.add_task
.. autofunction:: tasko.run_later
.. autofunction:: tasko.schedule
.. autofunction:: tasko.schedule_later
.. autofunction:: tasko.sleep
.. autofunction:: tasko.suspend
.. autofunction:: tasko.run