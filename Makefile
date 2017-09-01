.PHONY: clean copy/src build build/signer build/validator copy/dist test build/wheel dist/wheel

BUILDDIR:=build
DISTDIR:=dist

clean:
	rm -rf $(BUILDDIR) $(DISTDIR)

clean/dist:
	rm -rf ${DISTDIR}

build: clean copy/src build/signer build/validator copy/dist test

test:
	PYTHONPATH=$(DISTDIR) python test/test_*.py

copy/src:
	mkdir $(BUILDDIR)
	cp -r signer validator $(BUILDDIR)

copy/dist:
	mkdir -p $(DISTDIR)/escherauth_go
	cp $(BUILDDIR)/signer/escher_signer.py $(DISTDIR)/escherauth_go/
	cp $(BUILDDIR)/signer/signer.so $(DISTDIR)/escherauth_go/
	cp $(BUILDDIR)/validator/escher_validator.py $(DISTDIR)/escherauth_go/
	cp $(BUILDDIR)/validator/validator.so $(DISTDIR)/escherauth_go/
	cp setup.py $(DISTDIR)/

build/signer:
	cd $(BUILDDIR)/signer && $ go build -buildmode=c-shared -o signer.so .

build/validator:
	cd $(BUILDDIR)/validator && $ go build -buildmode=c-shared -o validator.so .

build/wheel:
	cd $(DISTDIR) && python setup.py sdist

dist/wheel: build/wheel
	twine upload $(DISTDIR)/dist/*