#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Jacopo Maiolini and Matteo Santilli"
__license__ = "MIT"

import musicalbeeps
from blessed import Terminal
import sys

class Synthetizer:
  def __init__(self): 
    self.player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)


    # To play an A on default octave n°4 for 0.2 seconds
    self.player.play_note("A", 2.0)

    self.term = Terminal()

    self.num_octave = 1
    self.num_keys = 8*self.num_octave

    self.key_width = int(self.term.width/self.num_keys)
    self.key_height = self.term.height


  def start(self):

      with self.term.cbreak(), self.term.hidden_cursor():
        while self.term.inkey(timeout=0.02) != 'q':
          for key in (1, self.num_keys-1):
            with self.term.location(50,0):
              print(self.vertical_line())
              sys.exit(0)      
          
          
          
          # with self.term.location(0,0):
          #   print(self.leftmost_line())
          # for key in (1, self.num_keys-1):
          #   with self.term.location(key*self.key_width,0):
          #     print(self.vertical_line())
          #     sys.exit(0)   
          # with self.term.location(self.term.width,0):
          #   print(self.rightmost_line())    
              
          # self.drawSynth()

  def spin(self):
    # with self.term.fullscreen(), self.term.cbreak():
    with self.term.cbreak(), self.term.hidden_cursor():
      self.drawSynth()


  def drawSynth(self):
    # print('\u0420\u043e\u0441\u0441\u0438\u044f')
    # for key in (1,self.num_octave*8)
    
    print(self.getKey())

  def getKey(self):
    # \u2501\u2503\u250F\u2513\u2517\u251B'
    key = ''
    key_width = int(self.term.width/(self.num_octave*8))
    key_height = self.term.height
    #top-left angle
    key += '\u250F'
    #top part
    for i in range(2,key_width-1):
      key += '\u2501'
    #top-right angle
    key +='\u2513\n'
    for i in range(2,key_height-1):
      key += '\u2503\n'
    key += '\u2517'
    #bottom part
    for i in range(2,key_width-1):
      key += '\u2501'
    #bottom-right angle
    key +='\u251B'
    return key

  #include angles
  def leftmost_line(self):
    leftmost_line = '\u250F\n'
    for i in range(2,self.key_height-1):
      leftmost_line += '\u2503\n'
    leftmost_line += '\u2517'
    return leftmost_line

  #include angles
  def rightmost_line(self):
    rightmost_line = '\u2513\n'
    for i in range(2,self.key_height-1):
      rightmost_line += '\u2503\n'
    rightmost_line += '\u251B'
    return rightmost_line

  # T-shape line
  def vertical_line(self):
    vert_line = '\u2533\n'
    for i in range(2,self.key_height-1):
      vert_line += '\u2503\n'
    vert_line += '\u253B'
    return vert_line
    