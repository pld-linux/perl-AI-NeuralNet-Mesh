%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	NeuralNet-Mesh
Summary:	I::NeuralNet::Mesh - An optimized, accurate neural network Mesh.
Name:		perl-%{pdir}-%{pnam}
Version:	0.44
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.zip
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AI::NeuralNet::Mesh is an optimized, accurate neural network Mesh.
It was designed with accruacy and speed in mind.

This network model is very flexable.  It will allow for clasic binary
operation or any range of integer or floating-point inputs you care
to provide.  With this you can change activation types on a per node
or per layer basis (you can even include your own anonymous subs as
activation types).  You can add sigmoid transfer functions and control
the threshold.  You can learn data sets in batch, and load CSV data
set files.  You can do almost anything you need to with this module.
This code is deigned to be flexable.

# %description -l pl
# TODO

%prep
%setup -q -n %{name}-%{version} -c

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/AI/NeuralNet/*.pm
%doc Changes *.htm README
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.mesh
%{_examplesdir}/%{name}-%{version}/*.txt
%{_examplesdir}/%{name}-%{version}/*.dat
%{_examplesdir}/%{name}-%{version}/*.pcx
%{_mandir}/man3/*
