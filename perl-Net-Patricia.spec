%include	/usr/lib/rpm/macros.perl
Summary:	Net-Patricia perl module
Summary(pl):	Modu� perla Net-Patricia
Name:		perl-Net-Patricia
Version:	1.010
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/authors/id/P/PL/PLONKA/Net-Patricia-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Patricia - Patricia Trie perl module for fast IP address lookups.

%description -l pl
Modu� perla Net-Patricia.

%prep
%setup -q -n Net-Patricia-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Net/*.pm
%attr(755,root,root) %{perl_sitearch}/auto/Net/Patricia/Patricia.so
%{_mandir}/man3/*
