#! user/bin/env make

output.yaml: *.txtCleaned
	python ParseSentence.py

.PHONY: clean

clean:
	rm -f output.yaml
