# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

import os
import re

abs_path = os.path.dirname(os.path.abspath(__file__))
notebook = os.path.join(abs_path, "..", "..", "..", "..", "Tutorials", "CNTK_203_Reinforcement_Learning_Basics.ipynb")
notebook_timeoutSeconds = 450

def get_output_stream_from_cell(cell, stream_name='stdout'):
    return "\n".join([output.text for output in cell.get('outputs', [])
        if output.output_type == 'stream' and output.name == stream_name])

def test_cntk_203_reinforcement_learning_basics_noErrors(nb):
    errors = [output for cell in nb.cells if 'outputs' in cell
              for output in cell['outputs'] if output.output_type == "error"]
    print(errors)
    assert errors == []

def test_cntk_203_reinforcement_learning_basics_tasks_are_solved(nb):
    testCells = [cell for cell in nb.cells if re.search('Task solved in[ :]', get_output_stream_from_cell(cell))]
    assert len(testCells) == 2
