/*
MIT License

Copyright (c) 2021 Josh Schiavone

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

#ifndef RRGEN_HPP
#define RRGEN_HPP

#include <random>
#include <algorithm>
#include <exception>
#include <string>

#include <vector>
#include <array>
#include <stack>
#include <list>
#include <iostream>

#define RRGEN_ERROR_CODE_STANDARD -1
#define RRGEN_SUCCESS_CODE_STANDARD 0 

/**
 * @brief debugging preprocessor - set a fatal type to a debug
 * value
 */
#define RRGEN_SET_VALUE(k_value, s_value) ((k_value) = (s_value))

typedef const char __cchar; 

namespace rrgen {
  inline bool rrgen_success_on_return_value(bool __svalue) {
    
    return (__svalue == true);
  }
  inline bool rrgen_error_on_return_value(bool __svalue) {
    return (__svalue == false);
  }
  
  constexpr unsigned int str_to_integer(const char* str, int hdx = 0) {
    return !str[hdx] ? 5381 : (str_to_integer(str, hdx+1) * 33) ^ str[hdx];
  }

  typedef struct __modes__ {
    __cchar* RRGEN_FRONTSIDE_MODE = "fside"; 
    __cchar* RRGEN_BACKSIDE_MODE = "bside";
  } modes, *pmodes; 

  template <typename rand_type, template <typename, typename> class Arg, std::size_t __datasize>
  class rrand {
  protected:
    std::uniform_int_distribution<rand_type> gen_random_data(const std::mt19937 __mtgenerator) {
      std::uniform_int_distribution<rand_type> distribution(
        std::numeric_limits<rand_type>::min(),
        std::numeric_limits<rand_type>::max());
      return distribution;
    }
    modes mds;
  public:
    Arg<rand_type, std::allocator<rand_type>> generate_seedless_vector(bool gen) {
      std::mt19937 __mtgenerator(__device());
      if (rrgen_success_on_return_value(gen)) {
        auto dist = gen_random_data(__mtgenerator);
        for (auto elem = RRGEN_SUCCESS_CODE_STANDARD; elem < __datasize; ++elem) {
          struct_container.push_back(dist(__mtgenerator));
        }
        return struct_container;
      } else { return struct_container; }
    }
    
    Arg<rand_type, std::allocator<rand_type>> generate_seedless_list(bool gen, const std::string& direction) {
      std::mt19937 __mtgenerator(__device()); 
      if (rrgen_success_on_return_value(gen)) {
        auto dist = gen_random_data(__mtgenerator);
        if (rrgen_success_on_return_value(direction.compare(mds.RRGEN_FRONTSIDE_MODE))) { 
            for (auto elem = RRGEN_SUCCESS_CODE_STANDARD; elem < __datasize; ++elem) {
              struct_container.push_front(dist(__mtgenerator));
            }
        } 
        if (rrgen_success_on_return_value(direction.compare(mds.RRGEN_BACKSIDE_MODE))) {
           for (auto elem = RRGEN_SUCCESS_CODE_STANDARD; elem < __datasize; ++elem) {
              struct_container.push_back(dist(__mtgenerator));
            }
        }
        return struct_container; 
      } else { return struct_container; }
    }

    rand_type show_contents() const {
      for (const rand_type& content : struct_container) {
        std::cout << content << " "; 
      }
    }
    
    rand_type xsize() const {
      return struct_container.size();
    }

    void delete_contents() {
      struct_container.clear(); 
    }
   
  private:
    Arg<rand_type, std::allocator<rand_type>> struct_container; 
    std::random_device __device;  
  }; // class: rrand

  template <typename rand_type, std::size_t __datasize>
  class rrand_array {
  protected:
    std::uniform_int_distribution<rand_type> gen_random_data(const std::mt19937 __mtgenerator) {
      std::uniform_int_distribution<rand_type> distribution(
        std::numeric_limits<rand_type>::min(),
        std::numeric_limits<rand_type>::max());
      return distribution;
    }
  public:
    std::array<rand_type, __datasize> generate_seedless_array(bool gen) {
      std::mt19937 __mtgenerator(__device());
      if (rrgen_success_on_return_value(gen)) {
        auto dist = gen_random_data(__mtgenerator);
        for (auto elem = RRGEN_SUCCESS_CODE_STANDARD; elem < __datasize; ++elem) {
          array_container.at(elem) = dist(__mtgenerator);
        }
        return array_container; 
      } else { return array_container; }
    }
    
    rand_type show_contents() const {
      for (const auto& content : array_container) {
        std::cout << content << " "; 
      }
    }
    
    rand_type xsize() const  { return array_container.size(); }
       
  private:
    std::random_device __device; 
    std::array<rand_type, __datasize> array_container; 
  }; // class: rrand_array

  template <typename rand_type, std::size_t __datasize>
  class rrand_stack : protected rrand_array<rand_type, __datasize> {
  public:
    std::stack<rand_type> generate_seedless_stack(bool gen) {
      std::mt19937 __mtgenerator(__device());
      if (rrgen_success_on_return_value(gen)) {
        auto dist = rrand_array<rand_type, __datasize>::gen_random_data(__mtgenerator);
        for (auto elem = RRGEN_SUCCESS_CODE_STANDARD; elem < __datasize; ++elem) {
          stack_container.push(dist(__mtgenerator));
        }
        return stack_container; 
      } else { return stack_container; }
    }
    
    constexpr bool is_empty() const noexcept {
      return stack_container.empty(); 
    }

    rand_type grab_top() const {
      return stack_container.top();
    }
    
    void push_top(rand_type value) {
      stack_container.push(value);
    }

    rand_type xsize() const {
      return stack_container.size();
    }

    void pop_off() {
      stack_container.pop();
    }
  
  private:
    std::random_device __device; 
    std::stack<rand_type> stack_container;
  }; // class: rrand_stack

  namespace exception {
    /**
    * @brief rrgen exception class
    * Used to throw exceptions rather than std::cerr
    */
    class rrgen_except : public std::exception {
    public:
      rrgen_except(const char* const message) : __errmessage__{message} {};

      const char* what() const noexcept { return __errmessage__; }
    private:
      const char* __errmessage__;      

    }; // class: rrgen_except 

  } // namespace: exception
  

} // namespace: rrgen 


#endif 
