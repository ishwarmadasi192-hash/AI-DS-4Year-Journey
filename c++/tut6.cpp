#include<iostream>
/*there are 2 type of header file
1. system header file: it comes with the compiler
2.user define header file: it is written by programmer*/
//#include "this.h"//-> this will show error if this.h is not present in the current directory

using namespace std;
int main(){
    int a=4,b=5;
cout<<"Operators in c++: "<<endl;
cout<<"Following are the type of operator in c++:0"<<endl;
//Arithmatic operator
cout<<"The value of a+b is: "<<a+b<<endl;
cout<<"The value of a-b is: "<<a-b<<endl;
cout<<"The value of a*b is: "<<a*b<<endl;
cout<<"The value of a%b is: "<<a%b<<endl;
cout<<"The value of a/b is: "<<a/b<<endl;
cout<<"The value of a-- is: "<<a--<<endl;
cout<<"The value of a++ is: "<<a++<<endl;
cout<<"The value of --a is: "<<--a<<endl;
cout<<"The value of ++a is: "<<++a<<endl;
//Assignment operators -> used to assign values to variable
// int a=3,b=9;
// char d='d';

//Comparison __ARRAY_OPERATORS
cout<<"The value od a ==b is "<<(a==b)<<endl;
cout<<"The value od a <= b is "<<(a<=b)<<endl;
cout<<"The value od a >=b is "<<(a>=b)<<endl;
cout<<"The value od a !=b is "<<(a!=b)<<endl;
cout<<"The value od a <b is "<<(a<b)<<endl;
cout<<"The value od a >b is "<<(a>b)<<endl;

//Logical operators

    return 0;
}