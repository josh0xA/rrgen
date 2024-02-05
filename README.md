# rrgen - A Header Only C++ Library For Storing Safe, Randomly Generated Data Into Modern Containers 
<p align="center">
    <img src="https://raw.githubusercontent.com/josh0xA/rrgen/master/docs/rrgen_logo.png"/></a>
</p>
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
*rrgen/docs/index.rst*

## Supported Containers
1) ``std::vector<>``<br/>
2) ``std::list<>``<br/>
3) ``std::array<>``<br/>
4) ``std::stack<>``<br/>

## Example Usages
```cpp
#include "../include/rrgen.hpp"
#include <iostream>

int main(void)
{
    // Example usage for rrgen vector
    rrgen::rrand<float, std::vector, 10> rrvec;
    rrvec.gen_rrvector(false, true, 0, 10);
    for (auto &i : rrvec.contents())
    {
        std::cout << i << " ";
    } // ^ the same as rrvec.show_contents()

    // Example usage for rrgen list (frontside insertion)
    rrgen::rrand<int, std::list, 10> rrlist;
    rrlist.gen_rrlist(false, true, "fside", 5, 25);
    std::cout << '\n'; rrlist.show_contents();
    std::cout << "Size: " << rrlist.contents().size() << '\n';

    // Example usage for rrgen array
    rrgen::rrand_array<int, 5> rrarr;
    rrarr.gen_rrarray(false, true, 5, 35);
    for (auto &i : rrarr.contents())
    {
        std::cout << i << " ";
    } // ^ the same as rrarr.show_contents()

    // Example usage for rrgen stack 
    rrgen::rrand_stack<float, 10> rrstack;
    rrstack.gen_rrstack(false, true, 200, 1000);
    for (auto m = rrstack.xsize(); m > 0; m--)
    {
        std::cout << rrstack.grab_top() << " ";
        rrstack.pop_off();
        if (m == 1) { std::cout << '\n'; }
    } 
}

``
Note: This is a transferred repository, from a completely unrelated project. 

## License 
MIT License <br/>
Copyright (c) Josh Schiavone 
