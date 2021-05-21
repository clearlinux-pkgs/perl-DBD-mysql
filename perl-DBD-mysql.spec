#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBD-mysql
Version  : 4.050
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/D/DV/DVEEDEN/DBD-mysql-4.050.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DV/DVEEDEN/DBD-mysql-4.050.tar.gz
Summary  : 'A MySQL driver for the Perl5 Database Interface (DBI)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-DBD-mysql-license = %{version}-%{release}
Requires: perl-DBD-mysql-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : mariadb-dev
BuildRequires : openssl-dev
BuildRequires : perl(DBI::DBD)
BuildRequires : perl(Devel::CheckLib)
BuildRequires : perl(Test::Deep)

%description
# DBD::mysql - database driver for Perl
This is the Perl [DBI](https://metacpan.org/pod/DBI) driver for access to MySQL databases.

%package dev
Summary: dev components for the perl-DBD-mysql package.
Group: Development
Provides: perl-DBD-mysql-devel = %{version}-%{release}
Requires: perl-DBD-mysql = %{version}-%{release}

%description dev
dev components for the perl-DBD-mysql package.


%package license
Summary: license components for the perl-DBD-mysql package.
Group: Default

%description license
license components for the perl-DBD-mysql package.


%package perl
Summary: perl components for the perl-DBD-mysql package.
Group: Default
Requires: perl-DBD-mysql = %{version}-%{release}

%description perl
perl components for the perl-DBD-mysql package.


%prep
%setup -q -n DBD-mysql-4.050
cd %{_builddir}/DBD-mysql-4.050

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DBD-mysql
cp %{_builddir}/DBD-mysql-4.050/LICENSE %{buildroot}/usr/share/package-licenses/perl-DBD-mysql/8f2a398dbb6085cfe3fd321d4e97475224b71dc7
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Bundle::DBD::mysql.3
/usr/share/man/man3/DBD::mysql.3
/usr/share/man/man3/DBD::mysql::INSTALL.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DBD-mysql/8f2a398dbb6085cfe3fd321d4e97475224b71dc7

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Bundle/DBD/mysql.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DBD/mysql.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DBD/mysql/GetInfo.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DBD/mysql/INSTALL.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/DBD/mysql/mysql.so
