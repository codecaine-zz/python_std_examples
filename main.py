from pathlib import Path
from doc_api import generate_code_example
import asyncio
import re

standard_library = {
    "Text Processing Services": [
        "re - Regular expression operations",
        "difflib - Helpers for computing deltas",
        "textwrap - Text wrapping and filling",
        "unicodedata - Unicode Database",
        "stringprep - Internet String Preparation",
        "readline - GNU readline interface",
        "rlcompleter - Completion function for GNU readline"
    ],
    "Binary Data Services": [
        "struct - Interpret bytes as packed binary data",
        "codecs - Codec registry and base classes",
        "Data Types",
        "datetime - Basic date and time types",
        "zoneinfo - IANA time zone support",
        "calendar - General calendar-related functions",
        "collections - Container datatypes",
        "collections.abc - Abstract Base Classes for Containers",
        "heapq - Heap queue algorithm",
        "bisect - Array bisection algorithm",
        "array - Efficient arrays of numeric values",
        "weakref - Weak references",
        "types - Dynamic type creation and names for built-in types",
        "copy - Shallow and deep copy operations",
        "pprint - Data pretty printer",
        "reprlib - Alternate repr() implementation",
        "enum - Support for enumerations",
        "graphlib - Functionality to operate with graph-like structures"
    ],
    "Numeric and Mathematical Modules": [
        "numbers - Numeric abstract base classes",
        "math - Mathematical functions",
        "cmath - Mathematical functions for complex numbers",
        "decimal - Decimal fixed-point and floating-point arithmetic",
        "fractions - Rational numbers",
        "random - Generate pseudo-random numbers",
        "statistics - Mathematical statistics functions"
    ],
    "Functional Programming Modules": [
        "itertools - Functions creating iterators for efficient looping",
        "functools - Higher-order functions and operations on callable objects",
        "operator - Standard operators as functions"
    ],
    "File and Directory Access": [
        "pathlib - Object-oriented filesystem paths",
        "os.path - Common pathname manipulations",
        "fileinput - Iterate over lines from multiple input streams",
        "stat - Interpreting stat() results",
        "filecmp - File and Directory Comparisons",
        "tempfile - Generate temporary files and directories",
        "glob - Unix style pathname pattern expansion",
        "fnmatch - Unix filename pattern matching",
        "linecache - Random access to text lines",
        "shutil - High-level file operations"
    ],
    "Data Persistence": [
        "pickle - Python object serialization",
        "copyreg - Register pickle support functions",
        "shelve - Python object persistence",
        "marshal - Internal Python object serialization",
        "dbm - Interfaces to Unix “databases”",
        "sqlite3 - DB-API 2.0 interface for SQLite databases"
    ],
    "Data Compression and Archiving": [
        "zlib - Compression compatible with gzip",
        "gzip - Support for gzip files",
        "bz2 - Support for bzip2 compression",
        "lzma - Compression using the LZMA algorithm",
        "zipfile - Work with ZIP archives",
        "tarfile - Read and write tar archive files"
    ],
    "File Formats": [
        "csv - CSV File Reading and Writing",
        "configparser - Configuration file parser",
        "tomllib - Parse TOML files",
        "netrc - netrc file processing",
        "plistlib - Generate and parse Apple .plist files"
    ],
    "Cryptographic Services": [
        "hashlib - Secure hashes and message digests",
        "hmac - Keyed-Hashing for Message Authentication",
        "secrets - Generate secure random numbers for managing secrets"
    ],
    "Generic Operating System Services": [
        "os - Miscellaneous operating system interfaces",
        "io - Core tools for working with streams",
        "time - Time access and conversions",
        "argparse - Parser for command-line options, arguments and subcommands",
        "logging - Logging facility for Python",
        "logging.config - Logging configuration",
        "logging.handlers - Logging handlers",
        "getpass - Portable password input",
        "curses - Terminal handling for character-cell displays",
        "curses.textpad - Text input widget for curses programs",
        "curses.ascii - Utilities for ASCII characters",
        "curses.panel - A panel stack extension for curses",
        "platform - Access to underlying platform’s identifying data",
        "errno - Standard errno system symbols",
        "ctypes - A foreign function library for Python"
    ],
    "Concurrent Execution": [
        "threading - Thread-based parallelism",
        "multiprocessing - Process-based parallelism",
        "multiprocessing.shared_memory - Shared memory for direct access across processes",
        "concurrent.futures - Launching parallel tasks",
        "subprocess - Subprocess management",
        "sched - Event scheduler",
        "queue - A synchronized queue class",
        "contextvars - Context Variables",
        "_thread - Low-level threading API"
    ],
    "Networking and Interprocess Communication": [
        "asyncio - Asynchronous I/O",
        "socket - Low-level networking interface",
        "ssl - TLS/SSL wrapper for socket objects",
        "select - Waiting for I/O completion",
        "selectors - High-level I/O multiplexing",
        "signal - Set handlers for asynchronous events",
        "mmap - Memory-mapped file support"
    ],
    "Internet Data Handling": [
        "email - An email and MIME handling package",
        "json - JSON encoder and decoder",
        "mailbox - Manipulate mailboxes in various formats",
        "mimetypes - Map filenames to MIME types",
        "base64 - Base16, Base32, Base64, Base85 Data Encodings",
        "binascii - Convert between binary and ASCII",
        "quopri - Encode and decode MIME quoted-printable data"
    ],
    "Structured Markup Processing Tools": [
        "html - HyperText Markup Language support",
        "html.parser - Simple HTML and XHTML parser",
        "html.entities - Definitions of HTML general entities"
    ],
    "XML Processing Modules": [
        "xml.etree.ElementTree - The ElementTree XML API",
        "xml.dom - The Document Object Model API",
        "xml.dom.minidom - Minimal DOM implementation",
        "xml.dom.pulldom - Support for building partial DOM trees",
        "xml.sax - Support for SAX2 parsers",
        "xml.sax.handler - Base classes for SAX handlers",
        "xml.sax.saxutils - SAX Utilities",
        "xml.sax.xmlreader - Interface for XML parsers",
        "xml.parsers.expat - Fast XML parsing using Expat"
    ],
    "Internet Protocols and Support": [
        "webbrowser - Convenient web-browser controller",
        "wsgiref - WSGI Utilities and Reference Implementation",
        "urllib - URL handling modules",
        "urllib.request - Extensible library for opening URLs",
        "urllib.response - Response classes used by urllib",
        "urllib.parse - Parse URLs into components",
        "urllib.error - Exception classes raised by urllib.request",
        "urllib.robotparser - Parser for robots.txt",
        "http - HTTP modules",
        "http.client - HTTP protocol client",
        "ftplib - FTP protocol client",
        "poplib - POP3 protocol client",
        "imaplib - IMAP4 protocol client",
        "nntplib - NNTP protocol client",
        "smtplib - SMTP protocol client",
        "http.server - HTTP servers",
        "http.cookies - HTTP state management",
        "http.cookiejar - Cookie handling for HTTP clients",
        "xmlrpc - XMLRPC server and client modules",
        "xmlrpc.client - XMLRPC client access",
        "xmlrpc.server - Basic XMLRPC servers",
        "ipaddress - IPv4/IPv6 manipulation library"
    ],
    "Multimedia Services": [
        "audioop - Manipulate raw audio data",
        "aifc - Read and write AIFF and AIFC files",
        "sunau - Read and write Sun AU files",
        "wave - Read and write WAV files",
        "chunk - Read IFF chunked data",
        "colorsys - Conversions between color systems",
        "imghdr - Determine the type of an image",
        "sndhdr - Determine type of sound file",
        "ossaudiodev - Access to OSS-compatible audio devices"
    ],
    "Internationalization": [
        "gettext - Multilingual internationalization services",
        "locale - Internationalization services"
    ],
    "Program Frameworks": [
        "turtle - Turtle graphics",
        "cmd - Support for line-oriented command interpreters",
        "shlex - Simple lexical analysis"
    ],
    "Graphical User Interfaces with Tk": [
        "tkinter - Python interface to Tcl/Tk",
        "tkinter.ttk - Tk themed widgets",
        "tkinter.tix - Extension widgets for Tk",
        "tkinter.scrolledtext - Scrolled Text Widget"
    ],
    "Development Tools": [
        "typing - Support for type hints",
        "pydoc - Documentation generator and online help system",
        "doctest - Test interactive Python examples",
        "unittest - Unit testing framework",
        "unittest.mock - mock object library",
        "unittest.mock - getting started",
        "2to3 - Automated Python 2 to 3 code translation",
        "test - Regression tests package for Python",
        "test.support - Utilities for the Python test suite",
        "test.support.script_helper - Utilities for the Python test suite"
    ],
    "Debugging and Profiling": [
        "bdb - Debugger framework",
        "faulthandler - Dump the Python traceback",
        "pdb - The Python Debugger",
        "timeit - Measure execution time of small code snippets",
        "trace - Trace or track Python statement execution",
        "tracemalloc - Trace memory allocations"
    ],
    "Software Packaging and Distribution": [
        "distutils - Building and installing Python packages",
        "ensurepip - Bootstrapping the pip installer",
        "venv - Creation of virtual environments",
        "zipapp - Manage executable Python zip archives"
    ],
    "Python Runtime Services": [
        "sys - System-specific parameters and functions",
        "sysconfig - Provide access to Python’s configuration information",
        "builtins - Built-in objects",
        "__main__ - Top-level script environment",
        "warnings - Warning control",
        "dataclasses - Data Classes",
        "contextlib - Utilities for with-statement contexts",
        "abc - Abstract Base Classes",
        "atexit - Exit handlers",
        "traceback - Print or retrieve a stack traceback",
        "__future__ - Future statement definitions",
        "gc - Garbage Collector interface",
        "inspect - Inspect live objects",
        "site - Site-specific configuration hook",
        "code - Interpreter base classes",
        "codeop - Compile Python code"
    ],
    "Custom Python Interpreters": [
        "code - Interpreter base classes",
        "codeop - Compile Python code"
    ],
    "Importing Modules": [
        "importlib - The implementation of import",
        "importlib.metadata - Accessing the import metadata",
        "importlib.resources - Resource reading using importers",
        "importlib.abc - Abstract base classes related to import",
        "importlib.util - Utility code for importers",
        "pkgutil - Package extension utility",
        "modulefinder - Find modules used by a script",
        "runpy - Locate and run Python modules without importing them first",
        "zipimport - Import modules from Zip archives"
    ],
    "Python Language Services": [
        "parser - Access Python parse trees",
        "ast - Abstract Syntax Trees",
        "symtable - Access to the compiler’s symbol tables",
        "token - Constants used with Python parse trees",
        "keyword - Testing for Python keywords",
        "tokenize - Tokenizer for Python source",
        "tabnanny - Detection of ambiguous indentation",
        "pyclbr - Python class browser support",
        "py_compile - Compile Python source files",
        "compileall - Byte-compile Python libraries",
        "dis - Disassembler for Python bytecode",
        "pickletools - Tools for pickle developers"
    ],
    "Miscellaneous Services": [
        "formatter - Generic output formatting"
    ],
    "Microsoft Windows Specific Services": [
        "msvcrt - Useful routines from the MS VC++ runtime",
        "winreg - Windows registry access",
        "winsound - Sound-playing interface for Windows"
    ],
    "Unix Specific Services": [
        "posix - The most common POSIX system calls",
        "pwd - The password database",
        "spwd - The shadow password database",
        "grp - The group database",
        "crypt - Function to check Unix passwords",
        "termios - POSIX style tty control",
        "tty - Terminal control functions",
        "pty - Pseudo-terminal utilities",
        "fcntl - The fcntl and ioctl system calls",
        "pipes - Interface to shell pipelines",
        "resource - Resource usage information",
        "nis - Interface to Sun’s NIS (Yellow Pages)",
        "syslog - Unix syslog library routines"
    ],
    "Superseded Modules": [
        "optparse - Parser for command line options",
        "imp - Access the import internals"
    ]
}

def safe_filename(name):
    return re.sub(r'[^\w\s\-_().,+]', ' ', name).strip().replace('  ', ' ')

async def write_code_example(file_path, category, module):
    code_example = generate_code_example(module)
    await asyncio.to_thread(file_path.write_text, f"# {module}\n\n{code_example}\n")
    print(f"Category: {category}, Module: {module}\n{code_example}\n")

def get_activation_script_path(venv_path):
    if os.name == 'nt':
        return f"{venv_path}\\Scripts\\activate"
    else:
        return f"{venv_path}/bin/activate"

async def process_module(category, module):
    base_dir = Path.cwd() / "standard_library_documents"
    category_dir = base_dir / safe_filename(category)
    category_dir.mkdir(parents=True, exist_ok=True)
    file_path = category_dir / f"{safe_filename(module)}.md"
    if file_path.exists():
        print(f"File {file_path} already exists. Skipping generation.")
        return
    print(f"Working on file: {file_path}")
    await write_code_example(file_path, category, module)

async def process_category(category, modules):
    tasks = [process_module(category, module) for module in modules]
    await asyncio.gather(*tasks)

async def main():
    tasks = [process_category(category, modules) for category, modules in standard_library.items()]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
