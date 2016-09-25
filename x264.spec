# SPEC file for x264
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
Name:		x264
Version:	20160925_1215_git72d53ab
Release:	1%{?dist}
Summary:	H.264 library

Group:		Applications/Multimedia
License:	GPLv2
URL:		http://www.videolan.org/developers/x264.html
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	yasm

%global debug_package %{nil}

%description


%prep
%setup -q


%build
%configure --disable-cli --enable-shared --enable-strip
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc [A-Z][A-Z][A-Z]*
%{_includedir}/*
%{_libdir}/lib*
%{_libdir}/pkgconfig/*


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%changelog


