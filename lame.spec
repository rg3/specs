Name:		lame
Version:	3.99.5
Release:	1%{?dist}
Summary:	MP3 encoding library and tool

Group:		Applications/Multimedia
License:	LGPLv2
URL:		http://lame.sourceforge.net/
Source0:	lame-3.99.5.tar.gz

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
%{_includedir}/%{name}/*
%{_libdir}/*
%{_mandir}/man*/*

%changelog

