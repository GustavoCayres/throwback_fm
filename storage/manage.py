#!/usr/bin/env python
import os

from migrate.versioning.shell import main

if __name__ == '__main__':
    main(repository='storage', url=os.environ["DATABASE_URL"], debug=os.environ["ENVIRONMENT"] == "DEVELOPMENT")
