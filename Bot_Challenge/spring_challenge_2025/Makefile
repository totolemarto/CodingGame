CC=gcc
CFLAGS= -g

OBJS = $(patsubst %.c,%.o,$(FILE))
all:main 

%.o: %.c
	$(CC) $(CFLAGS) -c $<

main: $(OBJS)
	echo $(OBJS)
	$(CC) $(CFLAGS) -o $@ $<

gprof:
	$(CC) $(CFLAGS) -pg -c $(FILE) 
	$(CC) $(CFLAGS) -pg -o main $(OBJS)
	./main  $(ARGS)
	gprof ./main


clean:
	rm main *.o
