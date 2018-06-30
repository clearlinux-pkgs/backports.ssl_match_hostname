#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5FAC8089CD84EE48 (a.badger@gmail.com)
#
Name     : backports.ssl_match_hostname
Version  : 3.5.0.1
Release  : 32
URL      : http://pypi.debian.net/backports.ssl_match_hostname/backports.ssl_match_hostname-3.5.0.1.tar.gz
Source0  : http://pypi.debian.net/backports.ssl_match_hostname/backports.ssl_match_hostname-3.5.0.1.tar.gz
Source99 : http://pypi.debian.net/backports.ssl_match_hostname/backports.ssl_match_hostname-3.5.0.1.tar.gz.asc
Summary  : The ssl.match_hostname() function from Python 3.5
Group    : Development/Tools
License  : Python-2.0
Requires: backports.ssl_match_hostname-python3
Requires: backports.ssl_match_hostname-license
Requires: backports.ssl_match_hostname-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
The ssl.match_hostname() function from Python 3.5
        =================================================
        
        The Secure Sockets Layer is only actually *secure*
        if you check the hostname in the certificate returned
        by the server to which you are connecting,
        and verify that it matches to hostname
        that you are trying to reach.
        
        But the matching logic, defined in `RFC2818`_,
        can be a bit tricky to implement on your own.
        So the ``ssl`` package in the Standard Library of Python 3.2
        and greater now includes a ``match_hostname()`` function
        for performing this check instead of requiring every application
        to implement the check separately.
        
        This backport brings ``match_hostname()`` to users
        of earlier versions of Python.
        Simply make this distribution a dependency of your package,

%package license
Summary: license components for the backports.ssl_match_hostname package.
Group: Default

%description license
license components for the backports.ssl_match_hostname package.


%package python
Summary: python components for the backports.ssl_match_hostname package.
Group: Default
Requires: backports.ssl_match_hostname-python3

%description python
python components for the backports.ssl_match_hostname package.


%package python3
Summary: python3 components for the backports.ssl_match_hostname package.
Group: Default
Requires: python3-core

%description python3
python3 components for the backports.ssl_match_hostname package.


%prep
%setup -q -n backports.ssl_match_hostname-3.5.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529092218
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/backports.ssl_match_hostname
cp backports/ssl_match_hostname/LICENSE.txt %{buildroot}/usr/share/doc/backports.ssl_match_hostname/backports_ssl_match_hostname_LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/backports.ssl_match_hostname/backports_ssl_match_hostname_LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
