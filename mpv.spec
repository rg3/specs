Name:		mpv
Version:	0.8.0
Release:	1%{?dist}
Summary:	Media Player

Group:		Applications/Multimedia
License:	GPLv2
URL:		http://mpv.io/
Source0:	%{name}-%{version}.tar.gz


%description


%prep
%setup -q


%build
./bootstrap.py
./waf configure --prefix=%{_prefix} --mandir=%{_mandir} --confdir=%{_sysconfdir} --libdir=%{_libdir}
./waf build


%install
DESTDIR=%{buildroot} ./waf install


%files
%doc [A-Z][A-Z][A-Z]*
%{_sysconfdir}/*
%{_mandir}/man*/*
%{_bindir}/*
%{_datadir}/*/*/*/*/*
%{_datadir}/applications/*
%{_datadir}/doc/%{name}/*



%changelog

