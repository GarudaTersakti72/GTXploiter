#GTOOLS CORE
#RECODE? YOU DEAD :)
# -*- coding utf-8 -*-
import os
import sys
import time

gtools_banner = """
  $$$$$$\ $$$$$$$$\ $$$\     $$$\ 
 $$  __$$\\__$$  __|\_$$\   $$  _|
$$ /  \__|  $$ |     $$ |  $$ |  
$$ |$$$$\   $$ |     $$$\ $$$ |  
$$ |\_$$ |  $$ |     $$  |\$$ |  
$$ |  $$ |  $$ |     $$ /  $$ |  
\$$$$$$  |  $$ |   $$$  |  \$$$\ 
 \______/   \__|   \___/    \___|
                                 
"""

def banner():
  print gtools_banner

def metasploit():
  print '\nSedang Menginstall Metasploit'
  os.system("apt update && apt upgrade")
  os.system("apt install git")
  os.system("git clone https://github.com/Junior60/Metasploit")
  os.system("mv metasploit.sh ~;cd ~;sh metasploit.sh")
  print 'Selesai :)'
  print "ketik msfconsole untuk menjalankan nya"

def commix():
  print '\nSedang Menginstall Commix'
  os.system('apt uptade && apt upgrade')
  os.system('apt install python2 git')
  os.system('git clone https://github.com/commixproject/commix')
  os.system('mv commix ~')
  print 'Selesai :)'

def brutal():
  print '\nSedang Menginstall Brutal'
  os.system('apt uptade && apt upgrade')
  os.system('apt install python2 git')
  os.system('git clone https://github.com/Screetsec/Brutal')
  os.system('mv Brutal ~')
  print 'Selesai :)'

def a_rat():
  print '\nSedang Menginstall A RAT'
  os.system('apt uptade && apt upgrade')
  os.system('apt install python2 git')
  os.system('git clone https://github.com/Xi4u7/A-Rat')
  os.system('mv A-Rat ~')
  print 'Selesai :)'

def wpsploit():
  print '\nSedang Menginstall WPSploit'
  os.system('apt uptade && apt upgrade')
  os.system('apt install git')
  os.system('git clone https://github.com/m4ll0k/WPSploit')
  os.system('mv WPSploit ~')
  print 'Selesai :)'

def websploit():
  print '\nSedang Menginstall websploit'
  os.system('apt uptade && apt upgrade')
  os.system('apt install git')
  os.system('git clone https://github.com/websploit/websploit')
  os.system('mv websploit ~')
  print 'Selesai :)'

def routersploit():
  print '\nSedang Menginstall routersploit'
  os.system('apt uptade && apt upgrade')
  os.system('apt install git')
  os.system('git clone https://github.com/threat9/routersploit')
  os.system('mv routersploit ~')
  print 'Selesai :)'

def blackbox():
  print '\nSedang Menginstall '
  os.system('apt uptade && apt upgrade')
  os.system('apt install git')
  os.system('git clone https://github.com/jothatron/blackbox')
  os.system('mv blackbox ~')
  print 'Selesai :)'

def xattacker():
  print '\nSedang Menginstall XAttacker'
  os.system('apt uptade && apt upgrade')
  os.system('apt install git')
  os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
  os.system('mv XAttacker ~')
  print 'Selesai :)'

def tfr():
  print '\nSedang Menginstall TheFatRat'
  os.system('apt uptade && apt upgrade')
  os.system('apt install python2 git')
  os.system('git clone https://github.com/Screetsec/TheFatRat')
  os.system('mv TheFatRat ~')
  print 'Selesai :)'

def drupalgeddon():
  print '\nSedang Menginstall Drupalgeddon'
  os.system('apt uptade && apt upgrade')
  os.system('apt install ruby git')
  os.system('git clone https://github.com/dreadlocked/Drupalgeddon2')
  os.system('mv Drupalgeddon2 ~')
  print 'Selesai :)'

def drxp():
  print '\nSedang Menginstall DarkSploit'
  os.system('apt uptade && apt upgrade')
  os.system('apt install git')
  os.system('git clone https://github.com/LOoLzeC/DarkSploit')
  os.system('mv DarkSploit ~')
  print 'Selesai :)'  

def soceng():
  print '\nSedangg Menginstall Social-Engineering'
  os.system('apt uptade && apt upgrade')
  os.system('apt install git')
  os.system('git clone https://github.com/trustedsec/social-engineering-toolkit')
  os.system('mv social-engineering-toolkit ~')
  print 'Selesai :)'
