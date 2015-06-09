# SPEC file for lame
#
# Written in 2015 by Ricardo Garcia <r@rg3.name>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#
Name:		lame
Version:	3.99.5
Release:	1%{?dist}
Summary:	MP3 encoding library and tool

Group:		Applications/Multimedia
License:	LGPLv2
URL:		http://lame.sourceforge.net/
Source0:	lame-3.99.5.tar.gz

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
%{_includedir}/%{name}/*
%{_libdir}/*
%{_mandir}/man*/*

%post -p /sbin/ldconfig

%changelog

