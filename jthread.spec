%define libname %mklibname %{name} %{version}
%define devname %mklibname -d %{name}

Name:		jthread
Version:	1.3.1
Release:	1
Summary:	Make use of threads easy on different platforms
Group:		System/Libraries
License:	MIT
Url:		http://research.edm.uhasselt.be/~jori/page/index.php?n=CS.Jthread
Source:		http://research.edm.uhasselt.be/jori/jthread/%{name}-%{version}.tar.bz2
BuildRequires:	cmake

%description
The JThread package provides some classes to make use of threads easy
on different platforms. The classes are actually rather simple
wrappers around existing thread implementations.

%package -n %{libname}
Group:		System/Libraries
Summary:	Make use of threads easy on different platforms
Obsoletes:	%{mklibname jthread 1.2.1} < %{EVRD}

%description -n %{libname}
The JThread package provides some classes to make use of threads easy
on different platforms. The classes are actually rather simple
wrappers around existing thread implementations.

%package -n %{devname}
Group:		Development/C++
Summary:	Make use of threads easy on different platforms
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
The JThread package provides some classes to make use of threads easy
on different platforms. The classes are actually rather simple
wrappers around existing thread implementations.


%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%doc *.TXT
%{_libdir}/libjthread.so.%{version}

%files -n %{devname}
%doc ChangeLog
%{_includedir}/jthread
%{_libdir}/cmake/JThread
%{_libdir}/pkgconfig/jthread.pc
%{_libdir}/libjthread.so
%{_libdir}/libjthread.a


%changelog
* Thu Jul 26 2012 Andrey Bondrov <abondrov@mandriva.org> 1.3.1-1
+ Revision: 811131
- New version 1.3.1, new library major, switch to cmake

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Sep 06 2007 Götz Waschk <waschk@mandriva.org> 1.2.1-1mdv2008.0
+ Revision: 80954
- Import jthread



* Thu Sep  6 2007 Götz Waschk <waschk@mandriva.org> 1.2.1-1mdv2008.0
- initial package
