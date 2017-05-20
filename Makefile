PWD=$(pwd)

clean:
	python setup.py clean
	rm -rf *.so *.o *.html mmh3object.cpp

build: clean
	# gcc -c MurmurHash3.cpp
	# gcc -shared -o libMurmurHash3.so MurmurHash3.o
	# python setup.py build_ext --inplace -v
	venv/bin/cython -a mmh3object.pyx -I.
	python setup.py build
	cp build/lib*/*.so ./

test: build
	venv/bin/python test.py

virtualenv:
	rm -rf venv
	virtualenv --python=python2.7 venv
	venv/bin/pip install -r requirements.txt
