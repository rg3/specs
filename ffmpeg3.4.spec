# SPEC file for ffmpeg 3.4
#
# Written in 2018 by Ricardo Garcia <r@rg3.name>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#
Name:		ffmpeg3.4
Version:	3.4.1
Release:	3%{?dist}
Summary:	Multimedia framework, libraries and tools

Group:		Applications/Multimedia
License:	Unredistributable
URL:		http://ffmpeg.org/
Source0:	ffmpeg-%{version}.tar.bz2

BuildRequires:	yasm
BuildRequires:	openssl-devel
BuildRequires:	lame-devel
BuildRequires:	x264
BuildRequires:	libvpx-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	opus-devel

%global debug_package %{nil}

%description


%prep
%setup -q -n ffmpeg-%{version}


%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}/%{name} \
	--shlibdir=%{_libdir}/%{name} \
	--incdir=%{_includedir}/%{name} \
	--mandir=%{_mandir} \
	--disable-programs \
	--disable-doc \
	--disable-static \
	--disable-debug \
	--disable-filters \
	--enable-shared \
	--enable-gpl \
	--enable-version3 \
	--enable-nonfree \
	--enable-postproc \
	--enable-libmp3lame \
	--enable-openssl \
	--enable-libpulse \
	--enable-libvpx \
	--enable-libopus \

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
make uninstall-examples DESTDIR=%{buildroot}
find %{buildroot} -type l -name '*.so' -print0 | xargs -0r rm
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat >%{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf <<EOF
%{_libdir}
%{_libdir}/%{name}
EOF


%files
%{_includedir}/%{name}
%{_libdir}/%{name}
%{_sysconfdir}/ld.so.conf.d/*


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%changelog

