from rtmbot import RtmBot
from rtmbot.core import Plugin

class HelloPlugin(Plugin):
    def process_message(self, data):
        if "애란" in data["text"]:
            self.outputs.append([data["channel"], "애란선생님 수업을 멈춰줘 (｡ŏ﹏ŏ)｡ "])
        if "배로" in data["text"]:
            self.outputs.append([data["channel"], "배로선생님 쉬는 시간 주세요 (ɷ ꒪ཀ꒪)ɷ "])
        if "정지"in data["text"]:
            self.outputs.append([data["channel"], "저는 항상 멈춰있어여 (*•̀ᴗ•́*)و "])
        if "댕댕" in data["text"]:
            self.outputs.append([data["channel"], "댕댕아 멈춰 🖐🏻"])
        if "냥" in data["text"]:
            self.outputs.append([data["channel"], "야옹아 멈춰 🖐🏻"])
        if "점심" in data["text"]:
            self.outputs.append([data["channel"], "다이어트를 멈추자🐷"])
        if "밥" in data["text"]:
            self.outputs.append([data["channel"], "크크킄ㅋ크배고파ㅏ아아ㅏ"])
        if "안녕" in data["text"]:
            self.outputs.append([data["channel"], "안녕하지 못해요.."])
        if "그만" in data["text"]:
            self.outputs.append([data["channel"], "부르셨어요? ٩(ˊᗜˋ*)و "])
        if "좋" in data["text"]:
            self.outputs.append([data["channel"], "침대가 제일 좋아..😴"])


        print(data)


config = {
    "SLACK_TOKEN": SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()


print("Hello world")
print("٩(๑`^´๑)۶ babo babo ٩(๑`^´๑)۶ ")
print("웅앵웅")
print("지금은 움직일 수 없습니다.")
