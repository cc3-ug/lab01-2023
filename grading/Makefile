CC=gcc
EFLAGS=-D TEST
CFLAGS=-Wall -Itests/include -fPIC -std=c99



test_eccentric: test_eccentric.c
	$(CC) $(EFLAGS) -o $@ $?



EX2_SRC=\
	ex2/flip_bit.c \
	ex2/get_bit.c \
	ex2/set_bit.c \
	tests/bit_ops_test.c

EX3_SRC=\
	ex3/lfsr_calculate.c \
	tests/lfsr_test.c

EX2_CONV_SRC=$(EX2_SRC:.c=_conv.c)
EX3_CONV_SRC=$(EX3_SRC:.c=_conv.c)
CONV=$(EX2_CONV_SRC) $(EX3_CONV_SRC)

EX2_OBJ=$(EX2_SRC:.c=.o)
EX3_OBJ=$(EX3_SRC:.c=.o)
OBJ=$(EX2_OBJ) $(EX3_OBJ)

bit_ops: $(EX2_OBJ)
	$(CC) $(CFLAGS) -o $@ $?

lfsr: $(EX3_OBJ)
	$(CC) $(CFLAGS) -o $@ $?

$(OBJ): %.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

$(CONV): %_conv.c: %.c
	$(CC) $(CFLAGS) -Itests/fake -E $< > $@




.PHONY: clean

clean:
	rm -f $(OBJ) $(CONV) bit_ops lfsr *.expected test_eccentric.c test_eccentric eccentric
	rm -rf grading/__pycache__/
