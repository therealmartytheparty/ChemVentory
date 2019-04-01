import time
import sys

class load_cell:

    EMULATE_HX711=False

    if not EMULATE_HX711:
        import RPi.GPIO as GPIO
        from hx711 import HX711
    else:
        from emulated_hx711 import HX711

    hx = HX711(5, 6)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(1)
    hx.reset()
    #hx.tare()

    def taring():
        hx.tare()

    def getting_weight():
        chem_weight = hx.get_weight(10)
        hx.power_down()
        return chem_weight
