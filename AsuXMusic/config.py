from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQBdsFFqBtgzu-1wWoZGsfwDzYhWXDvy_h_rNJGlnk_CuWzoGfwRrcAk11MtPzvOIdANKP502YXQgrX-L0rsQYgaBD6VD2mDuW7_w8haBnp9SEfIOAtZ62aYu4kwFEfIVvfD2lSPh9pnwaKZYzaCYDuchGd0reYCpeYcgK1gwd8B33addp9WNE0rMY6xeeNDEIPPOfHx5iEG9SgDwklZFx514g1zIocyyYKBWY9qrcgXQDhDQKyKoO7K8SM6P2oKn0wBqkRs-CXIA6yuiHEBrGlZKU8ZikiiSPLLMq4YBhoBm47Hqj1R91ZewBQ2gdTlZqbMcsyIZRA0i9xTnyXjtGAAAAAXTVprUA")

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
