.PHONY: maintainability coverage coverage-ci
maintainability:  ## run maintainability checks
	@radon cc --total-average -nB -s src

coverage:	## collect coverage data
	@pytest --doctest-modules --cov --cov-config=pyproject.toml --cov-branch --cov-report term --cov-report html:build/coverage
	@test -z "$(CI)" \
		&& ( echo "Opening 'build/coverage/index.html'..."; open build/coverage/index.html )\
		|| echo ""
coverage-ci:
	@CI=true $(MAKE) coverage
