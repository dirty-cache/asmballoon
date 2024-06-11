
# Code snippet for throttling I/O to ASM using CGroups

#echo "8:32 4000000" > /sys/fs/cgroup/blkio/blkio.throttle.write_bps_device
#echo $PID > /sys/fs/cgroup/blkio/limit1M/tasks
#https://unix.stackexchange.com/questions/48138/how-to-throttle-per-process-i-o-to-a-max-limit
def throttle(dg):
    try:
        os.mkdir('/sys/fs/cgroup/blkio/asmballoon')
    except OSError:
        pass
    r = sysdba(f"SELECT path FROM v$asm_disk JOIN v$asm_diskgroup dg USING (group_number) WHERE dg.name = '{dg}';")
    disks = r.splitlines()
    if not disks:
        return
    lim = int(1000 / len(disks))
    t = ''
    for disk in disks:
        s  = os.stat(os.path.realpath(disk))
        with open('/sys/fs/cgroup/blkio/asmballoon/blkio.throttle.write_bps_device', 'w') as f:
            f.write(f'{os.major(s.st_rdev)}:{os.minor(s.st_rdev)} {lim}\n')
    with open('/sys/fs/cgroup/blkio/asmballoon/blkio.throttle.write_bps_device') as f:
        print(f.read())
