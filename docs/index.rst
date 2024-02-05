rrgen - A Header Only C++ Library For Storing Safe, Randomly Generated Data Into Modern Containers
==================================================================================================

About
=====
This library was developed to combat unsecure methods of storing random data into modern C++ containers. 

Documentation
=============
Namespace: rrgen


Structures

    struct __modes__: Library structure for setting modes for list generations through std::random engines.

Classes
Class: rrand

The rrand class provides tools for generating random data and storing it in vectors, lists, and arrays.
Methods

    gen_rrvector(bool numeric, bool minmax, rand_type __min = 0, rand_type __max = 100): Randomly generates data and stores it in a vector.
    gen_rrlist(bool numeric, bool minmax, const std::string& direction, rand_type __min = 0, rand_type __max = 100): Randomly generates data and stores it in a list.
    contents() const: Returns the data container.
    show_contents() const: Prints the data stored in the container.
    xsize() const: Returns the size of the container.
    delete_contents(): Deletes all stored data in the container.

Class: rrand_array

The rrand_array class inherits from rrand and provides additional tools for generating random data in arrays.
Methods

    gen_rrarray(bool numeric, bool minmax, rand_type __min = 0, rand_type __max = 100): Generates random uniform data and stores values in an array.
    contents() const: Returns the array container.
    show_contents() const: Iterates array contents and outputs the stored data.
    xsize() const: Returns the size of the array container.

Class: rrand_stack

The rrand_stack class inherits from rrand_array and provides additional tools for generating random data in stacks.
Methods

    gen_rrstack(bool numeric, bool minmax, rand_type __min = 0, rand_type __max = 100): Generates random uniform data and stores values in a stack.
    contents() const: Returns the stack container.
    is_empty() const noexcept: Returns true if the stack is empty.
    grab_top() const: Returns the element at the top of the stack.
    push_top(rand_type value): Pushes an element to the top of the stack.
    xsize() const: Returns the size of the stack container.
    pop_off(): Pops the top element off the stack.

Namespace: exception
Class: rrgen_except

The rrgen_except class inherits from std::exception and is used to throw exceptions instead of using std::cerr.
Methods

    what() const noexcept: Returns the error message.