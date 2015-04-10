# SPEC file for libmad
#
# Written in 2015 by Ricardo Garcia <public at rg3.name>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#
Name:		libmad
Version:	0.15.1b
Release:	1%{?dist}
Summary:	MPEG Audio Decoder

Group:		Applications/Multimedia
License:	GPLv2
URL:		http://www.underbit.com/products/mad/
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-remove-force-mem.patch

%description


%prep
%setup -q
%patch0 -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc [A-Z][A-Z][A-Z]*
%{_includedir}/*
%{_libdir}/lib*



%post -p /sbin/ldconfig

%changelog

