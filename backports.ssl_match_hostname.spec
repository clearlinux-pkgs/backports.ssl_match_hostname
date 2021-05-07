#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5FAC8089CD84EE48 (a.badger@gmail.com)
#
Name     : backports.ssl_match_hostname
Version  : 3.7.0.1
Release  : 51
URL      : https://files.pythonhosted.org/packages/ff/2b/8265224812912bc5b7a607c44bf7b027554e1b9775e9ee0de8032e3de4b2/backports.ssl_match_hostname-3.7.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/2b/8265224812912bc5b7a607c44bf7b027554e1b9775e9ee0de8032e3de4b2/backports.ssl_match_hostname-3.7.0.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/ff/2b/8265224812912bc5b7a607c44bf7b027554e1b9775e9ee0de8032e3de4b2/backports.ssl_match_hostname-3.7.0.1.tar.gz.asc
Summary  : The ssl.match_hostname() function from Python 3.5
Group    : Development/Tools
License  : Python-2.0
Requires: backports.ssl_match_hostname-license = %{version}-%{release}
Requires: backports.ssl_match_hostname-python = %{version}-%{release}
Requires: backports.ssl_match_hostname-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
The ssl.match_hostname() function from Python 3.7
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
Requires: backports.ssl_match_hostname-python3 = %{version}-%{release}

%description python
python components for the backports.ssl_match_hostname package.


%package python3
Summary: python3 components for the backports.ssl_match_hostname package.
Group: Default
Requires: python3-core
Provides: pypi(backports.ssl_match_hostname)

%description python3
python3 components for the backports.ssl_match_hostname package.


%prep
%setup -q -n backports.ssl_match_hostname-3.7.0.1
cd %{_builddir}/backports.ssl_match_hostname-3.7.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602133216
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/backports.ssl_match_hostname
cp %{_builddir}/backports.ssl_match_hostname-3.7.0.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/backports.ssl_match_hostname/7c6735760988438332764e448d7b201c0fdd2bc9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/backports.ssl_match_hostname/7c6735760988438332764e448d7b201c0fdd2bc9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
