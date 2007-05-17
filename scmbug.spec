%define name scmbug
%define version 0.19.13
%define upstream_version 0-19-13
%define release %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Integration of Software Configuration Management with Bug-tracking
License:    GPL
Group:      Development/Tools
Url:        http://freshmeat.net/projects/scmbug
Source:     http://files.mkgnu.net/files/scmbug/SCMBUG_RELEASE_%{upstream_version}/source/SCMBUG_RELEASE_%{upstream_version}.tar.gz
BuildRequires:  docbook-utils
BuildRequires:  transfig
BuildRequires:  ImageMagick
BuildRequires:  docbook-dtd42-sgml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Scmbug is a system that integrates software configuration management (SCM) with bug-tracking.  It aims to be a universal tool that will glue any SCM system (such as CVS, Subversion, and Arch) with any bug-tracking system (such as Bugzilla and Mantis).

%package common
Summary:    Scmbug common libraries
Group:      Development/Tools

%description common
Provides library functionality shared by scmbug-tools and scmbug-server.

%package tools
Summary:    Scmbug integration tools
Group:      Development/Tools
Requires:   scmbug-common = %{version}
Requires:   libxslt
Requires:   docbook-utils

%description tools
Collection of tools that can install the integration glue in an SCM repository and enhance the experience of integrating SCM with bug-tracking.

%package server
Summary:    Scmbug integration server.
Group:      Development/Tools
Requires:   scmbug-common = %{version}

%description server
Accepts integration requests from the Scmbug glue.

%package doc
Summary:    Scmbug documentation
Group:      Development/Tools

%description doc
Provides the Scmbug manual.

%prep
%setup -n SCMBUG_RELEASE_%{upstream_version}

%build
%configure2_5x
%make

%install
%makeinstall

%clean
rm -rf %{buildroot}

%files common
%defattr(-,root,root)
%doc ChangeLog* doc/AUTHORS doc/COPYING doc/TODO
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%dir %{_datadir}/%{name}/lib/Scmbug
%{_datadir}/%{name}/lib/Scmbug/*.pm

%files server
%defattr(-,root,root)
%doc ChangeLog* doc/AUTHORS doc/COPYING doc/TODO
%dir %{_localstatedir}/log/%{name}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/init.d/*
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_sbindir}/*
%{_mandir}/man8/*
%{_datadir}/%{name}/lib/Scmbug/Daemon

%files tools
%defattr(-,root,root)
%doc ChangeLog* doc/AUTHORS doc/COPYING doc/TODO
%{_mandir}/man1/*
%{_prefix}/bin/*
%{_datadir}/%{name}/glue
%config(noreplace) %{_datadir}/%{name}/glue/etc/*
%{_datadir}/%{name}/glue/templates/*/*
%{_datadir}/%{name}/lib/Scmbug/Glue
%{_datadir}/%{name}/lib/Scmbug/Tools

%files doc
%defattr(-,root,root)
%doc ChangeLog* doc/AUTHORS doc/COPYING doc/TODO
%doc %{_datadir}/doc/%{name}-doc/*
