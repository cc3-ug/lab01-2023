int concat_bits(unsigned x, unsigned len_x, unsigned y, unsigned len_y) {

  // YOUR CODE HERE
  // In this exercise you are allowed to use
  // if, while, for
  // but you don't really need them

  x = (x << (32 - len_x)) >> (32 - len_x);
  y = (y << (32 - len_y)) >> (32 - len_y);

  x = x << (len_y);

  int res = x | y;
  res = (res << (32 - len_x - len_y)) >> (32 - len_x - len_y);

  return res;

}
