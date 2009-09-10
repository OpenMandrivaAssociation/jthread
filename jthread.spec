%define name jthread
%define version 1.2.1
%define release %mkrel 4
%define api %version
%define libname %mklibname %name %api
%define develname %mklibname -d %name

Summary: Make use of threads easy on different platforms
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://research.edm.uhasselt.be/jori/jthread/%{name}-%{version}.tar.bz2
License: MIT
Group: System/Libraries
Url: http://research.edm.uhasselt.be/~jori/page/index.php?n=CS.Jthread
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
The JThread package provides some classes to make use of threads easy
on different platforms. The classes are actually rather simple
wrappers around existing thread implementations.

%package -n %libname
Group:System/Libraries
Summary: Make use of threads easy on different platforms

%description -n %libname
The JThread package provides some classes to make use of threads easy
on different platforms. The classes are actually rather simple
wrappers around existing thread implementations.

%package -n %develname
Group: Development/C++
Summary: Make use of threads easy on different platforms
Requires: %libname = %version
Provides: lib%name-devel = %version-%release

%description -n %develname
The JThread package provides some classes to make use of threads easy
on different platforms. The classes are actually rather simple
wrappers around existing thread implementations.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%doc *.TXT
%_libdir/libjthread-%{api}.so

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog
%_includedir/jthread
%_libdir/pkgconfig/jthread.pc
%_libdir/libjthread.so
%_libdir/libjthread.a
%_libdir/libjthread.la
