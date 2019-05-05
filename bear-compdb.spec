# SPEC file for Bear
#
# Written in 2019 by Ricardo Garcia <r@rg3.name>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#
Name:		bear-compdb
Version:	2.3.13
Release:	1%{?dist}
Summary:	Compilation database generator for clang tooling

License:	GPLv3
URL:		https://github.com/rizsotto/Bear
Source0:	Bear-%{version}.tar.gz

%global debug_package %{nil}

%description


%prep
%setup -q -n Bear-%{version}


%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make %{?_smp_mflags}


%install
cd build
make install DESTDIR=%{buildroot}
sed -i -e '1s,^#!/usr/bin/env python$,#!/usr/bin/python2,' %{buildroot}%{_bindir}/bear


%files
%{_bindir}/*
%{_libdir}/*
%{_mandir}/man1/*
%{_datadir}/doc/bear


%changelog


