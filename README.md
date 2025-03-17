# Create a new directory for our project
uv init mcp-server
cd mcp-server

# Create virtual environment and activate it
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
uv add "mcp[cli]" httpx

# Start weather server 
uv run main.py

#open url to debug server 
npx @modelcontextprotocol/inspector uv run main.py 