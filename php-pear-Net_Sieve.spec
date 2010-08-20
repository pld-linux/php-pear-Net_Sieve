%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Sieve
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - handles talking to timsieved
Summary(pl.UTF-8):	%{_pearname} - obsługa komunikacji z timsieved
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	1
Epoch:		0
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	adf57c938d3d0da3f3da8670b6e9f68a
URL:		http://pear.php.net/package/Net_Sieve/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0
Requires:	php-pear-PEAR-core >= 1:1.4.0-0.b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an API to talk to the timsieved server that comes with Cyrus
IMAPd. Can be used to install, remove, mark active etc sieve scripts.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten moduł udostępnia API do komunikacji z serwerem timsieved,
dołączonym do Cyrus IMAPd. Może być używany do instalowania, usuwania,
zaznaczania aktywności itp. skryptów sieve.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
