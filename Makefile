init:
	pipenv install --dev

serve:
	pipenv run python main.py

test:
	pipenv run tests-execution

list-test:
	pipenv run tests-list
