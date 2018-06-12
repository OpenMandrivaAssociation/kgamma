%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		kgamma5
Summary:	Plasma 5 monitor calibration module
Version:	5.13.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xxf86vm)
Provides:	kgamma = 15.04.4
Obsoletes:	kgamma < 15.04.4

%description
Plasma 5 monitor calibration module.

%files -f kcmkgamma.lang
%dir %{_kde5_datadir}/kgamma
%dir %{_kde5_datadir}/kgamma/pics
%{_kde5_datadir}/kgamma/pics/*.png
%{_kde5_services}/kgamma.desktop
%{_qt5_plugindir}/kcm_kgamma.so

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kcmkgamma --all-name --with-html || touch kcmkgamma.lang
