# stdio-mysql-mcp

A Model Context Protocol (MCP) server that allows AI assistants like Claude Desktop and GitHub Copilot to connect to and query MySQL databases locally using standard input/output (stdio).

## Usage with Claude Desktop / GitHub Copilot

Add this to your MCP configuration file (`claude_desktop_config.json` or your custom settings):

```json
{
  "mcpServers": {
    "mysql-server": {
      "command": "uvx",
      "args": ["stdio-mysql-mcp"],
      "env": {
        "MYSQL_URL": "mysql://user:password@localhost:3306"
      }
    }
  }
}
```
## Usage with GitHub Copilot

If you're using the GitHub Copilot local/desktop integration (or another Copilot-compatible MCP host) the config format may differ. Here's the example you supplied — it works and shows how to point Copilot to a local Python interpreter and run the MCP server module:

```json
{
  "servers": {
    "my-mysql-server": {
      "command": "check/Scripts/python.exe",
      "args": [
        "-m",
        "stdio_mysql_mcp.server"
      ],
      "env": {
        "MYSQL_URL": "mysql://username:password@localhost:3306"
      }
    }
  }
}
```

Notes:
- `command` should be the full path to the Python executable you want Copilot to use. In virtualenvs on Windows this often looks like `path\to\venv\Scripts\python.exe`; on macOS/Linux it might be `path/to/venv/bin/python`.
- The `-m stdio_mysql_mcp.server` form runs the package's server module directly from the chosen Python interpreter.
- Ensure the Python environment has the package (or the source) installed so the module resolves.


## Available Tools
- `get_databases`: List all databases
- `get_tables_in_db`: List tables in a specific database
- `get_records`: Get all rows from a table
- `get_specific_column_records`: Get specific columns from a table
- `custom_sql_query`: Run custom SQL queries