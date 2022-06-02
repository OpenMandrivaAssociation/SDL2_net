%define major 0
%define api 2.0
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} -d

Summary:	Simple DirectMedia Layer 2 - network
Name:		SDL2_net
Version:	2.0.1
Release:	3
License:	ZLib
Group:		System/Libraries
Url:		http://www.libsdl.org/projects/SDL_net/
Source0:	http://www.libsdl.org/projects/SDL_net/release/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(sdl2)

%description
This is a small sample cross-platform networking library.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files -n %{devname}
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/SDL2/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install
