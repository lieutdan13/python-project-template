.PHONY: install
install-dev:	## install development dependencies
	pip install -e .[test,doc,dev]

.PHONY: maintainability
maintainability:  ## run maintainability checks
	@radon cc --total-average -nB -s src

.PHONY: coverage coverage-ci
coverage:	## collect coverage data
	@pytest --doctest-modules --cov --cov-config=pyproject.toml --cov-branch --cov-report term --cov-report html:build/coverage
	@test -z "$(CI)" \
		&& ( echo "Opening 'build/coverage/index.html'..."; open build/coverage/index.html )\
		|| echo ""
coverage-ci:
	@CI=true $(MAKE) coverage

DOCS_TARGET?=build/docs
.PHONY: docs
docs:	## build documentation
	mkdocs build --site-dir ${DOCS_TARGET}
