%define tarname	Paste

Name:           python-paste
Version:	3.1.0
Release:	1
Summary:        Tools for using a Web Server Gateway Interface stack
Group:          Development/Python
License:        MIT
URL:            http://pythonpaste.org
Source0:	https://files.pythonhosted.org/packages/36/05/554bf8d9104d8470137daf337ed3ff06dbc8889422e0d4ad53c1011caae4/Paste-3.1.0.tar.gz
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
