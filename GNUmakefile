EXTVERSION="3.0.0"
SRCURL=http://extjs.com/products/extjs/download.php?dl=extjs3
ZIPFILE=$(BUILD)/ext-$(EXTVERSION).zip
EXTSRCDIR=$(BUILD)/ext

ifeq ($(PYTHON),)
PYTHON= `which python`
endif

PKGDIR= `pwd`
BUILD=  $(PKGDIR)/build
DIST=   $(PKGDIR)/dist
SRCDIR= $(PKGDIR)/zenoss/extjs/src

ifeq ($(findstring curl, $(shell which curl)),curl)
CLIENT=curl -L --output $(ZIPFILE)
else
CLIENT=wget -O $(ZIPFILE)
endif

all: build

$(BUILD):
	@mkdir -p $(BUILD)

$(ZIPFILE): $(BUILD)
	@echo "Downloading Ext $(EXTVERSION)"
	@cd $(BUILD)
	@$(CLIENT) $(SRCURL)

$(EXTSRCDIR): $(ZIPFILE)
	@mkdir -p $@
	@unzip $(ZIPFILE) -d $@

ext-download: $(EXTSRCDIR)

ext-install: 
	for d in adapter src/direct src/core src/data src/dd \
		ext-all.js license.txt src/locale resources  \
		src/state src/util src/widgets; do \
		mv $(EXTSRCDIR)/ext-$(EXTVERSION)/$${d} $(SRCDIR); done
	@mv $(SRCDIR)/adapter $(SRCDIR)/adapters

ext: ext-download ext-install

build: ext
	@cd $(PKGDIR); $(PYTHON) setup.py sdist

clean: 
	@cd $(PKGDIR)
	@$(PYTHON) setup.py clean
	@rm -rf $(SRCDIR)/* $(BUILD) $(DIST)

