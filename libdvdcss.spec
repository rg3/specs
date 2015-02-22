Name:		libdvdcss
Version:	1.2.13
Release:	1%{?dist}
Summary:	CSS decryption library

Group:		Applications/Multimedia
License:	GPLv2
URL:		http://www.videolan.org/developers/libdvdcss.html
Source0:	%{name}-%{version}.tar.bz2

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
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/lib*
%{_docdir}/%{name}/*



%changelog

