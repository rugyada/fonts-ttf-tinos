Name:		fonts-ttf-tinos
Version:	1.0
Release:	1
Summary:	Tinos ttf fonts
License:	Apache License v2.00
Group:		System/Fonts/True type
Url:		https://www.ascenderfonts.com/
Source0:	%{name}-%version.tar.gz
BuildArch:	noarch

%description
Tinos is a typeface which is metrics compatible with Times New Roman.

%files
%dir %{_datadir}/fonts/TTF/tinos/
%{_datadir}/fonts/TTF/tinos/*

%prep
%setup -qn %{name}-%{version}/fonts/TTF/tinos/

%build
#

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/tinos
install -Dm 644  *.ttf  %{buildroot}%{_datadir}/fonts/TTF/tinos/
