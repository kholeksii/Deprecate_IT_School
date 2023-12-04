from src.drag_and_drop_functions import *
import os
import pytest
def test_drag_and_drop_test():
    created_scrn_path = drag_and_drop('https://the-internet.herokuapp.com/drag_and_drop', '//*[@id="column-a"]', '//*[@id="column-b"]', 'scrn_1.png')
    print(created_scrn_path)
    assert validate_file_contents(created_scrn_path, 'golden_scrn_1.png') == True
    os.remove(created_scrn_path)