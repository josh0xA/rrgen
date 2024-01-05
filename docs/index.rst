rrgen - A Header Only C++ Library For Storing Safe, Randomly Generated Data Into Modern Containers
==================================================================================================

About
=====
This library was developed to combat unsecure methods of storing random data into modern C++ containers. For example, pseudorandom number generators. Thus, rrgen uses STL's seedless distribution engines in order to efficiently and safely store a random number distribution into a certain C++ container.

Documentation
=============
Namespaces:
  | ``rrgen::``
  | ``rrgen::exception``
Classes:
  | ``rrgen::rrand<typename, template <typename, typename> class Arg, std::size_t __datasize>``
  | ``rrgen::rrand_array<typename, std::size_t __datasize>``
  | ``rrgen::rrand_stack<typename, std::size_t __datasize>``

Functions: 
  | ``rrgen::rrand<>`` 
  |     public: ``generate_rrvector(bool gen)`` This function uses STL's random distribution engine's in order to safely and securely generate random data between the numeric limits of a type. This data is then stored in the vector. Args:bool: If true, will add data to vector. If not, no data will be added.  
  |     public: ``generate_rrlist(bool gen, const std::string& direction)`` This function uses STL's random distribution engine's in order to safely and securely generate random data between the numeric limits of a type. This data is then stored in the list. Args:bool: If true, will add data to list. If not, no data will be added. Args:const std::string&: Push data from the front or the back. Supported: "fside" & "bside". 
  
