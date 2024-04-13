#include<iostream>
using namespace std;

bool checkDivisible(int x, int* array,int size){
    for (int i = 0; i < size; i++){
        if (x%array[i] == 0){
            return true;
        }
    }
    return false;
}

int* primeNo(int x){
    if(x < 1){
        return nullptr;
    }
    int* prime = new int[x];
    int size = 0;
    prime[size++] = 2;

    for (int i = 3; true; i = i+2){
        if (size == x){
            return prime;
        }
        if (!checkDivisible(i, prime, size)){
            prime[size++] = i;
        }        
    }
}

int main(){
    int num = 10000;
    int* array = primeNo(num);
    for (int i = 0; i < num; i++)
    {
        cout<<array[i]<<", ";
    }
    
}