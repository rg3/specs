# SPEC file for bsdmainutils
#
# Written in 2016-2018,2020 by Ricardo Garcia <r@rg3.name>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#
Name:		bsdmainutils
Version:	12.1.1
Release:	1%{?dist}
Summary:	Small group of tools taken from BSD systems

License:	BSD
URL:		https://packages.debian.org/unstable/utils/bsdmainutils
Source0:	%{name}_%{version}.tar.gz

BuildRequires:	libbsd-devel

%global debug_package %{nil}
%global subdirs "usr.bin/lorder usr.bin/ncal"

%description


%prep
%setup -q -n %{name}-%{version}


%build
for p in $( cat debian/patches/series ); do
	patch -Np1 <debian/patches/"$p";
done
BIN=%{subdirs} make -e %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 usr.bin/ncal/ncal %{buildroot}%{_bindir}/.
install -m 755 usr.bin/lorder/lorder %{buildroot}%{_bindir}/.
install -m 755 usr.bin/ncal/ncal.1 %{buildroot}%{_mandir}/man1/.
install -m 755 usr.bin/lorder/lorder.1 %{buildroot}%{_mandir}/man1/.


%files
%doc debian/copyright debian/changelog
%{_bindir}/*
%{_mandir}/man*/*


%changelog


