# EDR-001: Dataset Format Readers

## Status

Accepted

## Context

Athena needs to support multiple dataset formats such as CSV and Excel.

The initial DatasetEngine implementation can directly read a dataset using Pandas. However, placing format-specific reading logic for every supported format directly inside DatasetEngine would make the engine increasingly large and difficult to maintain as more formats are introduced.

Athena's architecture aims to keep responsibilities separated and make individual components easier to understand, test, debug, and modify.

## Decision

DatasetEngine will act as the coordinator for dataset reading, while individual reader components will handle format-specific reading logic.

The structure will follow this approach:

DatasetEngine
→ identifies the dataset format
→ selects the appropriate reader
→ delegates the reading operation
→ receives the resulting dataset representation

For example:

- CSVReader handles CSV files.
- ExcelReader handles Excel files.

Additional readers can be introduced later without placing all format-specific logic inside DatasetEngine.

## Rationale

This approach provides:

- Separation of responsibilities.
- Easier maintenance.
- Easier testing of individual readers.
- Clearer debugging boundaries.
- Better scalability when additional dataset formats are supported.
- Reduced growth of DatasetEngine as format support expands.

DatasetEngine therefore acts as a coordinator rather than containing the implementation details of every dataset format.

## Consequences

### Positive

Adding a new dataset format can be done by introducing a new reader rather than significantly modifying existing format-reading logic.

Individual readers can be tested independently.

DatasetEngine remains focused on coordinating dataset interpretation.

### Negative

The project will contain more files and components than a single-reader implementation.

For the current scope, this additional structure is considered acceptable because maintainability and clear separation of responsibilities are important goals of Athena.

## Initial Supported Formats

The initial implementation will support:

- CSV
- Excel (`.xlsx`)

Additional formats will be introduced only when there is an actual requirement for them.

## Scope

This decision concerns dataset format reading and does not define the complete internal architecture of DatasetEngine.

Future responsibilities such as metadata analysis, data-quality analysis, statistical analysis, and other dataset intelligence capabilities may be separated further if the complexity warrants it.
