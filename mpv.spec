# SPEC file for mpv
#
# Written in 2015-2018 by Ricardo Garcia <r@rg3.name>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#
Name:		mpv
Version:	0.29.1
Release:	1%{?dist}
Summary:	Media Player

Group:		Applications/Multimedia
License:	GPLv3
URL:		http://mpv.io/
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	ffmpeg
BuildRequires:	luajit-devel
BuildRequires:	libass-devel
BuildRequires:	libcdio-paranoia-devel
BuildRequires:	libv4l-devel

%global debug_package %{nil}

%description


%prep
%setup -q


%build
./bootstrap.py
./waf configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--confdir=%{_sysconfdir}/%{name} \
	--libdir=%{_libdir} \

./waf build


%install
DESTDIR=%{buildroot} ./waf install
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}


%files
%doc [A-Z][A-Z][A-Z]*
%{_sysconfdir}/%{name}
%{_bindir}/*
%{_datadir}/*/*/*/*/*
%{_datadir}/applications/*
%{_docdir}/%{name}


%changelog


