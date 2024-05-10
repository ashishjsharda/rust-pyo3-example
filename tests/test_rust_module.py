import sys
import os

# Get the absolute path to the rust-pyo3-example directory
rust_pyo3_example_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the target/release directory to the Python module search path
sys.path.append(os.path.join(rust_pyo3_example_dir, 'target', 'release'))

import rust_module

def test_sum_as_string():
    assert rust_module.sum_as_string(5, 7) == "12"