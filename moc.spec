# SPEC file for moc
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
Name:		moc
Version:	2.5.2
Release:	1%{?dist}
Summary:	Music On Console

Group:		Applications/Multimedia
License:	GPLv2
URL:		http://moc.daper.net/
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	ncurses-devel
BuildRequires:	libdb-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	libvorbis-devel
BuildRequires:	flac-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	ffmpeg
BuildRequires:	gettext-devel
BuildRequires:	popt-devel

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
%{_libdir}/%{name}
%{_mandir}/man*/*
%{_docdir}/%{name}
%{_datadir}/%{name}


%changelog


