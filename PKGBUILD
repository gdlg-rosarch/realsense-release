# Script generated with Bloom
pkgdesc="ROS - RealSense Camera package allowing access to Intel 3D cameras and advanced modules"
url='http://www.ros.org/wiki/RealSense'

pkgname='ros-kinetic-realsense-camera'
pkgver='1.8.1_2'
pkgrel=1
arch=('any')
license=('BSD 3-clause. See license attached'
)

makedepends=('boost'
'ros-kinetic-camera-info-manager'
'ros-kinetic-catkin'
'ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-image-transport'
'ros-kinetic-librealsense>=1.12.1'
'ros-kinetic-message-generation'
'ros-kinetic-nodelet'
'ros-kinetic-pcl-ros'
'ros-kinetic-roscpp'
'ros-kinetic-roslint'
'ros-kinetic-rostest'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

depends=('boost'
'ros-kinetic-camera-info-manager'
'ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-image-transport'
'ros-kinetic-librealsense'
'ros-kinetic-message-generation'
'ros-kinetic-message-runtime'
'ros-kinetic-nodelet'
'ros-kinetic-pcl-ros'
'ros-kinetic-rgbd-launch'
'ros-kinetic-roscpp'
'ros-kinetic-rostest'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=realsense_camera
source=()
md5sums=()

prepare() {
    cp -R $startdir/realsense_camera $srcdir/realsense_camera
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

