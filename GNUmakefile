ifeq ($(PYTHON),)
PYTHON= `which python`
endif

PKGDIR= `pwd`
BUILD=  $(PKGDIR)/build
DIST=   $(PKGDIR)/dist
SRCDIR= $(PKGDIR)/zenoss/extjs/src
EXTSRCDIR=$(BUILD)/ext

ZIPFILE=$(wildcard ext-*.zip)
EXTVERSION=$(patsubst ext-%.zip,%,$(ZIPFILE))

all: build

$(BUILD):
	@mkdir -p $(BUILD)

$(EXTSRCDIR): $(BUILD)
	@mkdir -p $@
	@unzip $(ZIPFILE) -d $@
	mv $(EXTSRCDIR)/ext-$(EXTVERSION).* $(EXTSRCDIR)/extjs-$(EXTVERSION)

ext-install:
	for d in src \
		ext.js ext-all.js ext-all-debug.js ext-all-dev.js license.txt resources examples;  do \
		cp -r $(EXTSRCDIR)/extjs-$(EXTVERSION)/$${d} $(SRCDIR); done


ext: $(EXTSRCDIR) ext-install

build: ext
	@cd $(PKGDIR); $(PYTHON) setup.py sdist

clean:
	@cd $(PKGDIR)
	@$(PYTHON) setup.py clean
	@rm -rf $(SRCDIR)/* $(BUILD) $(DIST)
