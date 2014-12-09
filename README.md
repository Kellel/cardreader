cardeditor
==========

The things
----------

cardeditor.py
  Basic cardreader that talks to an RS232 serial port or pretends to be 
  one through USB.


Prerequisites
-------------

1. pyqt4 (debian pyqt-dev-tools)
2. requests (debian (python-requests)


Usage
-----

1. Plug in Card Reader
2. Find device
  1. run `dmesg`
  2. look for something like /dev/ttyUSB0
  3. if not ttyUSB0 you will need to change this in Advanced -> Set Device
3. change device ownership `chown {kellen} {/dev/ttyUSB0}` where {kellen} will be replaced with your username and {/dev/ttyUSB0} will be the device location you found in step 2.
4. run cardeditor.py `python cardeditor.py`
5. For user lookup to work you will need to app parse API keys to parse_api.py -> headers
