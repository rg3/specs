# SPEC file for libdvdcss
#
# Written in 2015-2016 by Ricardo Garcia <r@rg3.name>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#
Name:		libdvdcss
Version:	1.2.13
Release:	1%{?dist}
Summary:	CSS decryption library

Group:		Applications/Multimedia
License:	GPLv2
URL:		http://www.videolan.org/developers/libdvdcss.html
Source0:	%{name}-%{version}.tar.bz2

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
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/lib*
%{_docdir}/%{name}/*


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%changelog


