.PHONY: help init test-generator clean-test

help: ## Show this help message
	@echo 'FastAPI Skeleton Generator'
	@echo '========================='
	@echo ''
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

init: ## Create new FastAPI project (usage: make init PROJECT=my-project)
	@if [ -z "$(PROJECT)" ]; then \
		echo "❌ PROJECT variable is required. Usage: make init PROJECT=my-project"; \
		exit 1; \
	fi
	chmod +x fastapi-init scripts/*.py scripts/*.sh
	./fastapi-init $(PROJECT) $(ARGS)

init-here: ## Initialize current directory as FastAPI project
	chmod +x fastapi-init scripts/*.py scripts/*.sh
	./fastapi-init . $(ARGS)

test-generator: ## Test the generator with a sample project
	chmod +x test-generator.sh
	./test-generator.sh

clean-test: ## Clean up test projects
	rm -rf test-project-* test-gen-* || true
	@echo "🧹 Stopping any running test containers..."
	docker stop test_gen_sample_backend test_gen_sample_frontend test_gen_sample_postgres || true
	docker rm test_gen_sample_backend test_gen_sample_frontend test_gen_sample_postgres || true
	docker volume rm test-gen-sample_postgres_data || true
	@echo "✅ Test projects and containers cleaned up"

cleanup-project: ## Clean up a specific project (usage: make cleanup-project PROJECT=name)
	@if [ -z "$(PROJECT)" ]; then \
		echo "❌ PROJECT variable is required. Usage: make cleanup-project PROJECT=my-project"; \
		exit 1; \
	fi
	chmod +x cleanup-project.sh
	./cleanup-project.sh $(PROJECT)

validate: ## Validate generator scripts
	chmod +x fastapi-init scripts/*.py scripts/*.sh
	bash -n fastapi-init
	bash -n scripts/validate.sh
	python3 -m py_compile scripts/customize.py
	@echo "✅ All scripts are valid"

# Development helpers
update-permissions: ## Update script permissions
	chmod +x fastapi-init scripts/*.py scripts/*.sh
	@echo "✅ Permissions updated"

show-structure: ## Show the skeleton structure
	@echo "📁 Skeleton structure:"
	@tree skeleton/ 2>/dev/null || find skeleton/ -type f | sort
