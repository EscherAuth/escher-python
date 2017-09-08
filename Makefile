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
	cp $(BUILDDIR)/signer/signer-linux-amd64.so $(DISTDIR)/escherauth_go/
	cp $(BUILDDIR)/signer/signer-darwin-10.10-amd64.dylib $(DISTDIR)/escherauth_go/
	cp $(BUILDDIR)/validator/escher_validator.py $(DISTDIR)/escherauth_go/
	cp $(BUILDDIR)/validator/validator-linux-amd64.so $(DISTDIR)/escherauth_go/
	cp $(BUILDDIR)/validator/validator-darwin-10.10-amd64.dylib $(DISTDIR)/escherauth_go/
	cp setup.py $(DISTDIR)/

build/signer:
	cd $(BUILDDIR)/signer && xgo -buildmode=c-shared -targets "linux/amd64,darwin-10.10/amd64" .
	

build/validator:
	cd $(BUILDDIR)/validator && xgo -buildmode=c-shared -targets "linux/amd64,darwin-10.10/amd64" .

build/wheel:
	cd $(DISTDIR) && python setup.py sdist

dist/wheel: build/wheel
	twine upload $(DISTDIR)/dist/*