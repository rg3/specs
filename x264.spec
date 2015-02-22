Name:		x264
Version:	40bb568
Release:	1%{?dist}
Summary:	H.264 library

Group:		Applications/Multimedia
License:	GPLv2
URL:		http://www.videolan.org/developers/x264.html
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	yasm
#Requires:	

%description


%prep
%setup -q


%build
%configure --disable-cli --enable-shared --enable-strip
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc [A-Z][A-Z][A-Z]*
%{_includedir}/*
%{_libdir}/lib*
%{_libdir}/pkgconfig/*


%changelog

