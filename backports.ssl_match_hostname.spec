#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : backports.ssl_match_hostname
Version  : 3.5.0.1
Release  : 12
URL      : https://pypi.python.org/packages/source/b/backports.ssl_match_hostname/backports.ssl_match_hostname-3.5.0.1.tar.gz
Source0  : https://pypi.python.org/packages/source/b/backports.ssl_match_hostname/backports.ssl_match_hostname-3.5.0.1.tar.gz
Summary  : The ssl.match_hostname() function from Python 3.5
Group    : Development/Tools
License  : Python-2.0
Requires: backports.ssl_match_hostname-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
The ssl.match_hostname() function from Python 3.5
=================================================

%package python
Summary: python components for the backports.ssl_match_hostname package.
Group: Default

%description python
python components for the backports.ssl_match_hostname package.


%prep
%setup -q -n backports.ssl_match_hostname-3.5.0.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
