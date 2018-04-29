#============================================================================
# Title       : Makefile
# Description : Makefile for asmballoon
# Author      : Bart Sjerps <bart@outrun.nl>
# License     : GPLv3+
# ---------------------------------------------------------------------------

version    = 0.1
prefix     = $$HOME
bindir     = $(prefix)/bin
mandir     = $(prefix)/share/man
docdir     = $(prefix)/share/doc

sysconfdir = /etc

all:

install:
	install -m 0755 -d $(bindir)
	install -m 0755 bin/asmballoon $(bindir)

uninstall:
	rm $(prefix)/bin/asmballoon

.PHONY: install

