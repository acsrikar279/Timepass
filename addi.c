#include <stdio.h>
#include <stdarg.h>
double addi(int num,...) {
   va_list valist;
   double sum = 0.0;
   int i;
   va_start(valist, num);
if(num==0)
	return 0;
for (i = 0; i < num; i++) {
      sum += va_arg(valist, int);
   }
   va_end(valist);
   return sum;
}
int main() {
   printf("Sum = %f\n", addi());
   printf("Sum = %f\n", addi(1,2,3,4,5,6,7));
}
