#============================================================================
# Title       : Makefile
# Description : Makefile for asmballoon
# Author      : Bart Sjerps <bart@outrun.nl>
# License     : GPLv3+
# ---------------------------------------------------------------------------

version    = 0.0.1
prefix     = /usr/local
bindir     = $(prefix)/bin
mandir     = $(prefix)/share/man
docdir     = $(prefix)/share/doc

sysconfdir = /etc

all:

src:
	tar -jcvf $(HOME)/SOURCES/asmballoon-$(version).tbz2 --transform "s|^|asmballoon/|" *

rpm:	src
	cd ../SPECS ; rpmbuild -ba asmballoon.spec

install:
	install -d 0755 $(bindir)
	install -m 0755 bin/asmballoon

clean:
	rm $(HOME)/SOURCES/asmballoon-$(version).tbz2

.PHONY: install

