Name: libaudioresource
Version: 1.0.8
Release: 1
Summary: Nemo Mobile Audio Resource API
License: LGPLv2
URL: https://github.com/sailfishos/libaudioresource
Source: %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(libresource-glib)
BuildRequires: cmake
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
This library provides a way to acquire audio resources for playback on Nemo
Mobile and Sailfish, as well as a way to get notified when audio resources
have been released, in which case audio playback must be stopped.

%package devel
Summary: Development library for %{name}
Requires: %{name} = %{version}

%description devel
This package contains the development library for %{name}.

%prep
%autosetup

%build
%cmake -DLIB_DEST=%{_lib}
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/%{name}.so.*
%license COPYING.LGPL

%files devel
%doc README
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/audioresource.pc
%{_includedir}/audioresource/audioresource.h
