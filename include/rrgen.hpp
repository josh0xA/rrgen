/*
MIT License

Copyright (c) 2024 Josh Schiavone

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
  /**
   * @brief For universal conditional use if true
   * @param bool, value to test
   * @return bool
   */
  inline bool rrgen_success_on_return_value(bool __svalue) {
    
    return (__svalue == true);
  }

  inline bool rrgen_error_on_return_value(bool __svalue) {
    /**
     * @brief For universal conditional use if false
     * @param bool, value to test
     * @return bool
     */
    return (__svalue == false);
  }
  
  typedef struct __modes__ {
    /**
     * @brief Library structure for setting modes for list generations
     * through std::random engines
     */
    __cchar* RRGEN_FRONTSIDE_MODE = "fside"; 
    __cchar* RRGEN_BACKSIDE_MODE = "bside";
  } modes, *pmodes; 
  
  /**
   * @brief Nested template class rrand. 
   * @class Usage for std::vector and std::list generations
   * @format rrand<typename, template<typename, typename>, std::size_t>
   */
  template <typename rand_type, template <typename, typename> class Arg, std::size_t __datasize>
  class rrand {
  protected:
    template <typename T = rand_type>
    std::enable_if_t<std::is_integral_v<T>, std::uniform_int_distribution<T>>
    gen_random_data_numeric(const std::mt19937 __mtgenerator) {
      std::uniform_int_distribution<T> distribution(
        std::numeric_limits<T>::min(),
        std::numeric_limits<T>::max());
      return distribution;
    }

    template <typename T = rand_type>
    std::enable_if_t<std::is_floating_point_v<T>, std::uniform_real_distribution<T>>
    gen_random_data_numeric(const std::mt19937 __mtgenerator) {
      std::uniform_real_distribution<T> distribution(
        std::numeric_limits<T>::min(),
        std::numeric_limits<T>::max());
      return distribution;
    }

    template <typename T = rand_type>
    std::enable_if_t<std::is_integral_v<T>, std::uniform_int_distribution<T>>
    gen_random_data_mm(const std::mt19937 __mtgenerator, T __min, T __max) {
      std::uniform_int_distribution<T> distribution(__min, __max);
      return distribution;
    }

    template <typename T = rand_type>
    std::enable_if_t<std::is_floating_point_v<T>, std::uniform_real_distribution<T>>
    gen_random_data_mm(const std::mt19937 __mtgenerator, T __min, T __max) {
      std::uniform_real_distribution<T> distribution(__min, __max);
      return distribution;
    }

    modes mds;
  public:
    /**
     * @brief Randomly generates data and stores the values into a vector
     * @param bool, must be true in order to generate data
     * @return Arg<rand_type, std::allocator<rand_type>> - data container
     */
    Arg<rand_type, std::allocator<rand_type>> gen_rrvector(bool numeric, bool minmax, 
      rand_type __min = 0, rand_type __max = 100) {
      std::mt19937 __mtgenerator(__device());
      if (rrgen_success_on_return_value(numeric)) {
        auto dist = gen_random_data_numeric(__mtgenerator);
        for (auto elem = RRGEN_SUCCESS_CODE_STANDARD; elem < __datasize; ++elem) {
          struct_container.push_back(dist(__mtgenerator));
        }
        return struct_container;
      } else { 
          if (rrgen_success_on_return_value(minmax)) {
            auto dist = gen_random_data_mm(__mtgenerator, __min, __max);
            for (auto elem = RRGEN_SUCCESS_CODE_STANDARD; elem < __datasize; ++elem) {
              struct_container.push_back(dist(__mtgenerator));
            }
            return struct_container;
          } else { return struct_container; }
      }
    }
    /**
    * @brief Randomly generates data and stores the values into a list
    * @param bool - must be true in order to generate data, std::string - push
    * direction
    * @return Arg<rand_type, std::allocator<rand_type>> - data container
    */
    Arg<rand_type, std::allocator<rand_type>> gen_rrlist(bool numeric, bool minmax, 
        const std::string& direction, rand_type __min = 0, rand_type __max = 100) {
      std::mt19937 __mtgenerator(__device()); 
      if (rrgen_success_on_return_value(numeric)) {
        auto dist = gen_random_data_numeric(__mtgenerator);
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
      } else { 
          if (rrgen_success_on_return_value(minmax)) {
            auto dist = gen_random_data_mm(__mtgenerator, __min, __max);
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
    }

    Arg<rand_type, std::allocator<rand_type>> contents() const {
      return struct_container;
    }

    rand_type show_contents() const {
      /**
       * @brief Prints the data stored in the container
       * @param void 
       * @return typename (rand_type)
       */
      for (const rand_type& content : struct_container) {
        std::cout << content << " "; 
      }
    }
    
    rand_type xsize() const {
      /**
       * @brief Returns the size of the container
       * @param void
       * @return typename (rand_type)
       */
      return struct_container.size();
    }

    void delete_contents() {
      /**
       * @brief Deletes all of the stored data in the container
       * @param void
       * @return void
       */
      struct_container.clear(); 
    }
   
  private:
    Arg<rand_type, std::allocator<rand_type>> struct_container; 
    std::random_device __device;  
  }; // class: rrand

  /**
   * @brief Template class rrand_array
   * @class Usage for generating random uniform data for std::array
   * @format rrand_array<typename, std::size_t> 
   */
  template <typename rand_type, std::size_t __datasize>
  class rrand_array {
  protected:
    /**
     * @brief Creates a uniform distribution of random numbers in the range of 
     * std::numeric_limits<type>::min() -> std::numeric_limits<type>::max()
     * @param std::mt19937, uniform generation engine
     * @return std::unirom_int_distribution<type>
     */
    template <typename T = rand_type>
    std::enable_if_t<std::is_integral_v<T>, std::uniform_int_distribution<T>>
    gen_random_data(const std::mt19937 __mtgenerator) {
      std::uniform_int_distribution<T> distribution(
        std::numeric_limits<T>::min(),
        std::numeric_limits<T>::max());
      return distribution;
    }

    template <typename T = rand_type>
    std::enable_if_t<std::is_floating_point_v<T>, std::uniform_real_distribution<T>>
    gen_random_data(const std::mt19937 __mtgenerator) {
      std::uniform_real_distribution<T> distribution(
        std::numeric_limits<T>::min(),
        std::numeric_limits<T>::max());
      return distribution;
    }

    template <typename T = rand_type>
    std::enable_if_t<std::is_integral_v<T>, std::uniform_int_distribution<T>>
    gen_random_data_mm(const std::mt19937 __mtgenerator, T __min, T __max) {
      std::uniform_int_distribution<T> distribution(__min, __max);
      return distribution;
    }

    template <typename T = rand_type>
    std::enable_if_t<std::is_floating_point_v<T>, std::uniform_real_distribution<T>>
    gen_random_data_mm(const std::mt19937 __mtgenerator, T __min, T __max) {
      std::uniform_real_distribution<T> distribution(__min, __max);
      return distribution;
    }

  public:
    /**
     * @brief Generates random uniform data and stores values into std::array
     * container
     * @param bool, must be true in order for generation to occur
     * @return std::array<typename, std::size_t>
     */
    std::array<rand_type, __datasize> gen_rrarray(bool numeric, bool minmax, rand_type __min = 0, rand_type __max = 100) {
      std::mt19937 __mtgenerator(__device());
      if (rrgen_success_on_return_value(numeric)) {
        auto dist = gen_random_data(__mtgenerator);
        for (auto elem = RRGEN_SUCCESS_CODE_STANDARD; elem < __datasize; ++elem) {
          array_container.at(elem) = dist(__mtgenerator);
        }
        return array_container; 
      } else { 
          if (rrgen_success_on_return_value(minmax)) {
            auto dist = gen_random_data_mm(__mtgenerator, __min, __max);
            for (auto elem = RRGEN_SUCCESS_CODE_STANDARD; elem < __datasize; ++elem) {
              array_container.at(elem) = dist(__mtgenerator);
            }
            return array_container; 
          } else { return array_container; }
      }
    }

    std::array<rand_type, __datasize> contents() const {
      return array_container;
    }
    
    rand_type show_contents() const {
      /**
       * @brief Iterates array contents and outputs the data stored
       * @param void
       * @return typename (rand_type)
       */
      for (const auto& content : array_container) {
        std::cout << content << " "; 
      }
    }
    /**
     * @brief Returns size of array container
     * @param void
     * @return typename (rand_tpe)
     */
    rand_type xsize() const  { return array_container.size(); }

       
  private:
    std::random_device __device; 
    std::array<rand_type, __datasize> array_container; 
  }; // class: rrand_array

  /**
   * @brief Inherited Template class rrand_stack 
   * @class Usage for generating random uniform data for std::stack
   * @format rrand_stack<typename, std::size_t> 
   */
  template <typename rand_type, std::size_t __datasize>
  class rrand_stack : protected rrand_array<rand_type, __datasize> {
  public:
    std::stack<rand_type> gen_rrstack(bool numeric, bool minmax, rand_type __min = 0, rand_type __max = 100) {
      std::mt19937 __mtgenerator(__device());
      if (rrgen_success_on_return_value(numeric)) {
        auto dist = rrand_array<rand_type, __datasize>::gen_random_data(__mtgenerator);
        for (auto elem = RRGEN_SUCCESS_CODE_STANDARD; elem < __datasize; ++elem) {
          stack_container.push(dist(__mtgenerator));
        }
        return stack_container; 
      } else { 
          if (rrgen_success_on_return_value(minmax)) {
            auto dist = rrand_array<rand_type, __datasize>::gen_random_data_mm(__mtgenerator, __min, __max);
            for (auto elem = RRGEN_SUCCESS_CODE_STANDARD; elem < __datasize; ++elem) {
              stack_container.push(dist(__mtgenerator));
            }
            return stack_container; 
          } else { return stack_container; }
      }
    }

    std::stack<rand_type> contents() const {
      return stack_container;
    }
    
    constexpr bool is_empty() const noexcept {
      /**
       * @brief returns whether or not the stack is empty
       * @param void
       * @return bool 
       */
      return stack_container.empty(); 
    }

    rand_type grab_top() const {
      /**
       * @brief returns the element at the top of the stack
       * @param void
       * @return typename (rand_type)
       */
      return stack_container.top();
    }
    
    void push_top(rand_type value) {
      /**
       * @brief pushes argument to the top of the stack container
       * @param typename (rand_type) - element/value to push 
       * @return void
       */
      stack_container.push(value);
    }

    rand_type xsize() const {
      /**
       * @brief returns the size of the stack container (# of elements)
       * @param void
       * @return typename (rand_type)
       */
      return stack_container.size();
    }

    void pop_off() {
      /**
       * @brief pops the top element off of the stack container
       * @param void
       * @return void
       */
      stack_container.pop();
    }
  
  private:
    std::random_device __device; 
    std::stack<rand_type> stack_container;
  }; // class: rrand_stack

  namespace exception {
    /**
    * @brief rrgen exception class - inherits fron stdexcept
    * Used to throw exceptions rather than std::cerr
    */
    class rrgen_except : public std::exception {
    public:
      /**
       * @brief Constructor - sets error strings
       * @class rrgen_except
       */
      rrgen_except(const char* const message) : __errmessage__{message} {};
      /**
       * @brief returns the error message 
       * @param void
       * @return const char*
       */
      const char* what() const noexcept { return __errmessage__; }
    private:
      const char* __errmessage__;      

    }; // class: rrgen_except 

  } // namespace: exception
  

} // namespace: rrgen 


#endif 
