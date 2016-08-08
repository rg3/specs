# SPEC file for ffmpeg
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
Name:		ffmpeg
Version:	3.1.1
Release:	3%{?dist}
Summary:	Multimedia framework, libraries and tools

Group:		Applications/Multimedia
License:	Unredistributable
URL:		http://ffmpeg.org/
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	yasm
BuildRequires:	openssl-devel
BuildRequires:	lame
BuildRequires:	x264
BuildRequires:	libvpx-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	opus-devel

%global debug_package %{nil}

%description


%prep
%setup -q


%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--shlibdir=%{_libdir} \
	--mandir=%{_mandir} \
	--disable-doc \
	--enable-shared \
	--enable-gpl \
	--enable-version3 \
	--enable-nonfree \
	--enable-postproc \
	--enable-libmp3lame \
	--enable-libx264 \
	--enable-openssl \
	--enable-libpulse \
	--enable-libvpx \
	--enable-libopus \

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc [A-Z][A-Z][A-Z]*
%{_includedir}/*/*
%{_datadir}/%{name}
%{_bindir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/lib*


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%changelog


