# IthoRFT

Itho Daalderop ventilator RFT remote Python interface

## Installation

This application depends on [pycc1101](https://github.com/kostyaz/pycc1101) library, which should be installed first.

## Usage

*pycc1101* provides a Python interface to TI CC1101 chip via SPI, assuming bus 0, device 0 address.
Internally it uses [spidev](https://pypi.org/project/spidev/) Python module as its sole non-standard dependency.

On the hardware side it should work on any computer with SPI, Linux, Python 2 and *spidev*. I tested it to work on Raspberry Pi 2B.

`itho.py`, when started from command line, shows a menu with commands to send to an Itho ventilator. It is self-explanatory.
