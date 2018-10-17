.PHONY: clean copy/src build build/signer build/validator copy/dist test build/wheel dist/wheel

BUILD_TARGETS=linux/amd64,darwin-10.11/amd64
BUILD_GO_VERSION=1.11.1
BUILDDIR:=build
DISTDIR:=dist

clean:
	rm -rf $(BUILDDIR) $(DISTDIR)

build: clean copy/src build/signer build/validator copy/dist test

test:
	PYTHONPATH=$(DISTDIR) python test/test_*.py

copy/src:
	mkdir -p $(BUILDDIR)
	cp -r src $(BUILDDIR)

copy/dist:
	mkdir -p $(DISTDIR)/escherauth_go/go
	cp $(BUILDDIR)/src/*.py \
		 setup.py \
		 $(DISTDIR)/escherauth_go/
	cp $(wildcard $(BUILDDIR)/src/go/**/*.so) \
		 $(wildcard $(BUILDDIR)/src/go/**/*.dylib) \
		 $(DISTDIR)/escherauth_go/go/

build/signer:
	cd $(BUILDDIR)/src/go/signer && GOPATH=$(PWD)/build xgo -go $(BUILD_GO_VERSION) -buildmode=c-shared -ldflags "-s -w" -targets $(BUILD_TARGETS) ./

build/validator:
	cd $(BUILDDIR)/src/go/validator && GOPATH=$(PWD)/build xgo -go $(BUILD_GO_VERSION) -buildmode=c-shared -ldflags "-s -w" -targets $(BUILD_TARGETS) ./

build/wheel:
	cd $(DISTDIR) && TARGET=linux/amd64 python setup.py sdist

dist/wheel: build/wheel
	twine upload $(DISTDIR)/dist/*