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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is the Portuguese translation of A Short Introduction to
LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-portuguese/pt-lshort-5.01.0.src.tar.gz
%doc %{_texmfdistdir}/doc/latex/lshort-portuguese/pt-lshort.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
