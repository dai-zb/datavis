.PHONY: build install uninstall lint clean

project_name = datavis
python = python
pip = pip

build: clean lint
	# sdist  将源码进行打包
	# python setup.py sdist bdist_wheel
	$(python) setup.py bdist_wheel

build_pyc: build
	 $(python) -m pyc src $(project_name)

install: uninstall build
	$(pip) install dist/*.whl

install_pyc: uninstall build_pyc
	$(pip) install .dist/*.whl

uninstall:
	$(pip) uninstall -y $(project_name)

lint:
	mypy src/$(project_name) --no-site-packages --ignore-missing-imports

clean:
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete

	rm -rf build
	rm -rf dist .dist .pyc
	rm -rf src/$(project_name).egg-info

	rm -rf .mypy_cache
	rm -rf coverage_result

test: lint
	$(python) -m unittest

# 代码覆盖率
coverage: lint
	$(python) -m coverage run -m unittest
	coverage html -d coverage_result
	coverage report > coverage_result.txt
	coverage report

