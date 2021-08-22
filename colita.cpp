#include<iostream>

#include <string>

using namespace std;

class nodo
{

public:
    nodo(int, string);
    string nombre;
    int edad;

    nodo *Next;
};

nodo::nodo(int _edad, string _nombre)
{
    edad = _edad;
    nombre = _nombre;

    this->Next = NULL;
};

class Cola{

private:
  

public:
    nodo *adelante;
    nodo *atras;
    int length;

    void encolar( int edad, string nombre );
    void desencolar();
    void imprimir();
};

void Cola::encolar(int _edad,string _nombre){
    nodo  *newNodo =  new nodo(_edad, _nombre);

    if(length == 0){
        adelante = newNodo;
        atras = newNodo;
    }else{
        atras->Next =newNodo;
        atras = newNodo;
    }

    length++;
};

void Cola::imprimir(){
       nodo *aux;

        aux = adelante;

        while(aux != NULL){
               cout<<"Mi nombre es: "<< aux->nombre <<" y mi edad "<<aux->edad<<endl ;
            aux = aux->Next;
        }
};



void Cola::desencolar(){
    if(!adelante){
        
    }
    if (adelante == atras){
        adelante = NULL;
    }
    adelante = adelante->Next;
    length--;
}

int main(){

    Cola colita = Cola();

    colita.encolar(23,"alexis");
    
    colita.encolar(12,"valery");
    colita.encolar(43,"alfredo");
    colita.desencolar();
    colita.desencolar();
    colita.imprimir();

    return 0;

}