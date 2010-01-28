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

ext-install: 
	for d in adapter src/direct src/core src/data src/dd \
		ext-all.js ext-all-debug.js license.txt src/locale resources  \
		src/state src/util src/widgets examples/ux/treegrid; do \
		mv $(EXTSRCDIR)/ext-$(EXTVERSION)/$${d} $(SRCDIR); done
	@mv $(SRCDIR)/adapter $(SRCDIR)/adapters

ext: $(EXTSRCDIR) ext-install

build: ext
	@cd $(PKGDIR); $(PYTHON) setup.py sdist

clean: 
	@cd $(PKGDIR)
	@$(PYTHON) setup.py clean
	@rm -rf $(SRCDIR)/* $(BUILD) $(DIST)

