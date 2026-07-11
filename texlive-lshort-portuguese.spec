%global tl_name lshort-portuguese
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.01.0
Release:	%{tl_revision}.1
Summary:	Introduction to LaTeX in Portuguese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/portuguese
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-portuguese.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-portuguese.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the Portuguese translation of A Short Introduction to LaTeX2e.

