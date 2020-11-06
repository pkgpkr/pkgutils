# Language support constants
JAVASCRIPT = 'javascript'
PYTHON = 'python'
JAVA = 'java'

JAVASCRIPT_DEPENDENCY_FNAME = 'package.json'
PYTHON_DEPENDENCY_FNAME = 'requirements.txt'
JAVA_DEPENDENCY_FNAME = 'pom.xml'

SUPPORTED_LANGUAGES = {JAVASCRIPT: {'dependencies_file': JAVASCRIPT_DEPENDENCY_FNAME, 'prefix': 'pkg:npm/'},
                       PYTHON: {'dependencies_file': PYTHON_DEPENDENCY_FNAME, 'prefix': 'pkg:pypi/'},
                       JAVA: {'dependencies_file': JAVA_DEPENDENCY_FNAME, 'prefix': 'pkg:maven/'}}

GITHUB_GRAPHQL_URL = 'https://api.github.com/graphql'