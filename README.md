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
  a. run `dmesg` 
  b. look for something like /dev/ttyUSB0
  c. if not ttyUSB0 you will need to change this in cardreader{2}.py
3. Ensure pyqt4 is installed
5. run cardreader.py
