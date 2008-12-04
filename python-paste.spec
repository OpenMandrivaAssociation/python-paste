Name:           python-paste
Version:        1.7.2
Release:        %mkrel 1
Summary:        Tools for using a Web Server Gateway Interface stack
Group:          System/Libraries
License:        MIT
URL:            http://pythonpaste.org
Source0:        http://cheeseshop.python.org/packages/source/P/Paste/Paste-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools


%description
These provide several pieces of "middleware" (or filters) that can be nested
to build web applications.  Each piece of middleware uses the WSGI (PEP 333)
interface, and should be compatible with other middleware based on those
interfaces.


%prep
%setup -q -n Paste-%{version}
%{__sed} -i -e '/^#!.*/,1 d' paste/util/scgiserver.py paste/debug/doctest_webapp.py

# clean docs directory
pushd docs
rm StyleGuide.txt *.css */*.css */*.js
popd

%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --single-version-externally-managed \
                             --skip-build -O1 --root=%{buildroot}

echo '%defattr (0644,root,root,0755)' > pyfiles
find %{buildroot}%{python_sitelib}/paste -type d | \
    sed 's:%{buildroot}\(.*\):%dir \1:' >> pyfiles
find %{buildroot}%{python_sitelib}/paste -not -type d -not -name '*.pyo' | \
    sed 's:%{buildroot}\(.*\):\1:' >> pyfiles
find %{buildroot}%{python_sitelib}/paste -not -type d -name '*.pyo' | \
    sed 's:%{buildroot}\(.*\):%ghost \1:' >> pyfiles



%clean
rm -rf %{buildroot}


%files -f pyfiles
%defattr(-,root,root,-)
%doc docs/*
%{python_sitelib}/Paste-%{version}-py%{pyver}*


