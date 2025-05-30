cmake_minimum_required(VERSION 3.10)

project(libaudioresource)

# Shared library version
set(MAJOR_VERSION "1")
set(MINOR_VERSION "0")
set(PATCH_VERSION "0")
set(VERSION "${MAJOR_VERSION}.${MINOR_VERSION}.${PATCH_VERSION}")
set(VERSION_SONAME "${MAJOR_VERSION}")

# Implementation backend dependencies: libresource
find_package(PkgConfig)
pkg_check_modules(LIBRESOURCE_GLIB REQUIRED libresource-glib)
include_directories(${LIBRESOURCE_GLIB_INCLUDE_DIRS})

# pkg-config support
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/pkgconfig/audioresource.pc.in
    ${CMAKE_CURRENT_BINARY_DIR}/audioresource.pc
    @ONLY)

# Shared library
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
add_library(audioresource SHARED src/audioresource.c)
target_link_libraries(audioresource ${LIBRESOURCE_GLIB_LIBRARIES})
set_target_properties(audioresource PROPERTIES VERSION ${VERSION} SOVERSION ${VERSION_SONAME})

# Installation
install(TARGETS audioresource LIBRARY DESTINATION ${LIB_DEST})
install(FILES include/audioresource.h DESTINATION include/audioresource)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/audioresource.pc DESTINATION ${LIB_DEST}/pkgconfig)
