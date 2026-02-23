from machine import Pin, PWM
import time


# Button setup
buttonDown = Pin(13, Pin.IN, Pin.PULL_DOWN)  # HIGH when not pressed, LOW when pressed
buttonUp = Pin(12, Pin.IN, Pin.PULL_DOWN)  # HIGH when not pressed, LOW when pressed

# ===== RAW IR DATA =====

power = [
    8931, 4440,
    568, 568, 568, 568, 568, 568, 568, 1652,
    568, 1652, 568, 1652, 568, 542, 568, 1652,
    568, 1652, 568, 1652, 568, 1652, 568, 568,
    568, 568, 568, 568, 568, 1652, 568, 568,
    568, 1652, 568, 568, 568, 1652, 568, 1652,
    568, 1652, 568, 542, 568, 542, 568, 1652,
    568, 568, 568, 1652, 568, 568, 568, 568,
    568, 568, 568, 1652, 568, 1652, 568, 568,
    568, 39520, 8931, 2220, 568
]

volUp = [
    8963, 4455,
    573, 547, 573, 547, 573, 521, 573, 1667,
    573, 1641, 573, 1641, 573, 547, 573, 1641,
    573, 1641, 573, 1641, 573, 1641, 573, 547,
    573, 521, 573, 521, 573, 1641, 573, 521,
    573, 1641, 573, 1641, 573, 521, 573, 1641,
    573, 1641, 573, 547, 573, 521, 573, 1641,
    573, 521, 573, 521, 573, 1641, 573, 521,
    573, 547, 573, 1641, 573, 1641, 573, 547,
    573, 39603, 8937, 2215, 573
]

volDown = [
    8963, 4455,
    573, 547, 573, 547, 573, 521, 573, 1667,
    573, 1641, 573, 1641, 573, 547, 573, 1641,
    573, 1667, 573, 1641, 573, 1641, 573, 547,
    573, 547, 573, 521, 573, 1667, 573, 521,
    573, 547, 573, 1641, 573, 547, 573, 1641,
    573, 1667, 573, 521, 573, 547, 573, 1641,
    573, 1667, 573, 521, 573, 1667, 573, 521,
    573, 547, 573, 1641, 573, 1667, 573, 521,
    573, 39681, 8937, 2215, 573
]
# ===== IR SETUP =====
ir = PWM(Pin(15), freq=38000, duty=0)

# ===== BLUE LED =====
led = Pin(2, Pin.OUT)

def send_raw(data):
    mark = True
    led.value(1)  # LED ON while transmitting
    
    for duration in data:
        if mark:
            ir.duty(700)   # stronger signal than 512
        else:
            ir.duty(0)
        time.sleep_us(duration)
        mark = not mark

    ir.duty(0)
    led.value(0)  # LED OFF after transmit


while True:
  if buttonDown.value():  # pressed
      send_raw(power)
  if buttonUp.value():  # pressed
      send_raw(volDown)
  time.sleep(0.3)
