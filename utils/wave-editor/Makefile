UI_FILES = $(wildcard resources/*.ui)
UI_PY_FILES := $(addprefix wave_editor/_ui/, $(notdir $(UI_FILES:.ui=.py)))

all: build_ui build_qrc

build_ui: $(UI_PY_FILES)
build_qrc: wave_editor/_ui/wave_editor_rc.py

wave_editor/_ui/wave_editor_rc.py: resources/wave_editor.qrc
	pyside-rcc $< -o $@

wave_editor/_ui/%.py: resources/%.ui
	pyside-uic $< -o $@

run: all
	python -m wave_editor

clean:
	rm -f $(UI_PY_FILES) wave_editor/_ui/wave_editor_rc.py

.PHONY: help clean all run
