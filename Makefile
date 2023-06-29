COPIER_ARGS?=--UNSAFE
COPIER_DEFAULT_VALUES?=-d "project_name=Sample Project" -d "package_name=sample_project" -d "user_name=mkj" --defaults

example: example-clean
	copier copy ${COPIER_ARGS} ${COPIER_DEFAULT_VALUES} . ./example
	$(MAKE) example-setup

example-manual: example-clean
	copier copy ${COPIER_ARGS} . ./example
	$(MAKE) example-setup

.PHONY: example-setup
example-setup:
	cd example &&\
		git add . &&\
		git commit -m "Initial commit" &&\
		pyenv local project-template-example &&\
		$(MAKE) install-dev &&\
		code --new-window .

.PHONY: example-push
example-push:
	cd example &&\
		git push -f -u origin main

.PHONY: example-clean
example-clean:
	rm -rf example && mkdir example

.PHONY: test
test:
	pytest -n 12
