.PHONY: .FORCE

build: .FORCE
	python setup.py sdist bdist_wheel

upload: .FORCE
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

#asks python to run this file right here
test1: .FORCE
	python main_test.py

#asks python to run a module wit this name
#python searches for it in the current folder and in other standard places described in [https://bic-berkeley.github.io/psych-214-fall-2016/sys_path.html]
test2: .FORCE
	python -m main_test

#runs a nested module file directly
test3: .FORCE
	python ./example_package/subpackage_redpill/module_br.py
#>>> Hello from: ./example_package/subpackage_redpill/module_br.py @ 2

#runs it as a module withn a subpackage within a packagea nested module file directly
test4: .FORCE
	python -m example_package.subpackage_redpill.module_br
#>>> Hello from: /mnt/storage/github/example_package_module_import/example_package/__init__.py @ 2
#>>> Hello from: /mnt/storage/github/example_package_module_import/example_package/subpackage_redpill/__init__.py @ 2
#>>> Hello from: /mnt/storage/github/example_package_module_import/example_package/subpackage_redpill/module_br.py @ 2

#tries to run a subpackage directory as if a file
test5: .FORCE
	python ./example_package/subpackage_redpill
#>>> Hello from: ./example_package/subpackage_redpill/__main__.py @ 2

#tries to run a subpackage as if a module
test5b: .FORCE
	python -m example_package.subpackage_redpill
#>>> Hello from: ./example_package/subpackage_redpill/__main__.py @ 2

#imports
test6: .FORCE
	python main_test6.py

test7: .FORCE
	python main_test7.py

test8: .FORCE
	python main_test8.py

test9: .FORCE
	python main_test9.py

test10: .FORCE
	python main_test10.py

test11: .FORCE
	python main_test11.py

#double import trap
test12: .FORCE
	(cd example_package/subpackage_redpill; python ../../main_test12.py)

#double import trap [http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html]
test13: .FORCE
	(cd example_package/subpackage_redpill; python < ../../main_test13.py)
#happens when you add a dir from inside the package to the path, e.g. when you run a python from inside the dir, and you do a local import ignoring the imported module being part of a package structure.

