Summary:	Trust management system
Name:		keynote
Version:	2.3
Release:	1
License:	BSD
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	http://www.cis.upenn.edu/~angelos/Code/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KeyNote is a simple and flexible trust-management system designed to
work well for a variety of large- and small- scale Internet-based
applications. It provides a single, unified language for both local
policies and credentials. KeyNote policies and credentials, called
`assertions', contain predicates that describe the trusted actions
permitted by the holders of specific public keys. KeyNote assertions
are essentially small, highly-structured programs. A signed assertion,
which can be sent over an untrusted network, is also called a
`credential assertion'. Credential assertions, which also serve the
role of certificates, have the same syntax as policy assertions but
are also signed by the principal delegating the trust.

%prep

%setup -q

%build
./configure --prefix=%{_prefix}
%{__make} crypto CFLAGS="-Wall $RPM_OPT_FLAGS"

%{__make} test
%{__make} test-sig

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}/keynote
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_mandir}/man3
install -d $RPM_BUILD_ROOT%{_mandir}/man4
install keynote $RPM_BUILD_ROOT%{_bindir}
cp libkeynote.a $RPM_BUILD_ROOT%{_libdir}
cp assertion.h keynote.h signature.h $RPM_BUILD_ROOT%{_includedir}/keynote
cp man/keynote.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp man/keynote.3 $RPM_BUILD_ROOT%{_mandir}/man3
cp man/keynote.4 $RPM_BUILD_ROOT%{_mandir}/man4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO doc/rfc2704.txt
%attr(0755,root,root) %{_bindir}/keynote
%{_includedir}/keynote/assertion.h
%{_includedir}/keynote/keynote.h
%{_includedir}/keynote/signature.h
%{_libdir}/libkeynote.a
%{_mandir}/man1/*.1.gz
%{_mandir}/man3/*.3.gz
%{_mandir}/man4/*.4.gz
