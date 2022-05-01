cmake_minimum_required(VERSION 3.10)

project(infra_red)


if(NOT CMAKE_BUILD_TYPE)
	set(CMAKE_BUILD_TYPE Release)
endif()
include_directories("/usr/local/include/opencv4")
set(CMAKE_CXX_FLAGS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")
set(CMAKE_C_FLAGS "-lusb-1.0")
set(CMAKE_CXX_FLAGS "-pthread")
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
find_package(OpenCV 4.5.4 REQUIRED)
include_directories(.)
link_directories(~/IRNDT_ws/src)
file(GLOB_RECURSE CXX_SRC
	"~/IRNDT_ws/src/*.hpp"
	"~/IRNDT_ws/src/*.cpp"
)
file(GLOB_RECURSE C_SRC "~/IRNDT_ws/src/*.h"  "~/IRNDT_ws/src/*.c")
#add_library(${PROJECT_NAME}  thermometry.h pot.h SimplePictureProcessing.h function.cpp Usb.h Usb.cpp )
add_executable(infra_red main.cpp Usb.cpp function.cpp Usb.h)
target_link_libraries(${PROJECT_NAME}
	PUBLIC
	${catkin_LIBRARIES}
	${OpenCV_LIBRARIES}
	Simple
	pot
	thermometry
	usb-1.0
)
