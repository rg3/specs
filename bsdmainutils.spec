# SPEC file for bsdmainutils
#
# Written in 2016-2018 by Ricardo Garcia <r@rg3.name>
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
Version:	11.1.2
Release:	1%{?dist}
Summary:	Small group of tools taken from BSD systems

Group:		Applications/System
License:	BSD
URL:		https://packages.debian.org/unstable/utils/bsdmainutils
Source0:	%{name}_%{version}.tar.gz
Patch0:		%{name}-no-root.patch
Patch1:		%{name}-from-man.patch
Patch2:		%{name}-ncal-symlinks.patch

BuildRequires:	libbsd-devel

%global debug_package %{nil}
%global subdirs "usr.bin/from usr.bin/lorder usr.bin/ncal"

%description


%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build
for p in $( cat debian/patches/series ); do
	patch -Np1 <debian/patches/"$p";
done
BIN=%{subdirs} make -e %{?_smp_mflags}


%install
BIN=%{subdirs} make -e install DESTDIR=%{buildroot}


%files
%doc debian/copyright debian/changelog
%{_bindir}/*
%{_mandir}/man*/*


%changelog


