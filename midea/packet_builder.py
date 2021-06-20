
from midea.command import base_command

VERSION = '0.1.13'


class packet_builder:

    def __init__(self):
        self.command = None

        # Init the packet with the header data. Weird magic numbers, I'm not sure what they all do, but they have to be there (packet length at 0x4)
        self.packet = bytearray([
            0x5a, 0x5a, 0x01, 0x11, 0x5c, 0x00, 0x20, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x34, 0x36, 0x16, 0x0e,
            0x13, 0x05, 0x15, 0x14, 0x26, 0x33, 0x37, 0x58,
            0x88, 0x31, 0x0a, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
        ])

    def set_command(self, command: base_command):
        self.command = command.finalize()

    def finalize(self):
        # Append the command data to the packet
        self.packet.extend(self.command)
        # self.packet.extend([0] * (16))
        # Append a basic checksum of the command to the packet (This is apart from the CRC8 that was added in the command)
        self.packet.extend([self.checksum(self.command[1:])])
        # Ehh... I dunno, but this seems to make things work. Pad with 0's
        self.packet.extend([0] * (52 - len(self.command)))
        # Set the packet length in the packet!
        self.packet[0x04] = len(self.packet)
        return self.packet

    def checksum(self, data):
        return 255 - sum(data) % 256 + 1
