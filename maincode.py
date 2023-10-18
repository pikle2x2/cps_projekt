
import spidev
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 17
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# MCP3008 setup
spi = spidev.SpiDev()
spi.open(0, 0)

def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    while True:
        x_value = read_adc(0)
        y_value = read_adc(1)
        button_state = GPIO.input(BUTTON_PIN)

        print(f'X Value: {x_value}, Y Value: {y_value}, Button State: {"Pressed" if not button_state else "Released"}')

        if not button_state:
            print("Button Pressed!")

except KeyboardInterrupt:
    GPIO.cleanup()
