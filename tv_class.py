# Pseudocode

class TV:
    def __init__(self):
    # Construct a default TV object
    # Initialize the TV with channel 1, volume level 1, and turned off
    self.channel = 1
    self.volumeLevel = 1
    self.on = False
    # Turn on the TV
    def turn_on(self):
        self.on = True
    # Turn off the TV
    def turn_off(self):
        self.on = False
    # Return the channel of the current TV
    def get_channel(self):
        return self.channel
    # Set a new channel for the TV if the TV is on and the channel is within the range (1 to 120)
    def set_channel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel
    # Return the current volume level of the TV
    def get_volume(self):
        ruturn self.volumeLevel
    # Set a new volume level for the TV if the TV is on and the volume level is within the range (1 to 7)
    def set_volume(self,volumeLevel):
        if 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel
    # Increase the channel number by 1 if the TV is on and the current channel is less than 120
    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1
    # Decrease the channel number by 1 if the TV is on and the current channel is greater than 1
    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1
    # Increase the volume level by 1 if the TV is on and the current volume level is less than 7
    def volume_up(self):
        if self.on and self.volumeLevel < 7:
    # Decrease the volume level by 1 if the TV is on and the current volume level is greater than 1