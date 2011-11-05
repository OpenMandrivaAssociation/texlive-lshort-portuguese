# revision 22569
# category Package
# catalog-ctan /info/lshort/portuguese
# catalog-date 2011-05-22 11:03:26 +0200
# catalog-license pd
# catalog-version 5.01.0
Name:		texlive-lshort-portuguese
Version:	5.01.0
Release:	1
Summary:	Introduction to LaTeX in Portuguese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/portuguese
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-portuguese.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-portuguese.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is the Portuguese translation of A Short Introduction to
LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-portuguese/pt-lshort-5.01.0.src.tar.gz
%doc %{_texmfdistdir}/doc/latex/lshort-portuguese/pt-lshort.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
