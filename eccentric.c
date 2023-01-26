#include <stdio.h>

/* Only change any of these 4 values */
#define V0 0
#define V1 -1
#define V2 0
#define V3 0

// DO NOT EDIT BELOW THIS LINE

#ifndef TEST
int main(void) {
  int a;
  char *s;

  /* This is a print statement. Notice the little 'f' at the end!
  It might be worthwhile to look up how printf works for your future
  debugging needs... */
  printf("Welcome to C:\n====================\n");

  /* for loop */
  for (a=0; a<V0; a++) {
    printf("Hola ");
  }
  printf("\n");

  /* switch statement */
  switch (V1) {
    case 0:   printf("Luis\n");
    case 1:   printf("Diego\n");     break;
    case 2:   printf("Jose Pablo\n");
    case 3:   printf("Luis\n");           break;
    case 4:   printf("Adrian\n");      break;
    case 5:   printf("Ali\n");
    default:  printf("Me perdi...\n");
  }

  /* ternary operator */
  s = (V3==3) ? "El gato dice" : "El perro dice";

  /* if statement */
  if (V2) {
    printf("\n%s miau\n", s);
  } else  {
    printf("\n%s pio\n", s);
  }

  return 0;
}
#endif
