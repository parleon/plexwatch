import os

GYM_URL = "https://recconnect.bc.edu/Program/GetProgramDetails" \
          "?courseId=56cdcc01-554c-4513-80a8-222faf55d82c" \
          "&semesterId=3bcce1ac-dca7-4313-bc36-6f3c3bc3abed"

POOL_URL = "https://recconnect.bc.edu/Program/GetProgramDetails" \
           "?courseId=c1082af2-56d3-4ddf-a227-ab958c16bbee" \
           "&semesterId=3bcce1ac-dca7-4313-bc36-6f3c3bc3abed"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
number = '+19377050937'