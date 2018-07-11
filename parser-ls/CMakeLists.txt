PROJECT(cnn:parser)
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

ADD_EXECUTABLE(lstm-parse-ls lstm-parse-ls.cc)
target_link_libraries(lstm-parse-ls cnn ${Boost_LIBRARIES})

