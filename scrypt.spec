# SPEC file for scrypt
#
# Written in 2018-2020 by Ricardo Garcia <r@rg3.name>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#
Name:		scrypt
Version:	1.3.3
Release:	1%{?dist}
Summary:	Password-based encryption utility

License:	BSD
URL:		https://www.tarsnap.com/scrypt.html
Source0:	%{name}-%{version}.tgz

%global debug_package %{nil}

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc [A-Z][A-Z][A-Z]*
%{_bindir}/*
%{_mandir}/man*/*


%changelog


