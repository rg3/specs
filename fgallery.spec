# SPEC file for fgallery
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
Name:		fgallery
Version:	1.8.2
Release:	3%{?dist}
Summary:	Minimalistic javascript photo gallery

License:	GPLv2+
URL:		https://www.thregr.org/~wavexx/software/fgallery/
Source0:	%{name}-%{version}.zip
BuildArch:	noarch

Requires:	perl
Requires:	ImageMagick
Requires:	lcms2-utils
Requires:	fbida
Requires:	zip
Requires:	perl-Image-ExifTool
Requires:	perl-Cpanel-JSON-XS
Requires:	jpegoptim
Requires:	pngcrush
Requires:	p7zip
Requires:	python3-PyQt4

%global debug_package %{nil}

%description


%prep
%setup -q


%build
# Nothing needs to be done here.


%install
mkdir -p %{buildroot}%{_datarootdir}/%{name}
mkdir -p %{buildroot}%{_datarootdir}/applications
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

sed -i -e 's,^#!/usr/bin/env python$,#!/usr/bin/python3,' utils/fcaption
gzip -9 %{name}.1
cp -R * %{buildroot}%{_datarootdir}/%{name}/.

ln -s %{_datarootdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
ln -s %{_datarootdir}/%{name}/%{name}.1.gz %{buildroot}%{_mandir}/man1/.
ln -s %{_datarootdir}/%{name}/utils/fcaption %{buildroot}%{_bindir}/fcaption
ln -s %{_datarootdir}/%{name}/utils/fcaption.desktop %{buildroot}%{_datarootdir}/applications/.


%files
%doc [A-Z][A-Z][A-Z]*
%{_datarootdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/fcaption
%{_datarootdir}/applications/fcaption.desktop


%changelog


