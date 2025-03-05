import requests
from dotenv import load_dotenv
import os

load_dotenv()
JUDGE0_IP = os.getenv('JUDGE0_IP')

payload = {
  "source_code": "#include <stdio.h>\n\nint main(void) {\n  char name[10];\n  scanf(\"%s\", name);\n  printf(\"hello, %s\n\", name);\n  return 0;\n}",
  "language_id": 52,
  "stdin": "world"
}
response = requests.get(JUDGE0_IP+'/languages')
response = requests.post(JUDGE0_IP+'/submissions', json=payload)
print(response.text)