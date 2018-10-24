ifeq ($(PREFIX),)
	PREFIX := /usr
endif

.PHONY: install
install:
	install -d $(DESTDIR)$(PREFIX)/bin
	install -m 755 cornora $(DESTDIR)$(PREFIX)/bin/cornora

.PHONY: uninstall
uninstall:
	test -e $(DESTDIR)$(PREFIX)/bin/cornora && rm $(DESTDIR)$(PREFIX)/bin/cornora || exit 0
