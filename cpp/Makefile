CXX = g++
CXXFLAGS = -std=c++11 -Wall -I . -c 
CLLFLAGS = -std=c++11 -Wall -I . -O3 -fPIC -shared
LXXFLAGS = -std=c++11 -lboard
OBJECTS = board.o  main.o
LIBS = ../libboard.so
TARGET = main

$(TARGET): $(OBJECTS) $(LIBS)
	$(CXX) $(LXXFLAGS) -o $(TARGET) $(OBJECTS) $(GTEST)


main.o: main.cpp
	$(CXX) $(CXXFLAGS) ./main.cpp -o ./main.o

../libboard.so:board.cpp
	$(CXX) $(CLLFLAGS) board.cpp -o ../libboard.so



clean:
	rm -fv $(TARGET) $(OBJECTS) $(LIBS)