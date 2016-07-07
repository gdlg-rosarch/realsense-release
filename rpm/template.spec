Name:           ros-indigo-realsense-camera
Version:        1.2.0
Release:        1%{?dist}
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
* Thu Jul 07 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-1
- Autogenerated by Bloom

* Thu Jun 30 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-0
- Autogenerated by Bloom

