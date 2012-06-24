%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Patricia
Summary:	Net::Patricia Perl module
Summary(cs):	Modul Net::Patricia pro Perl
Summary(da):	Perlmodul Net::Patricia
Summary(de):	Net::Patricia Perl Modul
Summary(es):	M�dulo de Perl Net::Patricia
Summary(fr):	Module Perl Net::Patricia
Summary(it):	Modulo di Perl Net::Patricia
Summary(ja):	Net::Patricia Perl �⥸�塼��
Summary(ko):	Net::Patricia �� ����
Summary(no):	Perlmodul Net::Patricia
Summary(pl):	Modu� Perla Net::Patricia
Summary(pt):	M�dulo de Perl Net::Patricia
Summary(pt_BR):	M�dulo Perl Net::Patricia
Summary(ru):	������ ��� Perl Net::Patricia
Summary(sv):	Net::Patricia Perlmodul
Summary(uk):	������ ��� Perl Net::Patricia
Summary(zh_CN):	Net::Patricia Perl ģ��
Name:		perl-Net-Patricia
Version:	1.010
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildRequires:	perl-devel
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
M�dulo de Perl Net::Patricia.

%description -l fr
Module Perl Net::Patricia.

%description -l it
Modulo di Perl Net::Patricia.

%description -l ja
Net::Patricia Perl �⥸�塼��

%description -l ko
Net::Patricia �� ����.

%description -l no
Perlmodul Net::Patricia.

%description -l pl
Modu� perla Net::Patricia.

%description -l pt
M�dulo de Perl Net::Patricia.

%description -l pt_BR
M�dulo Perl Net::Patricia.

%description -l ru
������ ��� Perl Net::Patricia.

%description -l sv
Net::Patricia Perlmodul.

%description -l uk
������ ��� Perl Net::Patricia.

%description -l zh_CN
Net::Patricia Perl ģ��

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Net/*.pm
%dir %{perl_sitearch}/auto/Net/Patricia
%attr(755,root,root) %{perl_sitearch}/auto/Net/Patricia/Patricia.so
%{_mandir}/man3/*
