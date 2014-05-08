import ctypes as _ctypes


__all__ = ['fan', 'cpu', 'battery']

_libsmc = _ctypes.cdll.LoadLibrary("./libsmc.so")

_libsmc.M_cpu_temp.restype = _ctypes.c_double
_libsmc.M_fan_speed.restype = _ctypes.c_float
_libsmc.M_battery_health.restype = _ctypes.c_char_p
_libsmc.M_battery_temp.restype = _ctypes.c_double


class _Fan(object):

    @property
    def number(self):
        return _libsmc.M_fan_number()

    def speed(self, fan):
        if fan > self.number - 1:
            return IndexError("Index for fan too big (Got {} max: {})".format(fan, self.number - 1))
        fan = int(fan)
        return _libsmc.M_fan_speed(fan)

fan = _Fan()

class _Cpu(object):

    def temp(self):
        return _libsmc.M_cpu_temp()

cpu = _Cpu()

class _Battery(object):

    @property
    def design_cycles(self):
        return _libsmc.M_battery_design_cycle_count()

    def health(self):
        return _libsmc.M_battery_health()

    def temp(self):
        return _libsmc.M_battery_temp()

    def remaining(self):
        r = _libsmc.M_battery_time_remaining()
        if r == -2:
            return "Unlimited"
        elif r == -1:
            return "Calculating"
        else:
            return r

    def percentage(self):
        return _libsmc.M_battery_charge()

battery = _Battery()
