#include "../include/rrgen.hpp"
#include <iostream>

int main(void)
{
    
  /* 
  rrgen::rrand<short, std::list, 5> rr;
  rr.generate_seedless_list(true, "bside");
  rr.show_contents();
  std::cout << '\n' << rr.xsize() << '\n';
  */
  /*
  rrgen::rrand_array<short, 5> rarray; 
  rarray.generate_seedless_array(true); 
  rarray.show_contents(); 
  std::cout << '\n' << rarray.xsize() << '\n';
  */

  rrgen::rrand_stack<short, 10> rstack;
  rstack.generate_seedless_stack(true);
  std::cout << "Current Stack Size: " << rstack.xsize() << '\n'; 
  rstack.push_top(444); 
  for (auto x = rstack.xsize(); x--;) {
    std::cout << rstack.grab_top() << '\n';
    rstack.pop_off();
    std::cout << "New size: " << rstack.xsize() << '\n';
    //std::cout << "Empty?: " << std::boolalpha << rstack.is_empty() << '\n';
    if (rstack.is_empty()) {
      throw rrgen::exception::rrgen_except("Stack is empty!\n");
    }
  }
  return 0;
}
