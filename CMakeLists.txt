cmake_minimum_required(VERSION 3.5)
project(aartfaac_imager_simulator)

find_package(Boost REQUIRED COMPONENTS system)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(aartfaac_imager_simulator ${SOURCE_FILES})
target_link_libraries(aartfaac_imager_simulator ${Boost_LIBRARIES} casa_images casa_casa casa_lattices casa_fits)