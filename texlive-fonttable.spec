%global tl_name fonttable
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6e
Release:	%{tl_revision}.1
Summary:	Print font tables from a LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fonttable
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fonttable.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fonttable.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fonttable.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a package version of nfssfont.tex (part of the LaTeX
distribution); it enables you to print a table of the characters of a
font and/or some text (for demonstration or testing purposes), from
within a document. (Packages such as testfont and nfssfont.tex provide
these facilities, but they run as interactive programs: the user is
expected to type details of what is needed.) Note that the package
mftinc also has a \fonttable function; the documentation explains how
avoid a clash with that package.

