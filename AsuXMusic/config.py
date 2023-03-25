from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQCjW8Xp5XlIfzZ1mQxjvdqcDq-BTEIAJr2G5n5bp8N0Lcdp1LaLbiSswAWSruoPOwV6E5hhNnru50mHgx3GiZojDj3sH9kemFazFK3QmLMcVmMI9jPI9265tOO0viG-5fI-t2v1iX_QtCqP3qQ2TEKLQ-LlRmhXEwWyD5YcuwninXR7sokhcVq1NEflrscwK9nObEQAWcMQ7taIQp4Razv8VBFpLA5mMWX08U--BIX3JPd3JCNmH3ccmeNH1oPAUDXnUh1sHGTNJOpSurFtUYCF8WQceP-s7P7L9L2A3ZNv071uXTQwv5Ed57HeXYCz-iRgoGKBx3m2_2fYQGbKFXBLAAAAAXTVprUA")

BOT_TOKEN = getenv("BOT_TOKEN", "5848521215:AAGCG3fg80BSnQB2O3YCHzUkP5N-e1Yfvvo")
API_ID = int(getenv("API_ID", "23112604"))
API_HASH = getenv("API_HASH", "117564565390a7f9b970caecb521954e")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "@HISTORICAL_PLACE")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@HISTORICAL_PLACE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6063403084").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6063403084").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "160"))

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/31e9ecee16a46575267a4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d744707634106cf76627a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
