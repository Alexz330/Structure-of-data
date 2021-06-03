// const array = ["Diego", "Karen", "Osacar"]


// se crea una clase para El array creado por nosotros
class MyArray{
    //Este es el constructor de nuestro array
    constructor(){
        // this.length esta la variable que nos servira para identificar el tamaño de nuestro arra
        // y tambien para saber cual es la posicion en la que se encuentra nuestro objeto
        this.length = 0;
        this.data = {}
    }

    // el metodo get que recibe como parametro el index del elemento, nos servira para saber la posicion en la lista de nuestro objeto 
    get(index){
        return this.data[index]
    }
    // el metodo push que recibe como parametro el elemento  para poder almacenarlo en el array 
    push(item){
        
        this.data[this.length] = item;
        this.length++;
        return this.data;
    }
    // el metodo pop nos sirve para eliminar el ultimo elemento del array
    pop(){

        const lastItem = this.data[this.length-1];
        delete this.data[this.length-1];
        
        return lastItem

    }
    // el medetodo myDelete recibe como parametro el index del elemento para poder eliminar dicho elemento del array
    myDelete(index){

        const item = this.data[index]
        // se hace referencia al metodo ShiftIndex para eleminar el elemento que coincida con el index de dicho elemento
        this.shiftIndex(index);
        return item;
    }

    // el metodo shiftIndex, funciona para eleminar un elemento en especifico y reacomoda el array
    shiftIndex(index){
        for(let i = index; i<this.length-1; i++ ){
            this.data[i] = this.data[i+1]
            
        }
        
        delete this.data[this.length - 1];
        this.length --;
    }
    // metodo para eleminar el primer elemento del array

    eliminarPrimerELemento(){
        
        const firstItem = this.data[0];       
        this.shiftIndex(0)
        return firstItem;
    }


    

}


const arreglito = new  MyArray();

