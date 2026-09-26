# Commands

`add NAME QUANTITY` increases stock; `use NAME QUANTITY` decreases it; `list` shows items in alphabetical order. Quantities must be positive integers. `use` rejects a request larger than current stock. The data file defaults to `kitchen.json`; use `--file PATH` or `PANTRY_FILE` to choose another file.

Documentation drift exercise: if the implementation changes the default file or quantity rules, the custodian should cite both this guide and `pantry.py`, then propose a documentation pull request.
