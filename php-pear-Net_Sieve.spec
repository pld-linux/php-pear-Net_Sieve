%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Sieve
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - handles talking to timsieved
Summary(pl):	%{_pearname} - obs³uga komunikacji z timsieved
Name:		php-pear-%{_pearname}
Version:	1.1.3
Release:	1
Epoch:		0
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d4a0e33c293e48d2f9f439156ba78224
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

%description -l pl
Ten modu³ udostêpnia API do komunikacji z serwerem timsieved,
do³±czonym do Cyrus IMAPd. Mo¿e byæ u¿ywany do instalowania, usuwania,
zaznaczania aktywno¶ci itp. skryptów sieve.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
