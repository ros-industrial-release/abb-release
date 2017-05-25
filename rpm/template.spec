Name:           ros-kinetic-abb
Version:        1.3.0
Release:        0%{?dist}
Summary:        ROS abb package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/abb
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-abb-driver
Requires:       ros-kinetic-abb-irb2400-moveit-config
Requires:       ros-kinetic-abb-irb2400-moveit-plugins
Requires:       ros-kinetic-abb-irb2400-support
Requires:       ros-kinetic-abb-irb4400-support
Requires:       ros-kinetic-abb-irb5400-support
Requires:       ros-kinetic-abb-irb6600-support
Requires:       ros-kinetic-abb-irb6640-moveit-config
Requires:       ros-kinetic-abb-irb6640-support
Requires:       ros-kinetic-abb-resources
BuildRequires:  ros-kinetic-catkin

%description
ROS-Industrial support for ABB manipulators (metapackage).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu May 25 2017 Shaun Edwards <shaun.edwards@gmail.com> - 1.3.0-0
- Autogenerated by Bloom

