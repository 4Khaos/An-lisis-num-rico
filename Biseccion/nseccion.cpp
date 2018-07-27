#include <iostream>
#include <iomanip> // setprecision
#include <cmath>

#define precision 8
#define intervalos 10
#define GRAVEDAD 9.8

using namespace std;

double func(double c);
void valores_intervalo (double a, double b);


int main () {

    cout << setprecision(precision);

    double a, b, sec, root;
    double pr;
    int cont = 0;

    cout << " a: ";
    cin >> a;

    cout << " b = ";
    cin >> b;

    cout << "\nDivisiones: ";
    cin >> sec;




    // EN BISECCION
    if (func(a) * func(b) > 0)
    {

        cout << "\nRango no valido \n";
        cout << " f(" << a << ") y f(" << b << ") tienen el mismo signo" << endl;

    }


    else
    {

        cout << "\nprecision = ";
        cin >> pr;
        cout << "\na\tb\traiz \n" << endl;

        do {
        //Valor absoluto
         root = abs((a - b))/sec;
         root+= a;
         cout << setw(20) << "\t" << a << "\t" << b << "\t" << root << endl;


         if (abs(func(root)) <= pr) {

             cout << "\n\n" << "la raiz de f es: " << root << endl;
             break;
          }
          else
            {
                if (func(root) * func(a) > 0)
                {
                    a = root;
                }
                else if (func(root) * func(b) > 0)
                {
                    b = root;
                }
            }

           cont++;

        } while (1);


    }

    cout << "\n" << cont << " iteraciones. " <<endl;
      // Tabla de valores
      valores_intervalo(a,b);


}

double func(double c)
{
    double m = 68.1;
    double n1 = GRAVEDAD*m/c;
    double n2 = -(c/68.1)*10;
    // Funcion tomada como referencia
    return (n1*(1-pow(M_E,n2))-40);
}


// Funcion que evalua el coeficiente de arrastre en la formula (Grafica)

void valores_intervalo (double a, double b)
{
    int puntos = intervalos + 1;

    double x = (b - a) / intervalos;

    cout << "\n";
    cout << "\tx\tf(x)\n" << endl;
    for (int i = 0; i < puntos; i++)
    {
        cout << "\t" << a << "\t" << func(a) << endl;
        a = a + x;
    }

}
