# rrgen - A Header Only C++ Library For Storing Safe Randomly Generated Data In Modern Containers 

## About
This library was developed to combat unsecure methods of storing random data into modern C++ containers. For example, pseudorandom number generators. Thus, rrgen uses STL's seedless distribution engines in order to efficiently and safely store a random number distribution into a certain C++ container. 

## Supported Containers
1) ``std::vector<Type> (std::size_t)``<br/>
2) ``std::list<Type> (std::size_t)``<br/>
3) ``std::array<Type, std::size_t>``<br/>
4) ``std::stack<Type>``<br/>

## Example Usage (#1)
```cpp
#include "include/rrgen.hpp"
#include <iostream>

int main(void) {
  rrgen::rrand<short, std::vector, 10> rvector; // Create vector container (size=10) containing integers
  rvector.generate_seedless_vector(true); // Fill the vector with a secure random distribution of integers
  rvector.show_contents();
}

```
### Output
```
28153 29568 15744 -22325 -21678 -26256 -23805 -30591 2896 30121
```


## The Problem With std::rand() and other PRNGs
First, rand is a pseudorandom number generator. This means it depends on a seed. For a given seed it will always give the same sequence (assuming the same implementation). This makes it not suitable for certain applications where security is of a great concern. But this is not specific to rand. It's a problem of any pseudo-random generator. A true random generator has its own problems (efficiency, implementation, entropy) so for problems that are not security related most often a pseudo-random generator is used.

- One problem is that it has a global state (set by srand). This makes it impossible to use multiple random engines at the same time. It also greatly complicates multithreaded tasks.

## License 
MIT License <br/>
Copyright (c) Josh Schiavone 
