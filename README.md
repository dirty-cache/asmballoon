ASMBalloon - Reclaim space on Oracle ASM diskgroups
======================

## Description

ASMballoon writes files a large empty file (the BALLOON file) into an ASM diskgroup,
then deletes the file again. The result is that many unused ASM allocation units are
zeroed out so that smart storage systems can reclaim the unused capacity.

## Details

Modern storage arrays typically provide thin-provisioned capacity from a larger storage pool. If
existing files are deleted, the old file structures are still on disk and the array has no way of knowing
the capacity can be freed up - see [Trim/Unmap](https://en.wikipedia.org/wiki/Trim_(computing))

On Oracle ASM this issue is no different. Unmap is only available if you use ASM Filter Driver, which not
every customer can use or wants to use.

_asmballoon_ works by creating a large temporary [sparse file](https://en.wikipedia.org/wiki/Sparse_file) and copying it to an ASM Diskgroup to fill (most of) the free space. This causes most of the free ASM space to be overwritten with zeroes. When done, the file is deleted and the disk capacity is free to be reallocated by the storage array.

As one cannot simply write a zeroed file to ASM, _asmballoon_ works around this by making the balloon file a valid Oracle file format (the header is an Oracle SPFILE) so it is accepted by Oracle ASM.

## WARNING

This script is provided as-is. Test it before use in production. Code updates/improvements or suggestions are welcome.

_asmballoon_ is safe to use in that it only uses standard Oracle SQL statements to create and delete the balloon file. It will never write to ASM disks or diskgroups outside of the Oracle SQL interface, and therefore can not cause data  corruption (a known issue with some other ASM reclaim utilities).

Note however that _asmballoon_ causes the ASM diskgroup to be nearly full very quickly, which may cause alerts in monitoring systems and actually cause free space issues if the database(s) are writing lots of data to the ASM diskgroup at the same time.

If _asmballoon_ is aborted before cleaning up the balloon file, it will not clean up the free space. This can be solved by running _asmballoon_ again with the cleanup option, but you need to be aware of it. Worst case you can manually remove the ```BALLOON``` file and directory from the disk group using Oracle ```asmcmd```.

Also note that quickly writing lots of data (even zeroes) to an ASM diskgroup may cause some I/O contention. I have experimented with using [Linux CGroups](https://en.wikipedia.org/wiki/Cgroups) to limit the I/O bandwith but this is work in progress. Let me know if you need it.

## Installation

Clone from git, then "make install". The script is installed in $HOME/bin so you can use it without
having to run install as root. This may change in the future.

Alternatively, just place the bin/asmballoon file somewhere in your PATH and make it executable.

## Manual

Run 'asmballoon -h' for help.
