#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Patricia
Summary:	Net::Patricia - Patricia Trie perl module for fast IP address lookups
#Summary(pl):	
Name:		perl-Net-Patricia
Version:	1.010
Release:	8
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	19f0c6944769daba64694ee3c72cf286
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module uses a Patricia Trie data structure to quickly perform IP
address prefix matching for applications such as IP subnet, network or
routing table lookups.

The data structure is based on a radix tree using a radix of two,
so sometimes you see patricia implementations called "radix" as well.
The term "Trie" is derived from the word "retrieval" but is pronounced
like "try".  Patricia stands for "Practical Algorithm to Retrieve
Information Coded as Alphanumeric", and was first suggested for routing
table lookups by Van Jacobsen.  Patricia Trie performance characteristics
are well-known as it has been employed for routing table lookups within
the BSD kernel since the 4.3 Reno release.

# %description -l pl
# TODO

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
