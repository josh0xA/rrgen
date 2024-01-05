# rrgen - A Header Only C++ Library For Storing Safe, Randomly Generated Data Into Modern Containers 

<p align="center">
    <a href="https://lbesson.mit-license.org/" target="_blank"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="lisence" /></a>
</p>

## About
This library was developed to combat insecure methods of storing random data into modern C++ containers. For example, old and clunky PRNGs. Thus, rrgen uses STL's distribution engines in order to efficiently and safely store a random number distribution into a given C++ container. 

## Installation
1) ``git clone https://github.com/josh0xA/rrgen.git`` <br/>
2) ``cd rrgen``<br/>
3) ``make``<br/>
4) Add ``include/rrgen.hpp`` to your project tree for access to the library classes and functions.<br/>

## Official Documentation
https://rrgen.readthedocs.io/

## Supported Containers
1) ``std::vector<Type> (std::size_t)``<br/>
2) ``std::list<Type> (std::size_t)``<br/>
3) ``std::array<Type, std::size_t>``<br/>
4) ``std::stack<Type, std::size_t>``<br/>

## Example Usage (#1)
```cpp
#include "include/rrgen.hpp"
#include <iostream>

int main(void) {
  rrgen::rrand<short, std::vector, 10> rvector; // Create vector container (size=10) containing integers
  rvector.gen_rrvector(true); // Fill the vector with a secure random distribution of integers
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
  rarray.gen_rrarray(true);
  rarray.show_contents();
  std::cout << "\nSize: " << rarray.xsize() << '\n';

}

void handle_stack() {
  rrgen::rrand_stack<uint32_t, 12> rstack; 
  rstack.gen_rrstack(true); 
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
...
Current Stack Size: 0
terminate called after throwing an instance of 'rrgen::exception::rrgen_except'
  what():  Stack is empty!

```

## License 
MIT License <br/>
Copyright (c) Josh Schiavone 
