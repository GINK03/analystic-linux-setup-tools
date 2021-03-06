#!/usr/bin/env python3


#echo "export PSSH={WRITE_SSH_PASS}" >> $HOME/.bashrc
#echo "export PATH=$HOME/.opt/bin:$PATH" >> $HOME/.bashrc
def init_bin():
  HOME = os.environ['HOME'] 
  if Path(f'{HOME}/.opts').exists() is False:
    shutil.copytree('opts', f'{HOME}/.opts')

    print('Add opts/bin to PATH')
    output = f'export PATH="$HOME/.opts/bin:$PATH"\n'
    Path(f'{HOME}/.bashrc').open('a').write(output) 

def install_bins():
  #print('Please input your linux password.')
  #PW = input().strip()
  os.system(f'sudo snap install kotlin')  
  os.system(f'sudo apt install neovim')
  os.system(f'sudo apt install openjdk-8-jdk')

print('this is a setup tools for Analyst Linux.')
import os
from pathlib import Path
import argparse as Ap
import shutil

init_bin()

p = Ap.ArgumentParser(description='Setup of Analyst Linux.')
p.add_argument("-p", "--python", type=bool, default=False)
p.add_argument("-s", "--ssh", type=bool, default=False)
p.add_argument("-b", "--bin", type=bool, default=False)
args = p.parse_args()

if args.bin == True:
  install_bins()

if args.python == True:
  bases = ['pandas', 'numpy', 'tensorflow-gpu', 'keras', 'scikit-learn']
  for base in bases:
    os.system(f'sudo pip3 install {base}')

if args.ssh == True:
  print('Try to install sshpass')
  os.system('sudo apt install sshpass 2>&1')

  HOME = os.environ['HOME'] 
  print('Please input yourt ssh-username.')
  USSH = input().strip()
  output = f'export USSH={USSH}\n'
  Path(f'{HOME}/.bashrc').open('a').write(output) 

  print('Please input yourt ssh-password.')
  PSSH = input().strip()
  output = f'export PSSH={PSSH}\n'
  Path(f'{HOME}/.bashrc').open('a').write(output) 




