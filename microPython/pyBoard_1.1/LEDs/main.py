
import pyb
import utime as ut

led1 = pyb.LED(1)
led1.off()

def FlashLED():
    while True:
        led1.toggle()
        ut.wait(0.25)


if __name__ == "__main__":
    FlashLED()