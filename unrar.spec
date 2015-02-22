# SPEC file to create a package
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
Name:		unrar
Version:	5.2.6
Release:	1%{?dist}
Summary:	RAR archive extractor

Group:		Applications/Archiving
License:	Proprietary
URL:		http://www.rarlab.com/
Source0:	unrarsrc-%{version}.tar.gz


%description


%prep
%setup -q -n %{name}


%build
make %{?_smp_mflags}


%install
install -d %{buildroot}/%{_bindir}
install -m 755 %{name} %{buildroot}/%{_bindir}


%files
%{_bindir}/*


%changelog

