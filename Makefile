#!/usr/bin/env make -f

SOURCE_FILES=../hl7conv

lint:
	@isort --check --diff --project=hl7conv ${SOURCE_FILES}
	@black --check --diff ${SOURCE_FILES}
	@flake8 ${SOURCE_FILES}
	@mypy ${SOURCE_FILES}
	@safety check --bare