# Interactive Client Update

This command will guide you through the mostly-automated process of updating this client library
to match the current Dialpad API spec. To do accomplish, it will:

- Overwrite `dialpad_api_spec.json` with the latest OpenAPI spec from Dialpad.
- Apply some light in-place preprocessing to `dialpad_api_spec.json`.
- Update `module_mapping.json` to include any new API endpoints that need to be mapped.
  - (This is the interactive bit)
- Re-generate the client resources and schemas.
- Bump the package version in `pyproject.toml`

During the mapping update step, you will be prompted to choose the appropriate `Class` and
`method()` names for any API operations that are not already mapped. The tool will suggest existing
Resource class names if an API sub-path is already mapped to a particular resource class, and the
suggested method names are just based on the HTTP verb (which isn't always an effective strategy).
As an illustrative example, `/api/v2/users/{id}/assign_number [POST]` is mapped to
`UsersResource.assign_number`.

This tool will only make **local changes**, so there's very little risk involved 👍

