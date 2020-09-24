#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gtksourceview
Version  : 4.8.0
Release  : 37
URL      : https://download.gnome.org/sources/gtksourceview/4.8/gtksourceview-4.8.0.tar.xz
Source0  : https://download.gnome.org/sources/gtksourceview/4.8/gtksourceview-4.8.0.tar.xz
Summary  : Source code editing widget
Group    : Development/Tools
License  : LGPL-2.1
Requires: gtksourceview-data = %{version}-%{release}
Requires: gtksourceview-lib = %{version}-%{release}
Requires: gtksourceview-license = %{version}-%{release}
Requires: gtksourceview-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-golang
BuildRequires : buildreq-meson
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : vala
BuildRequires : vala-bin
BuildRequires : vala-dev
Patch1: cve-2017-14108.patch

%description
Building GtkSourceView for Windows with Meson using Visual Studio
=========
Meson is now the supported method of building GtkSourceView with Visual Studio, where the process
of doing so is described in the following section:

%package data
Summary: data components for the gtksourceview package.
Group: Data

%description data
data components for the gtksourceview package.


%package dev
Summary: dev components for the gtksourceview package.
Group: Development
Requires: gtksourceview-lib = %{version}-%{release}
Requires: gtksourceview-data = %{version}-%{release}
Provides: gtksourceview-devel = %{version}-%{release}
Requires: gtksourceview = %{version}-%{release}

%description dev
dev components for the gtksourceview package.


%package lib
Summary: lib components for the gtksourceview package.
Group: Libraries
Requires: gtksourceview-data = %{version}-%{release}
Requires: gtksourceview-license = %{version}-%{release}

%description lib
lib components for the gtksourceview package.


%package license
Summary: license components for the gtksourceview package.
Group: Default

%description license
license components for the gtksourceview package.


%package locales
Summary: locales components for the gtksourceview package.
Group: Default

%description locales
locales components for the gtksourceview package.


