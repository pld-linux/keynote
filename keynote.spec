%define kversion 2.1
%define release 1

Summary:	Trust management system
Name:		keynote
Version:	%{kversion}
Release:	%{release}
Copyright:	BSD
Group:		System Environment/Libraries
Source0:	http://www.cis.upenn.edu/~angelos/Code/keynote-%{kversion}.tar.gz
BuildRoot:	/tmp/keynote-%{kversion}-root
Packager:	Damien Miller <djm@mindrot.org>

%changelog
* Thu Oct 21 1999 Damien Miller <djm@mindrot.org>
- v2.1
- Fixed parameterisation of version

* Sun Oct 03 1999 Damien Miller <djm@mindrot.org>
- Built RPM

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

%setup

%build
./configure --prefix=/usr
make crypto CFLAGS="-Wall $RPM_OPT_FLAGS"

make test
make test-sig

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib
mkdir -p $RPM_BUILD_ROOT/usr/include/keynote
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/man/man3
mkdir -p $RPM_BUILD_ROOT/usr/man/man4
install keynote $RPM_BUILD_ROOT/usr/bin
cp libkeynote.a $RPM_BUILD_ROOT/usr/lib
cp assertion.h keynote.h signature.h $RPM_BUILD_ROOT/usr/include/keynote
cp man/keynote.1 $RPM_BUILD_ROOT/usr/man/man1
cp man/keynote.3 $RPM_BUILD_ROOT/usr/man/man3
cp man/keynote.4 $RPM_BUILD_ROOT/usr/man/man4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc LICENSE README TODO doc/rfc2704.txt
%attr(0755,root,root) /usr/bin/keynote
/usr/include/keynote/assertion.h
/usr/include/keynote/keynote.h
/usr/include/keynote/signature.h
/usr/lib/libkeynote.a
/usr/man/man1/keynote.1
/usr/man/man3/keynote.3
/usr/man/man4/keynote.4
