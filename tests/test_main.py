**Pytest uchun test kod**
```python
import pytest
from kalkulyator import Kalkulyator

def test_qoshish():
    kalkulyator = Kalkulyator()
    assert kalkulyator.qoshish(5, 3) == 8

def test_ayirish():
    kalkulyator = Kalkulyator()
    assert kalkulyator.ayirish(5, 3) == 2

def test_kopaytirish():
    kalkulyator = Kalkulyator()
    assert kalkulyator.kopaytirish(5, 3) == 15

def test_bolish():
    kalkulyator = Kalkulyator()
    assert kalkulyator.bolish(5, 3) == 1

def test_qoshish_sifatli():
    kalkulyator = Kalkulyator()
    with pytest.raises(TypeError):
        kalkulyator.qoshish('a', 3)

def test_ayirish_sifatli():
    kalkulyator = Kalkulyator()
    with pytest.raises(TypeError):
        kalkulyator.ayirish('a', 3)

def test_kopaytirish_sifatli():
    kalkulyator = Kalkulyator()
    with pytest.raises(TypeError):
        kalkulyator.kopaytirish('a', 3)

def test_bolish_sifatli():
    kalkulyator = Kalkulyator()
    with pytest.raises(TypeError):
        kalkulyator.bolish('a', 3)
```

**Jest uchun test kod**
```javascript
import { describe, it, expect } from '@jest/globals';
import Kalkulyator from './kalkulyator';

describe('Kalkulyator', () => {
  it('qoshish', () => {
    const kalkulyator = new Kalkulyator();
    expect(kalkulyator.qoshish(5, 3)).toBe(8);
  });

  it('ayirish', () => {
    const kalkulyator = new Kalkulyator();
    expect(kalkulyator.ayirish(5, 3)).toBe(2);
  });

  it('kopaytirish', () => {
    const kalkulyator = new Kalkulyator();
    expect(kalkulyator.kopaytirish(5, 3)).toBe(15);
  });

  it('bolish', () => {
    const kalkulyator = new Kalkulyator();
    expect(kalkulyator.bolish(5, 3)).toBe(1);
  });

  it('qoshish sifatli', () => {
    const kalkulyator = new Kalkulyator();
    expect(() => kalkulyator.qoshish('a', 3)).toThrowError();
  });

  it('ayirish sifatli', () => {
    const kalkulyator = new Kalkulyator();
    expect(() => kalkulyator.ayirish('a', 3)).toThrowError();
  });

  it('kopaytirish sifatli', () => {
    const kalkulyator = new Kalkulyator();
    expect(() => kalkulyator.kopaytirish('a', 3)).toThrowError();
  });

  it('bolish sifatli', () => {
    const kalkulyator = new Kalkulyator();
    expect(() => kalkulyator.bolish('a', 3)).toThrowError();
  });
});
```
