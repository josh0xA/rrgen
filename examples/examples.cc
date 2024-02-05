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
