%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Sieve
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Handles talking to timsieved
Summary(pl):	%{_class}_%{_subclass} -
Name:		php-pear-%{_pearname}
Version:	0.8
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an API to talk to the timsieved server that comes with Cyrus
IMAPd. Can be used to install, remove, mark active etc sieve scripts.

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
