import os
from dotenv import load_dotenv

load_dotenv()
s = os.getenv('api')

print(s)
