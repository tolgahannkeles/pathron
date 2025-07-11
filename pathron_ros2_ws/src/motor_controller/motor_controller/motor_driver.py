from gpiozero import OutputDevice, PWMOutputDevice

class MotorDriver:
    """
    MotorDriver(in1, in2, ena, in3, in4, enb)

    - in1, in2  : Sol (motor A) yön pinleri
    - ena       : Sol (motor A) enable/PWM pini
    - in3, in4  : Sağ (motor B) yön pinleri
    - enb       : Sağ (motor B) enable/PWM pini
    """

    def __init__(self, in1, in2, ena, in3, in4, enb):
        # Yön pinleri
        self._in1 = OutputDevice(in1)
        self._in2 = OutputDevice(in2)
        self._in3 = OutputDevice(in3)
        self._in4 = OutputDevice(in4)

        # PWM pinleri (0–1 arası duty-cycle değeri)
        self._pwm_left  = PWMOutputDevice(ena, frequency=1000, initial_value=0)
        self._pwm_right = PWMOutputDevice(enb, frequency=1000, initial_value=0)

    # Genel motor set fonksiyonu  (-100 … +100 arası hız)
    def set_motors(self, left_speed: float, right_speed: float):
        self._drive(self._in1, self._in2, self._pwm_left,  left_speed)
        self._drive(self._in3, self._in4, self._pwm_right, right_speed)

    # Tek motor sürücü (yardımcı)
    @staticmethod
    def _drive(pin_fwd: OutputDevice, pin_rev: OutputDevice,
               pwm: PWMOutputDevice, speed: float):
        speed = max(min(speed, 100), -100)     # sınırla
        duty  = abs(speed) / 100.0             # 0–1

        if speed > 0:        # ileri
            pin_fwd.on()
            pin_rev.off()
            pwm.value = duty
        elif speed < 0:      # geri
            pin_fwd.off()
            pin_rev.on()
            pwm.value = duty
        else:                # dur
            pin_fwd.off()
            pin_rev.off()
            pwm.value = 0

    # Temizlik
    def stop(self):
        self._pwm_left.off()
        self._pwm_right.off()

        # gpiozero, RPi.GPIO cleanup’ı otomatik yapar; ekstra çağrı gerekmez
