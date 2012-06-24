Summary:	Trust management system
Summary(pl):	System zarz�dzania zaufaniem
Name:		keynote
Version:	2.3
Release:	2
License:	BSD
Group:		Applications/System
Source0:	http://www.cis.upenn.edu/~angelos/Code/%{name}-%{version}.tar.gz
# Source0-md5:	ba58a0297c421dc6aa671e6b753ef695
URL:		http://www.cis.upenn.edu/~angelos/keynote.html
BuildRequires:	automake
BuildRequires:	autoconf
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

%description -l pl
KeyNode to prosty i elastyczny system zarz�dzania zaufaniem
zaprojektowany tak, by dobrze dzia�a� z wieloma du�ej i ma�ej skali
aplikacjami internetowymi. Zapewnia jeden, zunifikowany j�zyk dla
lokalnych polis i uwierzytelnie�. Polisy i uwierzytelnienia KeyNode,
zwane zapewnieniami (assertions) zawieraj� orzeczenia opisuj�ce
zaufane czynno�ci, kt�re mog� by� podejmowane przez posiadaczy
specyficznych kluczy publicznych. Zapewnienia KeyNode to zasadniczo
ma�e, wysoko strukturalne programy. Podpisane zapewnienie, kt�re mo�e
by� wys�ane przez sie�, kt�rej nie ufamy, s� nazywane te�
potwierdzeniami uwierzytelnie� (credential assertions). Mog� one
pe�ni� rol� certyfikat�w, maj� t� sam� sk�adni� co potwierdzenia
polis, ale s� podpisane tak�e przez jednostk� nadrz�dn� deleguj�c�
dane uprawnienie.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure \
	--prefix=%{_prefix}

%{__make} crypto CFLAGS="-Wall %{rpmcflags}"

%{__make} test
%{__make} test-sig

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/keynote} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3,4}

install keynote $RPM_BUILD_ROOT%{_bindir}
install libkeynote.a $RPM_BUILD_ROOT%{_libdir}
install assertion.h keynote.h signature.h $RPM_BUILD_ROOT%{_includedir}/keynote
install man/keynote.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/keynote.3 $RPM_BUILD_ROOT%{_mandir}/man3
install man/keynote.4 $RPM_BUILD_ROOT%{_mandir}/man4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO doc/rfc2704.txt
%attr(755,root,root) %{_bindir}/keynote
%dir %{_includedir}/keynote
%{_includedir}/keynote/assertion.h
%{_includedir}/keynote/keynote.h
%{_includedir}/keynote/signature.h
%{_libdir}/libkeynote.a
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_mandir}/man4/*.4*
