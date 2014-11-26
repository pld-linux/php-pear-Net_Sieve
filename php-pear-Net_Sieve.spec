%define		status		stable
%define		pearname	Net_Sieve
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - handles talking to timsieved
Summary(pl.UTF-8):	%{pearname} - obsługa komunikacji z timsieved
Name:		php-pear-%{pearname}
Version:	1.3.3
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	20bdb388ce340feada1641afd603200e
URL:		http://pear.php.net/package/Net_Sieve/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0
Requires:	php-pear-PEAR-core >= 1:1.0
Suggests:	php-pear-Auth_SASL
Obsoletes:	php-pear-Net_Sieve-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Auth/SASL.*)

%description
Provides an API to talk to the timsieved server that comes with Cyrus
IMAPd. Can be used to install, remove, mark active etc sieve scripts.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ten moduł udostępnia API do komunikacji z serwerem timsieved,
dołączonym do Cyrus IMAPd. Może być używany do instalowania, usuwania,
zaznaczania aktywności itp. skryptów sieve.

Ta klasa ma w PEAR status: %{status}.

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
%{php_pear_dir}/Net/*.php
