MAKE ?= gmake
EXECUTABLES = errptjson psjson

.PHONY: all install uninstall $(EXECUTABLES)

all: $(EXECUTABLES)

-include $(DEPENDENCIES)

install: $(EXECUTABLES)
	mkdir -p $(PREFIX)/bin
	cp $(EXECUTABLES) $(PREFIX)/bin/

uninstall:
	-cd $(PREFIX)/bin/ && rm $(EXECUTABLES)

clean:
	for executable in $(EXECUTABLES); do $(MAKE) -f Makefile.$$executable clean; done

$(EXECUTABLES): %:
	$(MAKE) -f Makefile.$@