%prep
%setup -q -n gtksourceview-4.8.0
cd %{_builddir}/gtksourceview-4.8.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600280379
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gtksourceview
cp %{_builddir}/gtksourceview-4.8.0/COPYING %{buildroot}/usr/share/package-licenses/gtksourceview/caeb68c46fa36651acf592771d09de7937926bb3
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gtksourceview-4

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GtkSource-4.typelib
/usr/share/gir-1.0/*.gir
/usr/share/gtksourceview-4/language-specs/R.lang
/usr/share/gtksourceview-4/language-specs/abnf.lang
/usr/share/gtksourceview-4/language-specs/actionscript.lang
/usr/share/gtksourceview-4/language-specs/ada.lang
/usr/share/gtksourceview-4/language-specs/ansforth94.lang
/usr/share/gtksourceview-4/language-specs/asciidoc.lang
/usr/share/gtksourceview-4/language-specs/asp.lang
/usr/share/gtksourceview-4/language-specs/automake.lang
/usr/share/gtksourceview-4/language-specs/awk.lang
/usr/share/gtksourceview-4/language-specs/bennugd.lang
/usr/share/gtksourceview-4/language-specs/bibtex.lang
/usr/share/gtksourceview-4/language-specs/bluespec.lang
/usr/share/gtksourceview-4/language-specs/boo.lang
/usr/share/gtksourceview-4/language-specs/c.lang
/usr/share/gtksourceview-4/language-specs/cg.lang
/usr/share/gtksourceview-4/language-specs/changelog.lang
/usr/share/gtksourceview-4/language-specs/chdr.lang
/usr/share/gtksourceview-4/language-specs/cmake.lang
/usr/share/gtksourceview-4/language-specs/cobol.lang
/usr/share/gtksourceview-4/language-specs/commonlisp.lang
/usr/share/gtksourceview-4/language-specs/cpp.lang
/usr/share/gtksourceview-4/language-specs/cpphdr.lang
/usr/share/gtksourceview-4/language-specs/csharp.lang
/usr/share/gtksourceview-4/language-specs/css.lang
/usr/share/gtksourceview-4/language-specs/csv.lang
/usr/share/gtksourceview-4/language-specs/cuda.lang
/usr/share/gtksourceview-4/language-specs/d.lang
/usr/share/gtksourceview-4/language-specs/dart.lang
/usr/share/gtksourceview-4/language-specs/def.lang
/usr/share/gtksourceview-4/language-specs/desktop.lang
/usr/share/gtksourceview-4/language-specs/diff.lang
/usr/share/gtksourceview-4/language-specs/docbook.lang
/usr/share/gtksourceview-4/language-specs/docker.lang
/usr/share/gtksourceview-4/language-specs/dosbatch.lang
/usr/share/gtksourceview-4/language-specs/dot.lang
/usr/share/gtksourceview-4/language-specs/dpatch.lang
/usr/share/gtksourceview-4/language-specs/dtd.lang
/usr/share/gtksourceview-4/language-specs/dtl.lang
/usr/share/gtksourceview-4/language-specs/eiffel.lang
/usr/share/gtksourceview-4/language-specs/erb-html.lang
/usr/share/gtksourceview-4/language-specs/erb-js.lang
/usr/share/gtksourceview-4/language-specs/erb.lang
/usr/share/gtksourceview-4/language-specs/erlang.lang
/usr/share/gtksourceview-4/language-specs/fcl.lang
/usr/share/gtksourceview-4/language-specs/fish.lang
/usr/share/gtksourceview-4/language-specs/forth.lang
/usr/share/gtksourceview-4/language-specs/fortran.lang
/usr/share/gtksourceview-4/language-specs/fsharp.lang
/usr/share/gtksourceview-4/language-specs/ftl.lang
/usr/share/gtksourceview-4/language-specs/gap.lang
/usr/share/gtksourceview-4/language-specs/gdb-log.lang
/usr/share/gtksourceview-4/language-specs/gdscript.lang
/usr/share/gtksourceview-4/language-specs/genie.lang
/usr/share/gtksourceview-4/language-specs/glsl.lang
/usr/share/gtksourceview-4/language-specs/go.lang
/usr/share/gtksourceview-4/language-specs/gradle.lang
/usr/share/gtksourceview-4/language-specs/groovy.lang
/usr/share/gtksourceview-4/language-specs/gtk-doc.lang
/usr/share/gtksourceview-4/language-specs/gtkrc.lang
/usr/share/gtksourceview-4/language-specs/haddock.lang
/usr/share/gtksourceview-4/language-specs/haskell-literate.lang
/usr/share/gtksourceview-4/language-specs/haskell.lang
/usr/share/gtksourceview-4/language-specs/haxe.lang
/usr/share/gtksourceview-4/language-specs/html.lang
/usr/share/gtksourceview-4/language-specs/idl-exelis.lang
/usr/share/gtksourceview-4/language-specs/idl.lang
/usr/share/gtksourceview-4/language-specs/imagej.lang
/usr/share/gtksourceview-4/language-specs/ini.lang
/usr/share/gtksourceview-4/language-specs/j.lang
/usr/share/gtksourceview-4/language-specs/jade.lang
/usr/share/gtksourceview-4/language-specs/java.lang
/usr/share/gtksourceview-4/language-specs/javascript-expressions.lang
/usr/share/gtksourceview-4/language-specs/javascript-functions-classes.lang
/usr/share/gtksourceview-4/language-specs/javascript-literals.lang
/usr/share/gtksourceview-4/language-specs/javascript-modules.lang
/usr/share/gtksourceview-4/language-specs/javascript-statements.lang
/usr/share/gtksourceview-4/language-specs/javascript-values.lang
/usr/share/gtksourceview-4/language-specs/javascript.lang
/usr/share/gtksourceview-4/language-specs/jsdoc.lang
/usr/share/gtksourceview-4/language-specs/json.lang
/usr/share/gtksourceview-4/language-specs/jsx.lang
/usr/share/gtksourceview-4/language-specs/julia.lang
/usr/share/gtksourceview-4/language-specs/kotlin.lang
/usr/share/gtksourceview-4/language-specs/language.dtd
/usr/share/gtksourceview-4/language-specs/language.rng
/usr/share/gtksourceview-4/language-specs/language2.rng
/usr/share/gtksourceview-4/language-specs/latex.lang
/usr/share/gtksourceview-4/language-specs/less.lang
/usr/share/gtksourceview-4/language-specs/lex.lang
/usr/share/gtksourceview-4/language-specs/libtool.lang
/usr/share/gtksourceview-4/language-specs/llvm.lang
/usr/share/gtksourceview-4/language-specs/logcat.lang
/usr/share/gtksourceview-4/language-specs/logtalk.lang
/usr/share/gtksourceview-4/language-specs/lua.lang
/usr/share/gtksourceview-4/language-specs/m4.lang
/usr/share/gtksourceview-4/language-specs/makefile.lang
/usr/share/gtksourceview-4/language-specs/mallard.lang
/usr/share/gtksourceview-4/language-specs/markdown.lang
/usr/share/gtksourceview-4/language-specs/matlab.lang
/usr/share/gtksourceview-4/language-specs/maxima.lang
/usr/share/gtksourceview-4/language-specs/mediawiki.lang
/usr/share/gtksourceview-4/language-specs/meson.lang
/usr/share/gtksourceview-4/language-specs/modelica.lang
/usr/share/gtksourceview-4/language-specs/mxml.lang
/usr/share/gtksourceview-4/language-specs/nemerle.lang
/usr/share/gtksourceview-4/language-specs/netrexx.lang
/usr/share/gtksourceview-4/language-specs/nsis.lang
/usr/share/gtksourceview-4/language-specs/objc.lang
/usr/share/gtksourceview-4/language-specs/objj.lang
/usr/share/gtksourceview-4/language-specs/ocaml.lang
/usr/share/gtksourceview-4/language-specs/ocl.lang
/usr/share/gtksourceview-4/language-specs/octave.lang
/usr/share/gtksourceview-4/language-specs/ooc.lang
/usr/share/gtksourceview-4/language-specs/opal.lang
/usr/share/gtksourceview-4/language-specs/opencl.lang
/usr/share/gtksourceview-4/language-specs/pascal.lang
/usr/share/gtksourceview-4/language-specs/perl.lang
/usr/share/gtksourceview-4/language-specs/php.lang
/usr/share/gtksourceview-4/language-specs/pig.lang
/usr/share/gtksourceview-4/language-specs/pkgconfig.lang
/usr/share/gtksourceview-4/language-specs/po.lang
/usr/share/gtksourceview-4/language-specs/powershell.lang
/usr/share/gtksourceview-4/language-specs/prolog.lang
/usr/share/gtksourceview-4/language-specs/protobuf.lang
/usr/share/gtksourceview-4/language-specs/puppet.lang
/usr/share/gtksourceview-4/language-specs/python.lang
/usr/share/gtksourceview-4/language-specs/python3.lang
/usr/share/gtksourceview-4/language-specs/rpmspec.lang
/usr/share/gtksourceview-4/language-specs/rst.lang
/usr/share/gtksourceview-4/language-specs/ruby.lang
/usr/share/gtksourceview-4/language-specs/rust.lang
/usr/share/gtksourceview-4/language-specs/scala.lang
/usr/share/gtksourceview-4/language-specs/scheme.lang
/usr/share/gtksourceview-4/language-specs/scilab.lang
/usr/share/gtksourceview-4/language-specs/scss.lang
/usr/share/gtksourceview-4/language-specs/sh.lang
/usr/share/gtksourceview-4/language-specs/sml.lang
/usr/share/gtksourceview-4/language-specs/solidity.lang
/usr/share/gtksourceview-4/language-specs/sparql.lang
/usr/share/gtksourceview-4/language-specs/sql.lang
/usr/share/gtksourceview-4/language-specs/sweave.lang
/usr/share/gtksourceview-4/language-specs/swift.lang
/usr/share/gtksourceview-4/language-specs/systemverilog.lang
/usr/share/gtksourceview-4/language-specs/t2t.lang
/usr/share/gtksourceview-4/language-specs/tcl.lang
/usr/share/gtksourceview-4/language-specs/tera.lang
/usr/share/gtksourceview-4/language-specs/texinfo.lang
/usr/share/gtksourceview-4/language-specs/thrift.lang
/usr/share/gtksourceview-4/language-specs/toml.lang
/usr/share/gtksourceview-4/language-specs/typescript-js-expressions.lang
/usr/share/gtksourceview-4/language-specs/typescript-js-functions-classes.lang
/usr/share/gtksourceview-4/language-specs/typescript-js-literals.lang
/usr/share/gtksourceview-4/language-specs/typescript-js-modules.lang
/usr/share/gtksourceview-4/language-specs/typescript-js-statements.lang
/usr/share/gtksourceview-4/language-specs/typescript-jsx.lang
/usr/share/gtksourceview-4/language-specs/typescript-type-expressions.lang
/usr/share/gtksourceview-4/language-specs/typescript-type-generics.lang
/usr/share/gtksourceview-4/language-specs/typescript-type-literals.lang
/usr/share/gtksourceview-4/language-specs/typescript.lang
/usr/share/gtksourceview-4/language-specs/vala.lang
/usr/share/gtksourceview-4/language-specs/vbnet.lang
/usr/share/gtksourceview-4/language-specs/verilog.lang
/usr/share/gtksourceview-4/language-specs/vhdl.lang
/usr/share/gtksourceview-4/language-specs/xml.lang
/usr/share/gtksourceview-4/language-specs/xslt.lang
/usr/share/gtksourceview-4/language-specs/yacc.lang
/usr/share/gtksourceview-4/language-specs/yaml.lang
/usr/share/gtksourceview-4/language-specs/yara.lang
/usr/share/gtksourceview-4/styles/classic.xml
/usr/share/gtksourceview-4/styles/cobalt.xml
/usr/share/gtksourceview-4/styles/kate.xml
/usr/share/gtksourceview-4/styles/oblivion.xml
/usr/share/gtksourceview-4/styles/solarized-dark.xml
/usr/share/gtksourceview-4/styles/solarized-light.xml
/usr/share/gtksourceview-4/styles/styles.rng
/usr/share/gtksourceview-4/styles/tango.xml
/usr/share/vala/vapi/gtksourceview-4.deps
/usr/share/vala/vapi/gtksourceview-4.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gtksourceview-4/gtksourceview/completion-providers/words/gtksourcecompletionwords.h
/usr/include/gtksourceview-4/gtksourceview/gtksource-enumtypes.h
/usr/include/gtksourceview-4/gtksourceview/gtksource.h
/usr/include/gtksourceview-4/gtksourceview/gtksourceautocleanups.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcebuffer.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcecompletion.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcecompletioncontext.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcecompletioninfo.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcecompletionitem.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcecompletionproposal.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcecompletionprovider.h
/usr/include/gtksourceview-4/gtksourceview/gtksourceencoding.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcefile.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcefileloader.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcefilesaver.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcegutter.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcegutterrenderer.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcegutterrendererpixbuf.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcegutterrenderertext.h
/usr/include/gtksourceview-4/gtksourceview/gtksourceinit.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcelanguage.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcelanguagemanager.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcemap.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcemark.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcemarkattributes.h
/usr/include/gtksourceview-4/gtksourceview/gtksourceprintcompositor.h
/usr/include/gtksourceview-4/gtksourceview/gtksourceregion.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcesearchcontext.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcesearchsettings.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcespacedrawer.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcestyle.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcestylescheme.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcestyleschemechooser.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcestyleschemechooserbutton.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcestyleschemechooserwidget.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcestyleschememanager.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcetag.h
/usr/include/gtksourceview-4/gtksourceview/gtksourcetypes.h
/usr/include/gtksourceview-4/gtksourceview/gtksourceundomanager.h
/usr/include/gtksourceview-4/gtksourceview/gtksourceutils.h
/usr/include/gtksourceview-4/gtksourceview/gtksourceversion.h
/usr/include/gtksourceview-4/gtksourceview/gtksourceview.h
/usr/lib64/libgtksourceview-4.so
/usr/lib64/pkgconfig/gtksourceview-4.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgtksourceview-4.so.0
/usr/lib64/libgtksourceview-4.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gtksourceview/caeb68c46fa36651acf592771d09de7937926bb3

%files locales -f gtksourceview-4.lang
%defattr(-,root,root,-)

