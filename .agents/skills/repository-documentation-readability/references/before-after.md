<!-- Bundled examples for the repository-documentation-readability skill.
The root examples/before-after.md in the source repository is canonical. Keep this bundled copy synchronized before publishing a release. -->

# Before and after: repository documentation readability

These fictional examples show how to apply the guide without changing technical meaning.

They are transformations, not templates. The useful lesson is **why** the representation changes.

For the underlying guidance, see [GUIDE.md](../GUIDE.md).

## Example 1: turn a wall of text into a reading path

### Before

> Data Relay imports vendor CSV files into the analytics warehouse and before using it you need Python 3.12 and credentials in the environment and the input file must contain vendor_id, recorded_at, and amount columns, then you run python -m relay.import_file followed by the path and the command validates the file and writes accepted rows, but invalid rows are not written and are instead recorded in reports/rejected.csv and the process exits with status 2 when any rejected rows exist, and if the file passes completely it exits with status 0, and the import is idempotent based on vendor_id plus recorded_at so rerunning the same file will not duplicate accepted rows.

The paragraph is technically dense but forces the reader to extract prerequisites, schema, procedure, behavior, and exit semantics from one block.

### After

#### Import a vendor export

Data Relay validates a vendor CSV before writing accepted rows to the analytics warehouse. Imports are idempotent on the pair `vendor_id + recorded_at`, so rerunning the same file does not duplicate accepted rows.

**Prerequisites**

- Python 3.12
- warehouse credentials in the environment
- a CSV containing the required columns below

| Required column | Meaning |
| --- | --- |
| `vendor_id` | Vendor identifier |
| `recorded_at` | Source timestamp |
| `amount` | Imported amount |

**Run the import**

1. Execute:

   ```powershell
   python -m relay.import_file .\data\vendor.csv
   ```

2. Check the exit status.
3. If rows were rejected, inspect `reports/rejected.csv`.

| Result | Exit status | Effect |
| --- | ---: | --- |
| All rows accepted | `0` | Accepted rows are written |
| One or more rows rejected | `2` | Accepted rows are written; rejected rows are reported |

### Why the after version is easier to use

The technical behavior is unchanged. The presentation now separates:

- orientation: what the command does;
- prerequisites: what must be true first;
- procedure: what the reader should do;
- reference: required columns and exit behavior.

The reader can scan for one question without rereading the entire explanation.

## Example 2: replace a diagram that does not need to be a diagram

### Before

A mostly linear setup procedure is expressed as a large flowchart:

```mermaid
flowchart TD
    A["Clone repository"] --> B["Install dependencies"]
    B --> C["Copy environment file"]
    C --> D["Add credentials"]
    D --> E["Run database migration"]
    E --> F["Start application"]
    F --> G["Open health endpoint"]
    G --> H{"Healthy?"}
    H -->|Yes| I["Begin development"]
    H -->|No| J["Inspect startup logs"]
    J --> D
```

The diagram mixes a seven-step linear procedure with one small troubleshooting branch. Most of the visual structure adds no information beyond sequence.

### After

#### Start the application

1. Clone the repository.
2. Install dependencies.
3. Copy the environment file.
4. Add the required credentials.
5. Run the database migration.
6. Start the application.
7. Open the health endpoint.

If the health check passes, begin development. If it fails, inspect the startup logs, correct the environment or credentials, and retry.

### Why the after version is easier to use

A numbered list exposes the order more directly, is easier to copy into a checklist, and requires less horizontal or visual parsing on a phone.

The branch is simple enough to explain in one sentence. If troubleshooting later develops several distinct paths, a small decision diagram may become useful at that point.

## Example 3: structure troubleshooting around recovery

### Before

> If the worker does not start, first make sure Redis is running because sometimes the connection string is wrong or the service has not started, and you can also check the logs, and if you changed the environment file you might need to restart the terminal, and the worker should eventually print ready when everything is correct.

The paragraph mixes several possible causes, actions, and an expected result without telling the reader what to check first.

### After

#### Worker does not start

| Symptom | Likely cause | Resolution | Verify |
| --- | --- | --- | --- |
| Worker exits with a Redis connection error | Redis is not running | Start the configured Redis service | Retry the worker; the Redis connection error is gone |
| Worker connects to the wrong host | `REDIS_URL` is incorrect | Correct `REDIS_URL` in the environment | Print or inspect the active configuration, then retry |
| Environment changes are ignored | The current shell still has old values | Reload the environment or open a new shell | Start the worker and confirm it uses the updated value |

If none of these paths matches the observed failure, inspect the startup logs before changing additional configuration.

A healthy worker prints:

```text
ready
```

### Why the after version is easier to use

The reader can match an observable symptom to a likely cause, perform one targeted action, and verify whether recovery occurred.

The table also separates known troubleshooting paths from open-ended diagnostics instead of presenting every possibility as equally likely.

## What these examples demonstrate

A readability refactor should not ask, "How can I make this more visual?"

It should ask:

1. What is the reader trying to do: learn, complete a task, look up facts, or understand?
2. Who is the intended reader, and what must they already know or have?
3. Which information is explanation, procedure, reference, troubleshooting, or relationship?
4. What is the simplest representation that preserves the technical truth?
5. Can examples, links, and expected results be checked?
6. Can the reader find the answer quickly on both a narrow and a wide screen?
