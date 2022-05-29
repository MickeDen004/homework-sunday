# Device
# SocketBY
# SocketMX
# Adapter
import string
import random


# Client
class Device:
    __power = None

    def __init__(self, power, manufacturer="X", model="F", year="YYYY"):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.__ip_address = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        self.__power = power

    def charge(self):
        if self.__power.voltage() > 110:
            print("Device is on fire!")
        else:
            if self.__power.live() == 1 and \
                    self.__power.neutral() == -1:
                print("Your device is charging successfully")
            else:
                print("No power...")

    @staticmethod
    def serial_number(count=11):
        all_chars = string.ascii_uppercase + string.digits
        chars_count = len(all_chars)
        serial_list = []

        while count > 0:
            random_number = random.randint(0, chars_count - 1)

            random_character = all_chars[random_number]

            serial_list.append(random_character)

            count -= 1

        return "".join(serial_list)


class SocketBY_Interface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def earth(self):
        pass


# Adaptee
class SocketBY(SocketBY_Interface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


class SocketMX_Interface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass


# Adapter
class Adapter(SocketMX_Interface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()

# d = Device("samsung,", "EW", "2000")
# print(d.serial_number())


def main():
    socket = SocketBY()
    adapter = Adapter(socket)
    device = Device(adapter)

    device.charge()
    return 0


if __name__ == "__main__":
    main()