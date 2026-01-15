
# polar_bear.py

from .animal import Animal


class Polar_Bear(Animal):
    def __init__(self, name="Panda"):
        super().__init__(name, species="Polar Bear")

    def sound(self):
        return "growls"

    def action(self):
        return "hibernates in an igloo!"

class test_polar_bear():
    def test_init__(self, name)
        assert super().__init__(name, species) == "Panda Polar Bear says"
        assert sound(self) == "howls"
        assert action(self) == "sleeps"
 
