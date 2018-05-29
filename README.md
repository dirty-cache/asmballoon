ASMBalloon - Reclaim space on Oracle ASM diskgroups
======================

## Description

ASMballoon writes files with zeroes into an ASM diskgroup until reaching a certain watermark,
then deletes all created files again. The result is many unused ASM allocation units are 
zeroed out so that smart storage systems can reclaim the unused capacity.

## WARNING

This script is still experimental. Don't use in production, feel free to test and play around.
Code updates welcome.

## Internals

You cannot just write any file to Oracle ASM. ASMBalloon therefore creates a sparse Linux file 
of the required size (say 1GB) then overwrites the first block with the contents 
of an Oracle SPFILE.

This makes Oracle think we're saving parameter files and allows the write.

## Installation

Clone from git, then "make install". The script is installed in $HOME/bin so you can use it without
having to run install as root. This may change in the future.

## Manual

Run 'asmballoon -h' for help.
