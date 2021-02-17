# rrgen - A Header Only C++ Library For Storing Safe, Randomly Generated Data Into Modern Containers 

<p align="center" 
  <img src="https://github.com/josh0xA/rrgen/blob/main/docs/rrgen_logo.png?raw=true">
</p>

## About
This library was developed to combat unsecure methods of storing random data into modern C++ containers. For example, pseudorandom number generators. Thus, rrgen uses STL's seedless distribution engines in order to efficiently and safely store a random number distribution into a certain C++ container. 

## Official Documentation
https://rrgen.readthedocs.io/

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
### Possible Output
```
28153 29568 15744 -22325 -21678 -26256 -23805 -30591 2896 30121
```
## Example Usage (#2)
```cpp
#include "include/rrgen.hpp"
#include <iostream>

void handle_array() {
  rrgen::rrand_array<int, 5> rarray;
  rarray.generate_seedless_array(true);
  rarray.show_contents();
  std::cout << "\nSize: " << rarray.xsize() << '\n';

}

void handle_stack() {
  rrgen::rrand_stack<uint32_t, 12> rstack; 
  rstack.generate_seedless_stack(true); 
  std::cout << "Current Stack Size: " << rstack.xsize() << '\n';
  
  for (auto m = rstack.xsize(); m--;) {
    std::cout << rstack.grab_top() << '\n';
    rstack.pop_off();
    std::cout << "Current Stack Size: " << rstack.xsize() << '\n';
    
    if (rstack.is_empty()) {
      throw rrgen::exception::rrgen_except("Stack is empty!\n");
    }

  }
}

int main(void) {
  handle_array();
  handle_stack();
   
  return 0;
}
```

### Possible Output (handle_array())
```
-2008733701 1821221292 165435652 896912942 850256910 
Size: 5
```
### Possible Output (handle_stack())
```
Current Stack Size: 12
3701296188
Current Stack Size: 11
2208611429
Current Stack Size: 10
3326656092
Current Stack Size: 9
532142802
Current Stack Size: 8
2978594177
Current Stack Size: 7
1103941808
Current Stack Size: 6
1883298880
Current Stack Size: 5
2425042044
Current Stack Size: 4
2458856231
Current Stack Size: 3
480226278
Current Stack Size: 2
719366412
Current Stack Size: 1
1481043649
Current Stack Size: 0
terminate called after throwing an instance of 'rrgen::exception::rrgen_except'
  what():  Stack is empty!

```
- Note: Traversing a stack (even an rstack) is not very smart and it is very reduntant as it takes away from the main purpose of the containter. Only showing for development purposes.

## The Problem With std::rand() and other PRNGs
First, rand is a pseudorandom number generator. This means it depends on a seed. For a given seed it will always give the same sequence (assuming the same implementation). This makes it not suitable for certain applications where security is of a great concern. But this is not specific to rand. It's a problem of any pseudo-random generator. A true random generator has its own problems (efficiency, implementation, entropy) so for problems that are not security related most often a pseudo-random generator is used.

- One problem is that it has a global state (set by srand). This makes it impossible to use multiple random engines at the same time. It also greatly complicates multithreaded tasks.

## License 
MIT License <br/>
Copyright (c) Josh Schiavone 
