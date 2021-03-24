#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Jacopo Maiolini and Matteo Santilli"
__license__ = "MIT"

import musicalbeeps
from blessed import Terminal

class Synthetizer:

  player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)


  # To play an A on default octave n°4 for 0.2 seconds
  player.play_note("A", 2.0)

  t = Terminal()

  print (t.bold('Hi there!'))
  print (t.bold_red_on_bright_green('It hurts my eyes!'))

  with t.location(0, t.height - 1):
    print ('This is at the bottom.')


  def start(self):
    a = 3
    # try:
    #     while True:
    #         self.spin()
    # except KeyboardInterrupt:
    #     pass

  def spin(self):
    print('''
    |  |  |
    |  |  |
    |  |  |
    |  |  |
    |  |  |
        ''',end='\r')