import os
from dotenv import load_dotenv

load_dotenv()
you = os.getenv('api')
print(you)
