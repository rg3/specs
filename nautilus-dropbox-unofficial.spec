# SPEC file for nautilus-dropbox-unofficial
#
# Written in 2022 by Ricardo Garcia <r@rg3.name>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#
Name:		nautilus-dropbox-unofficial
Version:	2022.11.25
Release:	3%{?dist}
Summary:	Nautilus extension with Dropbox integration

License:	GPLv3
URL:		https://github.com/dropbox/nautilus-dropbox
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	gnome-common
BuildRequires:	nautilus-devel
BuildRequires:	python3-docutils	
BuildRequires:	python3-gobject	
BuildRequires:	gtk4-devel

%global debug_package %{nil}

%description


%prep
%setup -q


%build
./autogen.sh
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/*
%{_libdir}/nautilus/extensions-4/*
%{_mandir}/man*/*
%{_datadir}/applications/*
%{_datadir}/nautilus-dropbox/*
%{_datadir}/icons/*/*/*/*


%changelog


