%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Sieve
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - handles talking to timsieved
Summary(pl):	%{_pearname} - obs³uga komunikacji z timsieved
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	707ea1b512243d0463ffd08bae717cbc
URL:		http://pear.php.net/package/Net_Sieve/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an API to talk to the timsieved server that comes with Cyrus
IMAPd. Can be used to install, remove, mark active etc sieve scripts.

%description -l pl
Ten modu³ udostêpnia API do komunikacji z serwerem timsieved,
do³±czonym do Cyrus IMAPd. Mo¿e byæ u¿ywany do instalowania, usuwania,
zaznaczania aktywno¶ci itp. skryptów sieve.

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
%doc %{_pearname}-%{version}/test_sieve.php
%{php_pear_dir}/%{_class}/*.php
