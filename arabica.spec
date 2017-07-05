#
# TODO:
# - unify Arabica <-> arabica
# - more parsers
#
Summary:	Arabica - an XML parser toolkit written in C++
Summary(pl.UTF-8):	Arabica - narzędzia do parsowania XML napisane w C++
Name:		arabica
Version:	2016_January
%define	_ver	%(echo %{version} | tr _ -)
Release:	1
License:	BSD-like
Group:		Development/Libraries
Source0:	https://github.com/jezhiggins/arabica/archive/%{_ver}.tar.gz
# Source0-md5:	2ab97777049ac703e7ff03710ea9c1a2
URL:		http://www.jezuk.co.uk/cgi-bin/view/arabica
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arabica is an XML parser toolkit, providing SAX2 and DOM
implementations, written in Standard C++.

Arabica is a full SAX2 implementation, including the optional
interfaces and helper classes. It delivers UTF-8 encoded std::strings
or UCS-2 std::wstrings, but is templated on string type and so can
accommodate custom string types. It provides uniform SAX2 wrappers
for the expat parser, Xerces, libxml and, on Windows only, for the
Microsoft XML parser COM component.

%description -l pl.UTF-8
Arabica to pakiet narzędzi do parsowania XML zawierający implementacje
SAX2 i DOM napisane w standardowym C++.

Arabica to pełna implementacja SAX2 wraz z opcjonalnymi interfejsami i
klasami pomocniczymi. Dostarcza kodowane UTF-8 std::strings albo
kodowane UCS-2 std::wstrings, ale ma szablony oparte na typie string,
więc może obsługiwać własne typy string. Udostępnia jednolite wrappery
SAX2 dla parserów expat, Xerces, libxml oraz - tylko pod Windows -
komponentu COM parsera XML Microsoftu.

%package devel
Summary:	Header files for Arabica
Summary(pl.UTF-8):	Pliki nagłówkowe Arabica
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libxml2-devel

%description devel
Header files for Arabica.

%description devel -l pl.UTF-8
Pliki nagłówkowe Arabica.

%package static
Summary:	Static Arabica library
Summary(pl.UTF-8):	Statyczna biblioteka Arabica
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Arabica library.

%description static -l pl.UTF-8
Statyczna biblioteka Arabica.

%prep
%setup -q -n %{name}-%{_ver}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
     DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_bindir}/mangle $RPM_BUILD_ROOT%{_bindir}/arabica-mangle

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/arabica-mangle
%attr(755,root,root) %{_libdir}/libarabica.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libarabica.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarabica.so
%{_libdir}/libarabica.la
%{_includedir}/arabica
%{_pkgconfigdir}/arabica.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libarabica.a
