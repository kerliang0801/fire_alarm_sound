#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import os
import pygame.mixer

file_path = os.path.expanduser('~/ros2_ws/src/fire_alarm_sound/fire_alarm_sound/resource/fire_alarm.mp3')

class fire_alarm_sound(Node):
    def __init__(self):
        super().__init__('fire_alarm_node')
        pygame.init()
        pygame.mixer.music.load(file_path)

        self.sub = self.create_subscription(Bool,
                                            'fire_alarm_trigger',
                                            self.fire_alarm_callback,
                                            10)

        self.already_triggered = False

    def fire_alarm_callback(self, msg):
        if msg.data is True and self.already_triggered is False:
            print("playing")
            self.already_triggered = True
            pygame.mixer.music.play()

        else:
            print("stopping")
            self.already_triggered = False
            pygame.mixer.music.stop()


def main(args=None):
    rclpy.init(args=args)
    fire_alarm = fire_alarm_sound()
    rclpy.spin(fire_alarm)
    fire_alarm.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
