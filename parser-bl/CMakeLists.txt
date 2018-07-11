PROJECT(cnn:parser)
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

ADD_EXECUTABLE(lstm-parse-bl lstm-parse-bl.cc)
target_link_libraries(lstm-parse-bl cnn ${Boost_LIBRARIES})

