Name:           ros-indigo-realsense-camera
Version:        1.6.0
Release:        0%{?dist}
Summary:        ROS realsense_camera package

Group:          Development/Libraries
License:        BSD 3-clause. See license attached
URL:            http://www.ros.org/wiki/RealSense
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-camera-info-manager
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-librealsense
Requires:       ros-indigo-message-generation
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-rgbd-launch
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rostest
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-camera-info-manager
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-librealsense >= 0.9.2
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf

%description
RealSense Camera package allowing access to Intel 3D cameras and advanced
modules

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Oct 28 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.6.0-0
- Autogenerated by Bloom

* Thu Sep 29 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.5.0-0
- Autogenerated by Bloom

* Thu Aug 25 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.4.0-0
- Autogenerated by Bloom

* Thu Jul 28 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.3.0-0
- Autogenerated by Bloom

* Wed Jul 13 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.1-0
- Autogenerated by Bloom

* Wed Jul 13 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-17
- Autogenerated by Bloom

* Fri Jul 08 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-16
- Autogenerated by Bloom

* Fri Jul 08 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-15
- Autogenerated by Bloom

* Fri Jul 08 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-14
- Autogenerated by Bloom

* Fri Jul 08 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-13
- Autogenerated by Bloom

* Fri Jul 08 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-12
- Autogenerated by Bloom

* Fri Jul 08 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-11
- Autogenerated by Bloom

* Fri Jul 08 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-10
- Autogenerated by Bloom

* Fri Jul 08 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-9
- Autogenerated by Bloom

* Fri Jul 08 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-8
- Autogenerated by Bloom

* Fri Jul 08 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-7
- Autogenerated by Bloom

* Thu Jul 07 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-6
- Autogenerated by Bloom

* Thu Jul 07 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-5
- Autogenerated by Bloom

* Thu Jul 07 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-4
- Autogenerated by Bloom

* Thu Jul 07 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-3
- Autogenerated by Bloom

* Thu Jul 07 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-2
- Autogenerated by Bloom

* Thu Jul 07 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-1
- Autogenerated by Bloom

* Thu Jun 30 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-0
- Autogenerated by Bloom

