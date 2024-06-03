#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v12
# autospec commit: fbcebd0
#
Name     : gtksourceview
Version  : 5.12.1
Release  : 60
URL      : https://download.gnome.org/sources/gtksourceview/5.12/gtksourceview-5.12.1.tar.xz
Source0  : https://download.gnome.org/sources/gtksourceview/5.12/gtksourceview-5.12.1.tar.xz
Summary  : Source code editing widget
Group    : Development/Tools
License  : Apache-2.0 CC-BY-SA-3.0 LGPL-2.1
Requires: gtksourceview-data = %{version}-%{release}
Requires: gtksourceview-lib = %{version}-%{release}
Requires: gtksourceview-license = %{version}-%{release}
Requires: gtksourceview-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gi-docgen
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : vala
BuildRequires : vala-bin
BuildRequires : vala-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
GtkSourceView
=============
GtkSourceView is a GNOME library that extends GtkTextView, the standard GTK
widget for multiline text editing. GtkSourceView adds support for syntax
highlighting, undo/redo, file loading and saving, search and replace, a
completion system, printing, displaying line numbers, and other features
typical of a source code editor.

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
%setup -q -n gtksourceview-5.12.1
cd %{_builddir}/gtksourceview-5.12.1
pushd ..
cp -a gtksourceview-5.12.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1717427045
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gtksourceview
cp %{_builddir}/gtksourceview-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gtksourceview/caeb68c46fa36651acf592771d09de7937926bb3 || :
cp %{_builddir}/gtksourceview-%{version}/data/icons/COPYING %{buildroot}/usr/share/package-licenses/gtksourceview/261167ba61e9acca17c128a339a1ad1f2d6278f1 || :
cp %{_builddir}/gtksourceview-%{version}/data/snippets/licenses.snippets %{buildroot}/usr/share/package-licenses/gtksourceview/9a2d608368016f836294eefc8e698a08e393f51f || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gtksourceview-5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GtkSource-5.typelib
/usr/share/gir-1.0/*.gir
/usr/share/gtksourceview-5/fonts/BuilderBlocks.ttf
/usr/share/gtksourceview-5/language-specs/R.lang
/usr/share/gtksourceview-5/language-specs/abnf.lang
/usr/share/gtksourceview-5/language-specs/actionscript.lang
/usr/share/gtksourceview-5/language-specs/ada.lang
/usr/share/gtksourceview-5/language-specs/ansforth94.lang
/usr/share/gtksourceview-5/language-specs/asciidoc.lang
/usr/share/gtksourceview-5/language-specs/asp.lang
/usr/share/gtksourceview-5/language-specs/automake.lang
/usr/share/gtksourceview-5/language-specs/awk.lang
/usr/share/gtksourceview-5/language-specs/bennugd.lang
/usr/share/gtksourceview-5/language-specs/bibtex.lang
/usr/share/gtksourceview-5/language-specs/blueprint.lang
/usr/share/gtksourceview-5/language-specs/bluespec.lang
/usr/share/gtksourceview-5/language-specs/boo.lang
/usr/share/gtksourceview-5/language-specs/c.lang
/usr/share/gtksourceview-5/language-specs/cg.lang
/usr/share/gtksourceview-5/language-specs/changelog.lang
/usr/share/gtksourceview-5/language-specs/chdr.lang
/usr/share/gtksourceview-5/language-specs/cmake.lang
/usr/share/gtksourceview-5/language-specs/cobol.lang
/usr/share/gtksourceview-5/language-specs/commonlisp.lang
/usr/share/gtksourceview-5/language-specs/cpp.lang
/usr/share/gtksourceview-5/language-specs/cpphdr.lang
/usr/share/gtksourceview-5/language-specs/csharp.lang
/usr/share/gtksourceview-5/language-specs/css.lang
/usr/share/gtksourceview-5/language-specs/csv.lang
/usr/share/gtksourceview-5/language-specs/cuda.lang
/usr/share/gtksourceview-5/language-specs/d.lang
/usr/share/gtksourceview-5/language-specs/dart.lang
/usr/share/gtksourceview-5/language-specs/def.lang
/usr/share/gtksourceview-5/language-specs/desktop.lang
/usr/share/gtksourceview-5/language-specs/diff.lang
/usr/share/gtksourceview-5/language-specs/docbook.lang
/usr/share/gtksourceview-5/language-specs/docker.lang
/usr/share/gtksourceview-5/language-specs/dosbatch.lang
/usr/share/gtksourceview-5/language-specs/dot.lang
/usr/share/gtksourceview-5/language-specs/dpatch.lang
/usr/share/gtksourceview-5/language-specs/dtd.lang
/usr/share/gtksourceview-5/language-specs/dtl.lang
/usr/share/gtksourceview-5/language-specs/eiffel.lang
/usr/share/gtksourceview-5/language-specs/elixir.lang
/usr/share/gtksourceview-5/language-specs/erb-html.lang
/usr/share/gtksourceview-5/language-specs/erb-js.lang
/usr/share/gtksourceview-5/language-specs/erb.lang
/usr/share/gtksourceview-5/language-specs/erlang.lang
/usr/share/gtksourceview-5/language-specs/fcl.lang
/usr/share/gtksourceview-5/language-specs/fish.lang
/usr/share/gtksourceview-5/language-specs/forth.lang
/usr/share/gtksourceview-5/language-specs/fortran.lang
/usr/share/gtksourceview-5/language-specs/fsharp.lang
/usr/share/gtksourceview-5/language-specs/ftl.lang
/usr/share/gtksourceview-5/language-specs/gap.lang
/usr/share/gtksourceview-5/language-specs/gdb-log.lang
/usr/share/gtksourceview-5/language-specs/gdscript.lang
/usr/share/gtksourceview-5/language-specs/genie.lang
/usr/share/gtksourceview-5/language-specs/glsl.lang
/usr/share/gtksourceview-5/language-specs/go.lang
/usr/share/gtksourceview-5/language-specs/gradle.lang
/usr/share/gtksourceview-5/language-specs/groovy.lang
/usr/share/gtksourceview-5/language-specs/gtk-doc.lang
/usr/share/gtksourceview-5/language-specs/gtkrc.lang
/usr/share/gtksourceview-5/language-specs/haddock.lang
/usr/share/gtksourceview-5/language-specs/haskell-literate.lang
/usr/share/gtksourceview-5/language-specs/haskell.lang
/usr/share/gtksourceview-5/language-specs/haxe.lang
/usr/share/gtksourceview-5/language-specs/html.lang
/usr/share/gtksourceview-5/language-specs/idl-exelis.lang
/usr/share/gtksourceview-5/language-specs/idl.lang
/usr/share/gtksourceview-5/language-specs/imagej.lang
/usr/share/gtksourceview-5/language-specs/ini.lang
/usr/share/gtksourceview-5/language-specs/j.lang
/usr/share/gtksourceview-5/language-specs/jade.lang
/usr/share/gtksourceview-5/language-specs/java.lang
/usr/share/gtksourceview-5/language-specs/javascript-expressions.lang
/usr/share/gtksourceview-5/language-specs/javascript-functions-classes.lang
/usr/share/gtksourceview-5/language-specs/javascript-literals.lang
/usr/share/gtksourceview-5/language-specs/javascript-modules.lang
/usr/share/gtksourceview-5/language-specs/javascript-statements.lang
/usr/share/gtksourceview-5/language-specs/javascript-values.lang
/usr/share/gtksourceview-5/language-specs/javascript.lang
/usr/share/gtksourceview-5/language-specs/jsdoc.lang
/usr/share/gtksourceview-5/language-specs/json.lang
/usr/share/gtksourceview-5/language-specs/jsx.lang
/usr/share/gtksourceview-5/language-specs/julia.lang
/usr/share/gtksourceview-5/language-specs/kotlin.lang
/usr/share/gtksourceview-5/language-specs/language.dtd
/usr/share/gtksourceview-5/language-specs/language.rng
/usr/share/gtksourceview-5/language-specs/language2.rng
/usr/share/gtksourceview-5/language-specs/latex.lang
/usr/share/gtksourceview-5/language-specs/lean.lang
/usr/share/gtksourceview-5/language-specs/less.lang
/usr/share/gtksourceview-5/language-specs/lex.lang
/usr/share/gtksourceview-5/language-specs/libtool.lang
/usr/share/gtksourceview-5/language-specs/llvm.lang
/usr/share/gtksourceview-5/language-specs/logcat.lang
/usr/share/gtksourceview-5/language-specs/logtalk.lang
/usr/share/gtksourceview-5/language-specs/lua.lang
/usr/share/gtksourceview-5/language-specs/m4.lang
/usr/share/gtksourceview-5/language-specs/makefile.lang
/usr/share/gtksourceview-5/language-specs/mallard.lang
/usr/share/gtksourceview-5/language-specs/markdown.lang
/usr/share/gtksourceview-5/language-specs/matlab.lang
/usr/share/gtksourceview-5/language-specs/maxima.lang
/usr/share/gtksourceview-5/language-specs/mediawiki.lang
/usr/share/gtksourceview-5/language-specs/meson.lang
/usr/share/gtksourceview-5/language-specs/modelica.lang
/usr/share/gtksourceview-5/language-specs/mxml.lang
/usr/share/gtksourceview-5/language-specs/nemerle.lang
/usr/share/gtksourceview-5/language-specs/netrexx.lang
/usr/share/gtksourceview-5/language-specs/nix.lang
/usr/share/gtksourceview-5/language-specs/nsis.lang
/usr/share/gtksourceview-5/language-specs/objc.lang
/usr/share/gtksourceview-5/language-specs/objj.lang
/usr/share/gtksourceview-5/language-specs/ocaml.lang
/usr/share/gtksourceview-5/language-specs/ocl.lang
/usr/share/gtksourceview-5/language-specs/octave.lang
/usr/share/gtksourceview-5/language-specs/ooc.lang
/usr/share/gtksourceview-5/language-specs/opal.lang
/usr/share/gtksourceview-5/language-specs/opencl.lang
/usr/share/gtksourceview-5/language-specs/pascal.lang
/usr/share/gtksourceview-5/language-specs/perl.lang
/usr/share/gtksourceview-5/language-specs/php.lang
/usr/share/gtksourceview-5/language-specs/pig.lang
/usr/share/gtksourceview-5/language-specs/pkgconfig.lang
/usr/share/gtksourceview-5/language-specs/po.lang
/usr/share/gtksourceview-5/language-specs/powershell.lang
/usr/share/gtksourceview-5/language-specs/prolog.lang
/usr/share/gtksourceview-5/language-specs/protobuf.lang
/usr/share/gtksourceview-5/language-specs/puppet.lang
/usr/share/gtksourceview-5/language-specs/python.lang
/usr/share/gtksourceview-5/language-specs/python3.lang
/usr/share/gtksourceview-5/language-specs/reasonml.lang
/usr/share/gtksourceview-5/language-specs/rpmspec.lang
/usr/share/gtksourceview-5/language-specs/rst.lang
/usr/share/gtksourceview-5/language-specs/ruby.lang
/usr/share/gtksourceview-5/language-specs/rust.lang
/usr/share/gtksourceview-5/language-specs/scala.lang
/usr/share/gtksourceview-5/language-specs/scheme.lang
/usr/share/gtksourceview-5/language-specs/scilab.lang
/usr/share/gtksourceview-5/language-specs/scss.lang
/usr/share/gtksourceview-5/language-specs/sh.lang
/usr/share/gtksourceview-5/language-specs/sml.lang
/usr/share/gtksourceview-5/language-specs/solidity.lang
/usr/share/gtksourceview-5/language-specs/sparql.lang
/usr/share/gtksourceview-5/language-specs/spice.lang
/usr/share/gtksourceview-5/language-specs/sql.lang
/usr/share/gtksourceview-5/language-specs/star.lang
/usr/share/gtksourceview-5/language-specs/sweave.lang
/usr/share/gtksourceview-5/language-specs/swift.lang
/usr/share/gtksourceview-5/language-specs/systemverilog.lang
/usr/share/gtksourceview-5/language-specs/t2t.lang
/usr/share/gtksourceview-5/language-specs/tcl.lang
/usr/share/gtksourceview-5/language-specs/tera.lang
/usr/share/gtksourceview-5/language-specs/terraform.lang
/usr/share/gtksourceview-5/language-specs/texinfo.lang
/usr/share/gtksourceview-5/language-specs/thrift.lang
/usr/share/gtksourceview-5/language-specs/todotxt.lang
/usr/share/gtksourceview-5/language-specs/toml.lang
/usr/share/gtksourceview-5/language-specs/twig.lang
/usr/share/gtksourceview-5/language-specs/typescript-js-expressions.lang
/usr/share/gtksourceview-5/language-specs/typescript-js-functions-classes.lang
/usr/share/gtksourceview-5/language-specs/typescript-js-literals.lang
/usr/share/gtksourceview-5/language-specs/typescript-js-modules.lang
/usr/share/gtksourceview-5/language-specs/typescript-js-statements.lang
/usr/share/gtksourceview-5/language-specs/typescript-jsx.lang
/usr/share/gtksourceview-5/language-specs/typescript-type-expressions.lang
/usr/share/gtksourceview-5/language-specs/typescript-type-generics.lang
/usr/share/gtksourceview-5/language-specs/typescript-type-literals.lang
/usr/share/gtksourceview-5/language-specs/typescript.lang
/usr/share/gtksourceview-5/language-specs/vala.lang
/usr/share/gtksourceview-5/language-specs/vbnet.lang
/usr/share/gtksourceview-5/language-specs/verilog.lang
/usr/share/gtksourceview-5/language-specs/vhdl.lang
/usr/share/gtksourceview-5/language-specs/wren.lang
/usr/share/gtksourceview-5/language-specs/xml.lang
/usr/share/gtksourceview-5/language-specs/xslt.lang
/usr/share/gtksourceview-5/language-specs/yacc.lang
/usr/share/gtksourceview-5/language-specs/yaml.lang
/usr/share/gtksourceview-5/language-specs/yara.lang
/usr/share/gtksourceview-5/snippets/licenses.snippets
/usr/share/gtksourceview-5/snippets/snippets.rng
/usr/share/gtksourceview-5/styles/Adwaita-dark.xml
/usr/share/gtksourceview-5/styles/Adwaita.xml
/usr/share/gtksourceview-5/styles/classic-dark.xml
/usr/share/gtksourceview-5/styles/classic.xml
/usr/share/gtksourceview-5/styles/cobalt-light.xml
/usr/share/gtksourceview-5/styles/cobalt.xml
/usr/share/gtksourceview-5/styles/kate-dark.xml
/usr/share/gtksourceview-5/styles/kate.xml
/usr/share/gtksourceview-5/styles/oblivion.xml
/usr/share/gtksourceview-5/styles/solarized-dark.xml
/usr/share/gtksourceview-5/styles/solarized-light.xml
/usr/share/gtksourceview-5/styles/styles.rng
/usr/share/gtksourceview-5/styles/tango.xml
/usr/share/icons/hicolor/scalable/actions/completion-snippet-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/completion-word-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-class-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-define-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-enum-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-enum-value-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-function-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-include-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-method-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-namespace-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-struct-field-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-struct-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-typedef-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-union-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/lang-variable-symbolic.svg
/usr/share/vala/vapi/gtksourceview-5.deps
/usr/share/vala/vapi/gtksourceview-5.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gtksourceview-5/gtksourceview/completion-providers/snippets/gtksourcecompletionsnippets.h
/usr/include/gtksourceview-5/gtksourceview/completion-providers/words/gtksourcecompletionwords.h
/usr/include/gtksourceview-5/gtksourceview/gtksource-enumtypes.h
/usr/include/gtksourceview-5/gtksourceview/gtksource.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcebuffer.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcecompletion.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcecompletioncell.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcecompletioncontext.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcecompletionproposal.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcecompletionprovider.h
/usr/include/gtksourceview-5/gtksourceview/gtksourceencoding.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcefile.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcefileloader.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcefilesaver.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcegutter.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcegutterlines.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcegutterrenderer.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcegutterrendererpixbuf.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcegutterrenderertext.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcehover.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcehovercontext.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcehoverdisplay.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcehoverprovider.h
/usr/include/gtksourceview-5/gtksourceview/gtksourceindenter.h
/usr/include/gtksourceview-5/gtksourceview/gtksourceinit.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcelanguage.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcelanguagemanager.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcemap.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcemark.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcemarkattributes.h
/usr/include/gtksourceview-5/gtksourceview/gtksourceprintcompositor.h
/usr/include/gtksourceview-5/gtksourceview/gtksourceregion.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcescheduler.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcesearchcontext.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcesearchsettings.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcesnippet.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcesnippetchunk.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcesnippetcontext.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcesnippetmanager.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcespacedrawer.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcestyle.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcestylescheme.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcestyleschemechooser.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcestyleschemechooserbutton.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcestyleschemechooserwidget.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcestyleschememanager.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcestyleschemepreview.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcetag.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcetypes.h
/usr/include/gtksourceview-5/gtksourceview/gtksourceutils.h
/usr/include/gtksourceview-5/gtksourceview/gtksourceversion.h
/usr/include/gtksourceview-5/gtksourceview/gtksourceview.h
/usr/include/gtksourceview-5/gtksourceview/gtksourcevimimcontext.h
/usr/lib64/libgtksourceview-5.so
/usr/lib64/pkgconfig/gtksourceview-5.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgtksourceview-5.so.0.0.0
/usr/lib64/libgtksourceview-5.so.0
/usr/lib64/libgtksourceview-5.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gtksourceview/261167ba61e9acca17c128a339a1ad1f2d6278f1
/usr/share/package-licenses/gtksourceview/9a2d608368016f836294eefc8e698a08e393f51f
/usr/share/package-licenses/gtksourceview/caeb68c46fa36651acf592771d09de7937926bb3

%files locales -f gtksourceview-5.lang
%defattr(-,root,root,-)

