# CyberToolkit

A professional, modular cybersecurity framework designed for ethical hackers, penetration testers, and security researchers. Built with Python, featuring a powerful CLI, auto-loading modules, extensible plugin system, and configuration management.

## Features

- **Professional CLI**: Command-line interface with subcommands, help, and version
- **Modular Architecture**: Auto-loading modules and plugins
- **Configuration Management**: JSON-based config with CLI management
- **Logging Support**: Configurable logging levels and file output
- **Interactive Dashboard**: Rich terminal UI with commands
- **Multi-threaded Tools**: Fast scanning and brute-forcing
- **Cross-Platform**: Works on Linux, Kali Linux, and Termux
- **Voice Recognition**: Speech-to-text commands
- **AI Module Generator**: Create custom tools easily
- **Plugin Installer**: Git-based plugin management
- **Auto-Update**: Built-in update mechanism

## Installation

### Prerequisites
- Python 3.6+
- Internet connection for API-based tools

### Install from Source
```bash
git clone https://github.com/darkcoder194/Tool.git
cd Tool
pip install -r requirements.txt
pip install .
```

### For Termux (Android)
```bash
pkg install python git
git clone https://github.com/darkcoder194/Tool.git
cd Tool
pip install -r requirements.txt
pip install .
# For voice recognition (optional):
pip install SpeechRecognition
# May require: pkg install portaudio
```

### For Kali Linux
```bash
sudo apt update
sudo apt install python3 python3-pip git
git clone https://github.com/darkcoder194/Tool.git
cd Tool
pip3 install -r requirements.txt
pip3 install .
```

## Usage

### Command Line Interface

CyberToolkit now supports a professional command-line interface:

```bash
# Show help
cybertool --help

# Show version
cybertool --version

# List all available modules
cybertool list

# Run a specific module
cybertool run <module_id> [args...]

# Update the toolkit
cybertool update

# Manage configuration
cybertool config list
cybertool config get <key>
cybertool config set <key> <value>

# Start interactive mode
cybertool interactive
```

### Interactive Mode
```bash
cybertool
```
This starts the interactive shell:
```
CyberToolkit v1.0
Type 'help' for commands
cybertool >
```

### Examples

```bash
# DNS lookup
cybertool run dns google.com

# Port scan
cybertool run port 192.168.1.1

# List modules
cybertool list

# Update toolkit
cybertool update

# Set log level
cybertool --log-level DEBUG run port 127.0.0.1
```

## Configuration

Configuration is stored in `~/.cybertoolkit/config.json`. You can manage it via CLI:

```bash
# List all config
cybertool config list

# Get a specific value
cybertool config get log_level

# Set a value
cybertool config set log_level DEBUG
```

## Modules

Available modules include:

- **sub**: Subdomain Finder
- **5**: hm
- **headers**: HTTP Headers Analyzer
- **whois**: WHOIS Lookup
- **hash**: Hash Generator
- **dir**: Directory Brute-Force Scanner
- **net**: Network Info
- **tech**: Web Technology Detector
- **port**: Port Scanner
- **ip**: IP Lookup
- **pass**: Password Strength
- **gh-search**: GitHub Tool Search
- **netmon**: Network Monitor
- **voice**: Voice Recognition
- **dns**: DNS Lookup

## Development

### Adding New Modules

Create a new Python file in the `cybertoolkit/modules/` directory with a `tool_info()` function:

```python
def tool_info():
    return {
        'id': 'mytool',
        'name': 'My Custom Tool',
        'run': run_tool
    }

def run_tool(args):
    # Your tool logic here
    pass
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
python -m cybertoolkit.main <command> <args>
```

## Commands

### Core Commands
- `help` - Show available commands
- `tools` - List all loaded modules and plugins
- `reload` - Reload modules and plugins
- `exit` - Exit the toolkit

### Available Modules

| Command | Description | Usage |
|---------|-------------|-------|
| `ip` | IP geolocation lookup | `ip <ip_address>` |
| `dns` | DNS resolution and reverse lookup | `dns <domain>` |
| `whois` | WHOIS domain information | `whois <domain>` |
| `port` | Multi-threaded port scanner | `port <ip> [start_port] [end_port]` |
| `sub` | Subdomain enumeration | `sub <domain>` |
| `headers` | HTTP header analysis | `headers <url>` |
| `gh-search` | GitHub repository search | `gh-search <query>` |
| `dir` | Directory brute-force scanner | `dir <url> [threads]` |
| `tech` | Web technology detector | `tech <url>` |
| `voice` | Voice recognition (speech-to-text) | `voice` |
| `install` | Install plugin from GitHub | `install <github-repo-url>` |
| `ai-build` | Generate new module template | `ai-build <id> <name>` |
| `dashboard` | Show dashboard panel | `dashboard` |
| `hash` | Hash generator (MD5/SHA1/SHA256) | `hash <text>` |
| `pass` | Password strength checker | `pass <password>` |
| `net` | System network information | `net` |
| `netmon` | Network traffic monitor | `netmon` |
| `5` | Custom module (placeholder) | `5 <args>` |

## Examples

### IP Lookup
```bash
cybertool > ip 8.8.8.8
# or
python -m cybertoolkit.main ip 8.8.8.8
```

### Port Scanning
```bash
cybertool > port 192.168.1.1 1 1000
```

### Directory Brute-Force
```bash
cybertool > dir http://example.com 20
```

### Install Plugin
```bash
cybertool > install https://github.com/user/custom-plugin
```

### Voice Recognition
```bash
cybertool > voice
# Speak a command like "run ip 8.8.8.8"
```

## Architecture

### Project Structure
```
cybertoolkit/
├── cli.py                 # Interactive command-line interface
├── main.py                # Entry point and argument parser
├── module_registry.py     # Dynamic module loading system
├── plugin_installer.py    # Plugin management
├── ai_builder.py          # Module template generator
├── dashboard.py           # Dashboard display
├── modules/               # Built-in modules
│   ├── ip_lookup.py
│   ├── dns_lookup.py
│   ├── port_scanner.py
│   └── ...
├── plugins/               # Extensible plugins
│   ├── loader.py
│   └── (installed plugins)
└── __init__.py
```

### Module Format
Each module must implement:
```python
def tool_info():
    return {
        "id": "command_name",
        "name": "Tool Name",
        "run": run
    }

def run(args):
    # Tool implementation
    pass
```

### Plugin System
Plugins are installed via Git and auto-loaded:
- Clone to `cybertoolkit/plugins/`
- Follow same module format
- Reload with `reload` command

## Requirements

- `rich` - Terminal UI
- `requests` - HTTP client
- `dnspython` - DNS operations
- `python-whois` - WHOIS lookups
- `SpeechRecognition` - Voice recognition
- `pyfiglet` - ASCII art (optional)

## Development

### Adding New Modules
1. Create `modules/new_tool.py`
2. Implement `tool_info()` and `run(args)`
3. Test with `python -m cybertoolkit.main new_tool <args>`

### Creating Plugins
1. Create GitHub repository with module file
2. Install with `install <repo-url>`
3. Plugin appears in `tools` list

## Security Notice

CyberToolkit is for educational and ethical security research only. Use responsibly and with permission. The authors are not responsible for misuse.

## License

MIT License - See LICENSE file for details.

## Contributing

1. Fork the repository
2. Create feature branch
3. Add modules/plugins
4. Test thoroughly
5. Submit pull request

## Support

- Issues: GitHub Issues
- Wiki: Documentation and tutorials
- Community: Join discussions

---

**Built with ❤️ for the cybersecurity community**