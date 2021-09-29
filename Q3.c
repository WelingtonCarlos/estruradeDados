#include<stdio.h>
int main()
{
 int numero, guarda_maior, guarda_menor;
 int i;
 int x = 0;
 int y = 0;

 printf("Entre com o 1o numero inteiro: ");
 scanf("%i", &numero);

 guarda_maior=numero;
 guarda_menor=numero;

 for(i=1; i<5; i++)
 {
 printf("\nEntre com o %do numero inteiro: ",i+1);
 scanf("%i", &numero);

 if(numero>guarda_maior){
    guarda_maior=numero;
    x = x + 1;
 }
 else
 if(numero<guarda_menor)
    guarda_menor=numero;
    y = y + 1;
 }


 printf("\nO menor numero entrado e: %d", guarda_menor);
 printf(" e ele aparareceu %d vezes", x );
 printf("\nO maior numero entrado e: %d", guarda_maior);
 printf(" e ele aparareceu %d vezes", y );

 getch();
}
