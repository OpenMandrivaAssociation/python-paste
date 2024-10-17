%define tarname	Paste

Name:           python-paste
Version:	3.5.0
Release:	1
Summary:        Tools for using a Web Server Gateway Interface stack
Group:          Development/Python
License:        MIT
URL:            https://pythonpaste.org
Source0:	https://files.pythonhosted.org/packages/b7/e0/eb502f90e14570c88ed108a101ff223ccc853e2ba057ac4e7d6eb40c923e/Paste-3.5.0.tar.gz
BuildArch:      noarch
Requires:	python-pkg-resources
BuildRequires:  python-setuptools
#BuildRequires:	python-sphinx

%description
These provide several pieces of "middleware" (or filters) that can be nested
to build web applications.  Each piece of middleware uses the WSGI (PEP 333)
interface, and should be compatible with other middleware based on those
interfaces.

%prep
%setup -q -n %{tarname}-%{version}
%{__sed} -i -e '/^#!.*/,1 d' paste/util/scgiserver.py paste/debug/doctest_webapp.py

%install
%py_install

%files
%{python_sitelib}/%{tarname}-%{version}*
