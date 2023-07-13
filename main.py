import importlib

day = "39"
dayCode = "day"+day

your_module = importlib.import_module(dayCode)
your_module.quote

print("Code run")