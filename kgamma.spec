Name: kgamma
Summary: kgamma color profiling
Version: 4.7.97
Release: 1
Epoch: 2
Group: Graphical desktop/KDE
License: GPLv2
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
Conflicts:     okular < 2:4.6.4

%description
Adjust your monitor's gamma settings.

%files
%_kde_bindir/xf86gammacfg
%_kde_services/%name.desktop
%_kde_appsdir/%name
%_kde_libdir/kde4/*_kgamma.*
%doc %_kde_docdir/HTML/*/kcontrol/%name

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

