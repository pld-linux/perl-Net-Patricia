#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Patricia
Summary:	Net::Patricia Perl module
Summary(cs):	Modul Net::Patricia pro Perl
Summary(da):	Perlmodul Net::Patricia
Summary(de):	Net::Patricia Perl Modul
Summary(es):	Módulo de Perl Net::Patricia
Summary(fr):	Module Perl Net::Patricia
Summary(it):	Modulo di Perl Net::Patricia
Summary(ja):	Net::Patricia Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Net::Patricia ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Net::Patricia
Summary(pl):	Modu³ Perla Net::Patricia
Summary(pt):	Módulo de Perl Net::Patricia
Summary(pt_BR):	Módulo Perl Net::Patricia
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Net::Patricia
Summary(sv):	Net::Patricia Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Net::Patricia
Summary(zh_CN):	Net::Patricia Perl Ä£¿é
Name:		perl-Net-Patricia
Version:	1.010
Release:	7
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	19f0c6944769daba64694ee3c72cf286
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Patricia - Patricia Trie perl module for fast IP address lookups.

%description -l cs
Modul Net::Patricia pro Perl.

%description -l da
Perlmodul Net::Patricia.

%description -l de
Net::Patricia Perl Modul.

%description -l es
Módulo de Perl Net::Patricia.

%description -l fr
Module Perl Net::Patricia.

%description -l it
Modulo di Perl Net::Patricia.

%description -l ja
Net::Patricia Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Net::Patricia ÆÞ ¸ðÁÙ.

%description -l nb
Perlmodul Net::Patricia.

%description -l pl
Modu³ perla Net::Patricia.

%description -l pt
Módulo de Perl Net::Patricia.

%description -l pt_BR
Módulo Perl Net::Patricia.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Net::Patricia.

%description -l sv
Net::Patricia Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Net::Patricia.

%description -l zh_CN
Net::Patricia Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/*.pm
%dir %{perl_vendorarch}/auto/Net/Patricia
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Patricia/Patricia.so
%{_mandir}/man3/*
