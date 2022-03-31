import os

import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

TEST = os.getenv("TEST")

print(TEST)

