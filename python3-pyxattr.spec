#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define 	module	pyxattr
Summary:	Python 3 module for accessing Extended Attributes of the files
Summary(pl.UTF-8):	Moduł Pythona 3 pozwalający na dostęp do rozszerzonych atrybutów plików
Name:		python3-%{module}
Version:	0.7.1
Release:	2
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	https://pyxattr.k1024.org/downloads/%{module}-%{version}.tar.gz
# Source0-md5:	f3341e703489452afaf68b336be5d32c
URL:		https://pyxattr.k1024.org/
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-recommonmark
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-libs >= 1:3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 3 module for accessing Extended Attributes of the files.

%description -l pl.UTF-8
Moduł Pythona 3 pozwalający na dostęp do rozszerzonych atrybutów
plików.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-3/lib.*) \
%{__python3} -m pytest test
%endif

%if %{with doc}
sphinx-build-3 -b html doc doc/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{py3_sitedir}/xattr.cpython-*.so
%{py3_sitedir}/pyxattr-%{version}-py*.egg-info
