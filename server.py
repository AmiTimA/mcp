from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Weather Service")


@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    return f"The current weather in {location} is sunny with a temperature of 25°C."

@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Resource to get weather information."""
    return f"Weather data for {location}: Sunny, 25°C."

@mcp.prompt()
def weather_report(location: str) -> str:
    """Generate a weather report for a given location."""
    return f"Weather Report:\n{location}"

# Run the server
if __name__ == "__main__":
    mcp.run(transport="sse", port=3001)