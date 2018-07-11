##GTX AUTO INSTALL EXPLOIT TOOLS
# -*- coding utf-8 -*-
import os
import sys
from time import sleep as timeout
from gxcore import *

def main():
  banner()
  print" GTX AUTO INSTALL EXPLOIT TOOLS"
  print" CREATED BY: YUKKI666"
  print" Version : Beta Ver"
  print" THANKS FOR : Garuda Tersakti 72"
  print"\n (01) Metasploit"
  print" (02) Commix"
  print" (03) sqlmap"
  print" (04) Brutal"
  print" (05) A-Rat"
  print" (06) WPSploit"
  print" (07) Websploit"
  print" (08) Routersploit"
  print" (09) BlackBox"
  print" (10) XAttacker"
  print" (11) The FatRat"
  print" (12) DrupalGeddon2"
  print" (13) DarkSploit"
  print" (14) Social Engineering"
  print" (00) Exit GTX"
  exploitool = raw_input("GTX > ")

  if exploitool == "01" or exploitool == "1":
     metasploit()
  elif exploitool == "02" or exploitool == "2":
     commix()
  elif exploitool == "03" or exploitool == "3":
     sqlmap()
  elif exploitool == "04" or exploitool == "4":
     brutal()
  elif exploitool == "05" or exploitool == "5":
     a_rat()
  elif exploitool == "06" or exploitool == "6":
     wpsploit()
  elif exploitool == "07" or exploitool == "7":
     websploit()
  elif exploitool == "08" or exploitool == "8":
     routersploit()
  elif exploitool == "09" or exploitool == "9":
     blackbox()
  elif exploitool == "10":
     xattacker()
  elif exploitool == "11":
     tfr()
  elif exploitool == "12":
     drupaleddon()
  elif exploitool == "13":
     drxp()     
  elif exploitool == "14":
     soceng()
  elif exploitool == "00":
     sys.exit()
  else:
    print "\nERROR COMMAND SALAH"
    timeout(2)
    sys.exit()

if __name__ == "__main__":
   main()