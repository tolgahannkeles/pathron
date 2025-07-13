from gpiozero import DistanceSensor

class HCSR04:
    def __init__(self, trig_pin=23, echo_pin=24):
        self.sensor = DistanceSensor(echo=echo_pin, trigger=trig_pin, max_distance=4.0)

    def get_distance(self):
        # Mesafe metre cinsinden gelir
        distance = self.sensor.distance  # bu zaten 0.0–1.0 arasında normalized float
        return round(distance, 2)  # metre cinsinden, iki basamak

    def cleanup(self):
        self.sensor.close()
