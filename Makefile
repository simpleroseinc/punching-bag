PYTHON := $(shell which python3)


.PHONY: pr
pr:
	@echo 'PR job is being RUN!!'


.PHONY: ci
ci:
	@echo 'CI JOB is being RUN!!'


.PHONY: binary-push
binary-push:
	@echo 'binary push'


.PHONY: version-bump-patch
version-bump-patch:
	$(PYTHON) cicd/versioning.py cicd/version.txt --patch > cicd/new_version.txt
	@mv cicd/new_version.txt cicd/version.txt

.PHONY: version-bump-minor
version-bump-minor:
	$(PYTHON) cicd/versioning.py cicd/version.txt --minor > cicd/new_version.txt
	@mv cicd/new_version.txt cicd/version.txt

.PHONY: version-bump-major
version-bump-major:
	$(PYTHON) cicd/versioning.py cicd/version.txt --major > cicd/new_version.txt
	@mv cicd/new_version.txt cicd/version.txt