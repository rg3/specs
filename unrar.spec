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

