# CyberToolkit

A modular, advanced cybersecurity framework designed for ethical hackers, penetration testers, and security researchers. Built with Python, featuring an interactive CLI, auto-loading modules, and extensible plugin system.

## Features

- **Modular Architecture**: Auto-loading modules and plugins
- **Interactive Dashboard**: Rich terminal UI with commands
- **Multi-threaded Tools**: Fast scanning and brute-forcing
- **Cross-Platform**: Works on Linux, Kali Linux, and Termux
- **Voice Recognition**: Speech-to-text commands
- **AI Module Generator**: Create custom tools easily
- **Plugin Installer**: Git-based plugin management

## Installation

### Prerequisites
- Python 3.6+
- Internet connection for API-based tools

### Install from Source
```bash
git clone https://github.com/darkcoder194/Tool.git
cd Tool
pip install -r requirements.txt
```

### For Termux (Android)
```bash
pkg install python git
git clone https://github.com/darkcoder194/Tool.git
cd Tool
pip install -r requirements.txt
```

## Usage

### Interactive Mode
```bash
python -m cybertoolkit.main
```
This starts the interactive shell:
```
CyberToolkit v1.0
Type 'help' for commands
cybertool >
```

### Direct Command Mode
```bash
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