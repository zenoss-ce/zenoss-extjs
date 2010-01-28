zenoss.extjs 
A Zope package wrapper around the Ext JS JavaScript library. 
Copyright 2009 Zenoss, Inc. 
All rights reserved. See LICENSE.txt for licensing.

Ext JS - JavaScript Library
Copyright (c) 2006-2009, Ext JS, LLC
All rights reserved.
licensing@extjs.com


BUILDING
==============================
If this package contains a GNUmakefile, you can build a Python package
containing the Ext source. If it does not, you already have the source.

To download the Ext source and build the package, simply run 'make'. The
artifact will be created under dist/zenoss.extjs-<version>.tar.gz.


INSTALLATION
==============================
Installation is the same as any other Python package. Unpack the tarball and
install with setuptools:

    $ tar xzf zenoss.extjs-2.2.1.tar.gz
    $ cd zenoss.extjs-2.2.1
    $ python setup.py install

You can also include the package in a buildout recipe.


USAGE
==============================
This package makes Ext source files traversable as browser resources under the
name 'extjs':

    <script src="++resource++extjs/ext-all.js"></script>

Refer to Ext documentation for load order, dependencies, etc.

