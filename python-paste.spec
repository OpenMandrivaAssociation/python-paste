%define tarname	Paste
%define name	python-paste
%define version	1.7.5.1
%define release 5

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Tools for using a Web Server Gateway Interface stack
Group:          Development/Python
License:        MIT
URL:            http://pythonpaste.org
Source0:        http://pypi.python.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
Requires:	python-pkg-resources
BuildRequires:  python-setuptools
BuildRequires:	python-sphinx

%description
These provide several pieces of "middleware" (or filters) that can be nested
to build web applications.  Each piece of middleware uses the WSGI (PEP 333)
interface, and should be compatible with other middleware based on those
interfaces.

%prep
%setup -q -n %{tarname}-%{version}
%{__sed} -i -e '/^#!.*/,1 d' paste/util/scgiserver.py paste/debug/doctest_webapp.py

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's|^/usr/lib/python2.7/site-packages/Paste-1.7.5.1-py2.7.egg-info$||g' FILE_LIST
sphinx-build -b html docs html
rm -f html/.buildinfo

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root,-)
%doc html/



%changelog
* Thu Mar 31 2011 Lev Givon <lev@mandriva.org> 1.7.5.1-3mdv2011.0
+ Revision: 649508
- Fix group.
- Build docs properly.
  Require pkg_resources.

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 1.7.5.1-2mdv2011.0
+ Revision: 591770
- Rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.5.1-1mdv2011.0
+ Revision: 587726
- update to new version 1.7.5.1

* Tue Sep 14 2010 Crispin Boylan <crisb@mandriva.org> 1.7.4-1mdv2011.0
+ Revision: 578207
- 1.7.4
- New release

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.7.2-3mdv2010.0
+ Revision: 442336
- rebuild

* Fri Dec 26 2008 Crispin Boylan <crisb@mandriva.org> 1.7.2-2mdv2009.1
+ Revision: 319379
- Rebuild for python2.6

* Thu Dec 04 2008 Crispin Boylan <crisb@mandriva.org> 1.7.2-1mdv2009.1
+ Revision: 309938
- Correct group
- Initial mdv package
- create python-paste

