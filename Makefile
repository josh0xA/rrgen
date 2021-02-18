all: include/rrgen.hpp
	g++ -std=c++14 -march=native -o rrgen.so include/rrgen.hpp

clean:
	$(RM) rrgen.so 

