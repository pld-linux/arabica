#
# TODO:
# - unify Arabica <-> arabica
# - is -fPIC correct?
# - more parsers
#
Summary:	Arabica - an XML parser toolkit written in C++
Summary(pl.UTF-8):	Arabica - narzędzia do parsowania XML napisane w C++
Name:		arabica
Version:	2004_february
%define	_ver	%(echo %{version} | tr _ -)
Release:	0.1
License:	BSD-like
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/arabica/%{name}-%{_ver}.tar.gz
# Source0-md5:	64a0ccdfd9a9e10a5391237969033c3c
Patch0:		%{name}-makefile.patch
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

%prep
%setup -q -n %{name}-%{_ver}
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CPP="%{__cpp}" \
	LD="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} -fPIC" \
	INCS_DIRS="-I%{_builddir}/%{buildsubdir} `xml2-config --cflags`" \
	DYNAMIC_LIBS="-lstdc++ `xml2-config --libs`" \
	LINK_SHARED="-shared -fPIC"
#	USE_PARSER="-DUSE_EXPAT -DUSE_LIBXML2 -DUSE_XERCES"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/arabica}

install bin/libArabica.so $RPM_BUILD_ROOT%{_libdir}
find DOM SAX XML Utils -name \*.h -exec \
	install -D '{}' $RPM_BUILD_ROOT%{_includedir}/arabica/'{}' \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog todo.txt
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/arabica
