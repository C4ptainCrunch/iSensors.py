all:
	gcc -shared -o libsmc.so -fPIC smc.c -framework IOKit -framework CoreFoundation

clean:
	@rm -r libsmc.so