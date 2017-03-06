UI_FILES = $(wildcard _ui/*.ui)

all: $(UI_FILES:.ui=.py)

_ui/%.py: _ui/%.ui
	pyside-uic $< -o $@
	
clean:
	rm -f $(UI_FILES:.ui=.py)

