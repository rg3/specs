Name:		eawpats
Version:	12
Release:	1%{?dist}
Summary:	Eric Welsh's GUS patches for TiMidity

Group:		Applications/Multimedia
License:	Proprietary
Source0:	eawpats12_full.tar.gz
BuildArch:	noarch

Requires:	timidity++

%description


%prep
%setup -q -n %{name}


%build


%install
%global patsdir %{_datadir}/timidity/%{name}
%global patscopydir %{buildroot}/%{patsdir}
mkdir -p %{patscopydir}
cp -R * %{patscopydir}
mkdir -p %{buildroot}/%{_sysconfdir}
cat >%{buildroot}/%{_sysconfdir}/timidity-%{name}.cfg <<EOF
dir %{patsdir}
source gravis.cfg
source gsdrums.cfg
source gssfx.cfg
source xgmap2.cfg
EOF


%files
%{_sysconfdir}/*
%{patsdir}/*



%changelog

