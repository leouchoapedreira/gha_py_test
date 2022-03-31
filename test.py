import os

import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

TEST = os.getenv("TEST")

if TEST:
    print(f"TEST should be {TEST} in local")
else:
    TEST = os.environ["TEST"]
    print(f"TEST should be {TEST} in gha")


print(TEST)

