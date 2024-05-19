.DEFAULT_GOAL := help

CURRENT_DIR := $(CURDIR)

MODULE1=$(CURRENT_DIR)/module-1
MODULE1_CRITICAL_THINKING=$(MODULE1)/critical-thinking


.PHONY: help
help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*' $(MAKEFILE_LIST) | sort

.PHONY: m1
m1: ## executes module 1 critical thinking
	@echo "executing module 1 critical thinking ..."
	@cd $(MODULE1_CRITICAL_THINKING); ./app.py
	@echo "completed module 1 critical thinking."
