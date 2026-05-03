from typing import Callable, Any
from functools import singledispatch, wraps
import time

@singledispatch
def base(spell: Any):
  return "Unknon spell type"

@base.register(str)
def _(Enchantment: str):
  return f"Enchantment: {Enchantment}"
@base.register(int)
def _(Damagespell: int):
  return f"Damage spell: {Damagespell} damage"
@base.register(list)
def _(multi_cast: list):
  n = len(multi_cast)
  return f"Multi-cast: {n} spells"
def spell_dispatcher() -> Callable[[Any], str]:
    return base






def spell_timer(func: Callable) -> Callable:
  @wraps(func)
  def wrapper(*args, **kwargs):
    print(f"Casting {func.__name__}...")
    start = time.time()
    result = func(*args, **kwargs)
    final = time.time()
    dur = final - start
    print(f"Spell completed in {dur:.3f} seconds")
    return result
  return wrapper
@spell_timer
def fireball():
  time.sleep(0.101)
  return "Result: Fireball cast!"


def power_validator(min_power: int) -> Callable:
  def dec(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
      if args[0] >= min_power:
        return func(*args, **kwargs)
      else:
        return "Insufficient power for this spell"
    return wrapper
  return dec

@power_validator(40)
def cast_fireball(power: int):
    return f"Fireball launched with {power} power!"

def retry_spell(max_attempts: int) -> Callable:
  def dec(func: Callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        attempts = 1 
        while attempts < max_attempts:
          try:
            return func(*args, **kwargs)
          except Exception:
            print(f"Spell failed, retrying... (attempt {attempts}/{max_attempts})")
            attempts += 1
        return f"Spell casting failed after {max_attempts} attempts"
    return wrapper
  return dec

@retry_spell(3)
def zip(target_heal: int, power: int) -> str:
    if target_heal > power:
      raise ValueError("u cant attack")
    else:
      return "Waaaaaaagh spelled !"
    
def power_validator(min_power: int) -> Callable:
  def dec(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
      if args[2] >= min_power:
        return func(*args, **kwargs)
      else:
        return "Insufficient power for this spell"
    return wrapper
  return dec

class Mageguild:
  @staticmethod
  def validate_mage_name(name: str) -> bool:
    if len(name) >= 3 and (name.isalpha() or name.isspace()):
      return True
    else:
      return False
  @power_validator(10)
  def cast_spell(self, spell_name: str, power: int) -> str:
    return f"Successfully cast {spell_name} with {power} power"



dispatcher = spell_dispatcher()
print(cast_fireball(60))
print(cast_fireball(30))
print(fireball())
print(dispatcher(42))                       
print(dispatcher(["fireball", "zip", "rocket"]))    
print(dispatcher(3.14))
print(zip(40,50))
print(zip(40,30))
mage = Mageguild()
print(mage.validate_mage_name("fews"))
print(mage.validate_mage_name("fews4"))
print(mage.cast_spell("lightning", 15))
print(mage.cast_spell("lightning", 5))
