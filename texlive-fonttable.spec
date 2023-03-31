Name:		texlive-fonttable
Version:	44799
Release:	2
Summary:	Print font tables from a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fonttable
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonttable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonttable.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonttable.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a package version of nfssfont.tex (part of the LaTeX
distribution); it enables you to print a table of the
characters of a font and/or some text (for demonstration or
testing purposes), from within a document. (Packages such as
testfont and nfssfont.tex provide these facilities, but they
run as interactive programs: the user is expected to type
details of what is needed.) Note that the package mftinc also
has a \fonttable function; the documentation explains how avoid
a clash with that package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fonttable
%doc %{_texmfdistdir}/doc/latex/fonttable
#- source
%doc %{_texmfdistdir}/source/latex/fonttable

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
