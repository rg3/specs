Name:		ffmpeg
Version:	2.5.4
Release:	1%{?dist}
Summary:	Multimedia framework, libraries and tools

Group:		Applications/Multimedia
License:	Unredistributable
URL:		http://ffmpeg.org/
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	yasm openssl-devel

%description


%prep
%setup -q


%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --shlibdir=%{_libdir} --mandir=%{_mandir} --enable-gpl --enable-nonfree --disable-doc --enable-postproc --enable-libmp3lame --enable-libx264 --enable-shared --enable-openssl
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc [A-Z][A-Z][A-Z]*
%{_includedir}/*/*
%{_datadir}/%{name}/*
%{_bindir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/lib*



%changelog

