#include "concat_bits.h"

void test_concat_bits(unsigned x, unsigned len_x, unsigned y, unsigned len_y, unsigned expected) {
  unsigned res = concat_bits(x, len_x, y, len_y);
  if(res != expected) {
    printf("concat_bits(0x%08x, %u, 0x%08x, %u): 0x%08x, expected 0x%08x\n", x, len_x, y, len_y, res, expected);
  } else {
    printf("concat_bits(0x%08x, %u, 0x%08x, %u): 0x%08x, correct\n", x, len_x, y, len_y, res);
  }
}

int main(int argc, const char * argv[]) {
  test_concat_bits(0x00000044, 8, 0x000000cc, 8, 0x000044cc);
  test_concat_bits(0x00000044, 4, 0x000000cc, 4, 0x0000004c);
  test_concat_bits(0x000000cc, 8, 0x00000044, 8, 0xffffcc44);
  test_concat_bits(0x000000cc, 4, 0x00000044, 4, 0xffffffc4);
  test_concat_bits(0x000000aa, 8, 0x0000cccc, 16, 0xffaacccc);
  test_concat_bits(0x00000066, 6, 0xfffffccc, 10, 0xffff98cc);
  test_concat_bits(0x87654321, 12, 0x12345678, 12, 0x00321678);
  test_concat_bits(0x87654321, 16, 0x12345678, 16, 0x43215678);
  printf("\n");
  return 0;
}
