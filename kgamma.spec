Name:		kgamma
Summary:	Color profiling
Version:	15.04.3
Release:	3
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(xxf86vm)
Conflicts:	okular < 2:4.6.4

%description
Adjust your monitor's gamma settings.

%files
%doc %{_kde_docdir}/HTML/*/kcontrol/%{name}
%{_kde_bindir}/xf86gammacfg
%{_kde_services}/%{name}.desktop
%{_kde_appsdir}/%{name}
%{_kde_libdir}/kde4/*_kgamma.*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

