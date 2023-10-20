
import spidev
import time

# Define SPI bus and device (Chip Select)
spi = spidev.SpiDev()
spi.open(0, 0)

# Define function to read ADC channel
def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Define function to convert ADC value to voltage
def adc_to_voltage(adc_value):
    return (adc_value / 1023.0) * 3.3

try:
    while True:
        # Read ADC value from channel 0
        adc_value = read_adc(0)
        
        # Convert ADC value to voltage
        voltage = adc_to_voltage(adc_value)
        
        # Print voltage
        print(f"Voltage: {voltage:.2f} V")
        
        # Wait for a short time (optional)
        time.sleep(0.5)

except KeyboardInterrupt:
    spi.close()
