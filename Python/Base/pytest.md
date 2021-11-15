# Pytest
## Simple Application
### scripty.py:
```python
def fx(x, y):
    return x == y

def test_fx():
    assert fx(1, 1)
    assert not fx(1, 2)
```

### How to test
```bash
pytest scripty.py -> output report  # All test_functions()

pytest scripty.py::text_fx          # Specific Function

pytest testing/                     # All tests in dir
```

# Skipping and adding conditions
To skip, skipif and provide reason for known failure:
```python
@pytest.mark.xfail(reason='Bug #42') # a TODO test
def test_fx():
    assert fx(1, 1)
    assert not fx(1, 2)

@pytest.mark.skipif(sys.platform=='win32', 
                    reason='Not applicable to windows')
def test_fx():
    assert fx(1, 1)
    assert not fx(1, 2)

@pytest.mark.skip(reason='reason') # Force test to never run
    assert fx(1, 1)
    assert not fx(1, 2)    
```

# Expected exceptions/warnings to be raised
```python
def test_zero_division():
    with pytest.raises(ZeroDivisionError, 
                       message="Expecting ZeroDivisionError"):
        1 / 0

def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn("my warning", UserWarning)
```

# Handle float comparisons
```python
from pytest import approx
# approx (rel=?, abs = ?)

# floats
isequal = 0.1 + 0.2 == approx(0.3)

# lists
isequal = (0.1 + 0.2, 0.2 + 0.4) == approx((0.3, 0.6))

# dicts
isequal = {'a': 0.1 + 0.2, 'b': 0.2 + 0.4} == approx({'a': 0.3, 'b': 0.6})

# numpy arrays
isequal = np.array([0.1, 0.2]) + np.array([0.2, 0.4]) == approx(np.array([0.3, 0.6])) 
```
# Pytest options

pytest -<> to get extra detail on:

    +----+--------------------+
    | rf | failed             |
    | rE | errors             |
    | rs | skipped            |
    | rx | failed             |
    | rX | passed             |
    | rp | passes             |
    | rP | pass with input    |
    | ra | all except pP      |
    +----+--------------------+

## Runtime options:
    --pdb   # with debugger
    -v      # verbose
    -s      # print stdoutput/stdferr
    -x      # stop after 1st failure

# Automatic Setup and Teardown

```python
def setup_function():
    pass

def teardown_function():
    pass

def test_thing(tmpdir):
    #pytest passes this location to you
    pass
```