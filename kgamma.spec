%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name:		kgamma
Summary:	Plasma 6 monitor calibration module
Version:	6.4.4
Release:	%{?git:0.%{git}.}2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kgamma/-/archive/%{gitbranch}/kgamma-%{gitbranchd}.tar.bz2#/kgamma5-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/kgamma-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	gettext
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed 2025-04-27 after 6.0
%rename plasma6-kgamma
# Let's get rid of 5.x cruft
Obsoletes: kgamma5 < %{EVRD}

%description
Plasma 6 monitor calibration module.

%files -f %{name}.lang
%dir %{_datadir}/kgamma
%dir %{_datadir}/kgamma/pics
%{_datadir}/kgamma/pics/*.png
%{_qtdir}/plugins/plasma/kcminit/kcm_kgamma_init.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kgamma.so
%{_datadir}/applications/kcm_kgamma.desktop
