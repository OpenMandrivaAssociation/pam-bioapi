%define name pam-bioapi
%define version 0.3.0
%define release %mkrel 5

Summary: The pam authentification module for bioapi
Name: 	 %{name}
Version: %{version}
Release: %{release}
Source0: http://www.nax.cz/pub/bioapi/pam_bioapi/%{name}_%{version}.tar.gz
License: GPL 
Group:   Sciences/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:     http://www.nax.cz/pub/bioapi/pam_bioapi/ 
BuildRequires: libpam-devel, libbioapi-devel
Requires: bioapi

%description
%prep
%setup -q -n %{name}

%build
aclocal-1.7
libtoolize --copy --force --ltdl
automake-1.7 -a -c
autoconf
%configure --libdir=/%{_lib} --enable-file-store
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall libdir=$RPM_BUILD_ROOT/%{_lib} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/test_enroll-pam_bioapi
%{_bindir}/test_verify-pam_bioapi
/%{_lib}/security/*

