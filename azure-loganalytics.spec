#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-loganalytics
Version  : 0.1.0
Release  : 7
URL      : https://files.pythonhosted.org/packages/7a/37/6d296ee71319f49a93ea87698da2c5326105d005267d58fb00cb9ec0c3f8/azure-loganalytics-0.1.0.zip
Source0  : https://files.pythonhosted.org/packages/7a/37/6d296ee71319f49a93ea87698da2c5326105d005267d58fb00cb9ec0c3f8/azure-loganalytics-0.1.0.zip
Summary  : Microsoft Azure Log Analytics Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-loganalytics-python = %{version}-%{release}
Requires: azure-loganalytics-python3 = %{version}-%{release}
Requires: azure-common
Requires: msrest
BuildRequires : azure-common
BuildRequires : buildreq-distutils3
BuildRequires : msrest

%description
==============================
        
        This is the Microsoft Azure Log Analytics Client Library.
        
        This package has been tested with Python 2.7, 3.4, 3.5 and 3.6.

%package python
Summary: python components for the azure-loganalytics package.
Group: Default
Requires: azure-loganalytics-python3 = %{version}-%{release}

%description python
python components for the azure-loganalytics package.


%package python3
Summary: python3 components for the azure-loganalytics package.
Group: Default
Requires: python3-core
Provides: pypi(azure_loganalytics)
Requires: pypi(azure_common)
Requires: pypi(azure_nspkg)
Requires: pypi(msrest)

%description python3
python3 components for the azure-loganalytics package.


%prep
%setup -q -n azure-loganalytics-0.1.0
cd %{_builddir}/azure-loganalytics-0.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588780875
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.9/site-packages/azure/__init__.py
rm -f %{buildroot}/usr/lib/python3.9/site-packages/azure/__pycache__/__init__.cpython-38.pyc

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
