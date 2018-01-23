#from www.informit.com/articles/article.aspx?p=2491680
import spidev
spi = spidev()
spi.open(0,0)
channel = 0
vRef = 3300
result = spi.xfer2([1, (8 + channel) << 4, 0])
adcValue =((result[1] & 3) << 8) + result[2]
mVolts = round((adcValue*(vRef/1024.0)),2)
