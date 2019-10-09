%define tarname	Paste

Name:           python-paste
Version:	3.2.1
Release:	1
Summary:        Tools for using a Web Server Gateway Interface stack
Group:          Development/Python
License:        MIT
URL:            http://pythonpaste.org
Source0:	https://files.pythonhosted.org/packages/0d/86/7008b5563594e8a63763f05212a3eb84c85f0b2eff834e5697716e56bca9/Paste-3.2.1.tar.gz
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
