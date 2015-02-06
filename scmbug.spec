%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32::OLE\\)'
%endif

%define upstream_version %(echo %{version} | sed -e 's/\\./-/g')

Name:		scmbug
Version:	0.26.22
Release:	4
Summary:	Integration of Software Configuration Management with Bug-tracking
License:	GPL
Group:		Networking/WWW
Url:		http://www.mkgnu.net/?q=scmbug
Source:		http://files.mkgnu.net/files/scmbug/SCMBUG_RELEASE_%{upstream_version}/source/SCMBUG_RELEASE_%{upstream_version}.tar.gz
BuildRequires:	transfig
BuildRequires:	imagemagick
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd42-sgml
BuildRequires:	docbook-utils-pdf
BuildRequires:	ghostscript-dvipdf
BuildRequires:	texlive
BuildArch:	noarch

%description
Scmbug is a system that integrates software configuration management (SCM) with
bug-tracking.  It aims to be a universal tool that will glue any SCM system
(such as CVS, Subversion, and Arch) with any bug-tracking system (such as
Bugzilla and Mantis).

%package common
Summary:    Scmbug common libraries
Group:      Networking/WWW

%description common
Provides library functionality shared by scmbug-tools and scmbug-server.

%package tools
Summary:    Scmbug integration tools
Group:      Networking/WWW
Requires:   scmbug-common = %{version}
Requires:   libxslt-proc
Requires:   docbook-utils

%description tools
Collection of tools that can install the integration glue in an SCM repository
and enhance the experience of integrating SCM with bug-tracking.

%package server
Summary:    Scmbug integration server
Group:      Networking/WWW
Requires:   scmbug-common = %{version}

%description server
Accepts integration requests from the Scmbug glue.

%package doc
Summary:    Scmbug documentation
Group:      Networking/WWW

%description doc
Provides the Scmbug manual.

%prep
%setup -q -n SCMBUG_RELEASE_%{upstream_version}

%build
export POSIXLY_CORRECT=1
%configure2_5x
make

%install
%makeinstall

# fix documentation mess
rm -rf %{buildroot}%{_docdir}/%{name}-server
rm -rf %{buildroot}%{_docdir}/%{name}-common
rm -rf %{buildroot}%{_docdir}/%{name}-tools
mv %{buildroot}%{_docdir}/%{name}-doc %{buildroot}%{_docdir}/%{name}
install -m 644 ChangeLog* %{buildroot}%{_docdir}/%{name}

%files common
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/ChangeLog*
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/TODO
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%dir %{_datadir}/%{name}/lib/Scmbug
%{_datadir}/%{name}/lib/Scmbug/*.pm

%files server
%dir %{_localstatedir}/log/%{name}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/init.d/*
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_sbindir}/*
%{_mandir}/man8/*
%{_datadir}/%{name}/lib/Scmbug/Daemon
%{_datadir}/%{name}/WebReports

%files tools
%{_mandir}/man1/*
%{_prefix}/bin/*
%dir %{_datadir}/%{name}/glue
%dir %{_datadir}/%{name}/glue/etc
%config(noreplace) %{_datadir}/%{name}/glue/etc/*
%{_datadir}/%{name}/glue/templates
%{_datadir}/%{name}/glue/bin
%{_datadir}/%{name}/lib/Scmbug/Glue
%{_datadir}/%{name}/lib/Scmbug/Tools

%files doc
%{_docdir}/%{name}/manual

