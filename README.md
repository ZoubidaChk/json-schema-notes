# JSON Schema Notes
A utility for working with notes and JSON Schema data.

## Run

Run the project with Python:

    python json_schema_notes.py

This project is kept as a standalone Python file and uses Python libraries only.
 
## Features
- Validates basic data types:
  - `object`, `array`, `string`, `number`, `integer`, `boolean`
- Enforces `required` fields (within objects)
- Checks string length via `minLength`
- Supports nested object schemas (recursive validation)
- Returns clear error messages with JSON‑pointer‑like paths

> **Note:** This is **not** a full JSON Schema implementation. It supports only a subset of keywords (see [Schema Format](#schema-format) below).
