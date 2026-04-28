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

## Available Tools
- `get_databases`: List all databases
- `get_tables_in_db`: List tables in a specific database
- `get_records`: Get all rows from a table
- `get_specific_column_records`: Get specific columns from a table
- `custom_sql_query`: Run custom SQL queries