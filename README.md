cardreader
==========

The things
----------

cardreader.py
  Basic cardreader
  
cardreader2.py
   Cardreader with parse integration

Usage
-----

1. Plug in Card Reader
2. Find device 
..a. run `dmesg` 
..b. look for something like /dev/ttyUSB0
..c. if not ttyUSB0 you will need to change this in cardreader{2}.py
3. change device ownership `chown {kellen} {/dev/ttyUSB0}` where {kellen} will be replaced with your username and {/dev/ttyUSB0} will be the device location you found in step 2. 
3. Ensure pyqt4 is installed
4. run cardreader.py or cardreader2.py `python cardreader.py`
