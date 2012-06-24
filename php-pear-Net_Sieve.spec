%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Sieve
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Handles talking to timsieved
Summary(pl):	%{_pearname} - obs�uga komunikacji z timsieved
Name:		php-pear-%{_pearname}
Version:	0.9.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0b721a275a7b525a4636db977b9e7a43
URL:		http://pear.php.net/package/Net_Sieve/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an API to talk to the timsieved server that comes with Cyrus
IMAPd. Can be used to install, remove, mark active etc sieve scripts.

%description -l pl
Ten modu� udost�pnia API do komunikacji z serwerem timsieved,
do��czonym do Cyrus IMAPd. Mo�e by� u�ywany do instalowania, usuwania,
zaznaczania aktywno�ci itp. skrypt�w sieve.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
