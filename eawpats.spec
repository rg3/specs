# SPEC file for eawpats
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
%global patsconfigpath %{_sysconfdir}/timidity-%{name}.cfg
%global stdconfigpath %{_sysconfdir}/timidity.cfg
mkdir -p %{patscopydir}
cp -R * %{patscopydir}
mkdir -p %{buildroot}/%{_sysconfdir}
cat >%{buildroot}/%{patsconfigpath} <<EOF
dir %{patsdir}
source gravis.cfg
source gsdrums.cfg
source gssfx.cfg
source xgmap2.cfg
EOF


%files
%{_sysconfdir}/*
%{patsdir}/*



%post
if [ ! -e %{stdconfigpath} ]; then
    /bin/cp %{patsconfigpath} %{stdconfigpath}
fi

%preun
if [ -f %{stdconfigpath} -a -f %{patsconfigpath} ]; then
   STDSUM=$( /bin/sha1sum <%{stdconfigpath} | /bin/cut -d' ' -f1 )
   PATSUM=$( /bin/sha1sum <%{patsconfigpath} | /bin/cut -d' ' -f1 )
   if [ "$STDSUM" == "$PATSUM" ]; then
       /bin/rm %{stdconfigpath}
   fi
fi

%changelog

