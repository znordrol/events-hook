from secrets import choice
from base64 import b64decode

# https://discord.com/channels/305627343895003136/845532524724879380/907373349024432150
# https://discord.com/channels/747830885339889796/749030749591568484/792317725887168522

uwu_gif = [
    "https://c.tenor.com/U45Q8YaJzBUAAAAC/moti-hearts.gif",
    "https://c.tenor.com/HR1d8i8sGtQAAAAC/milk-and-mocha-bear-hearts.gif",
    "https://c.tenor.com/-yQr4mYAmL4AAAAC/lovely-cats.gif",
    "https://c.tenor.com/U7h-gyy--akAAAAC/kiss.gif",
    "https://c.tenor.com/ZvQzus4psfcAAAAC/kk.gif",
    "https://c.tenor.com/PvDVBj2mRcoAAAAC/mybc.gif",
    "https://c.tenor.com/lnP_tav2DVEAAAAC/love-cute.gif",
    "https://c.tenor.com/6pFkg0D_3W0AAAAC/cat-couple-cute-cats.gif",
    "https://c.tenor.com/AOdHdHyKcVYAAAAC/love-cute.gif",
    "https://c.tenor.com/EyrzkknfVPQAAAAC/bear-love.gif",
    "https://c.tenor.com/DJc6hVhbCpsAAAAC/milk-and-mocha-bears.gif",
    "https://c.tenor.com/LucJKXbuWyQAAAAC/peachcat-cat.gif",
]

closings = [
    "THV2IHlh",
    "WE9YTw==",
    "TG92ZSB5b3U=",
    "TWlzc2luZyB5b3UgZXZlcnkgbW9tZW50",
    "VGhpbmtpbmcgb2YgeW91",
    "V2l0aCBsb3Zl",
    "TG90cyBvZiBsb3Zl",
    "U3RpbGwgdGhpbmtpbmcgb2YgeW91",
    "TXVjaCBsb3Zl",
    "QWxsIG15IGxvdmU=",
    "QWx3YXlz",
    "U2VuZGluZyB5b3UgYWxsIG15IGxvdmU=",
    "WW91ciBkZXZvdGVkIGxvdmVy",
    "VGUgYW1v",
    "V28gYWkgbmk=",
    "SmUgdCdhaW1l",
    "SWNoIGxpZWJlIGRpY2g=",
    "T25lIHdobyBoYXMgYmVlbiBtZXNtZXJpemVk",
    "QWxsIG15IGhlYXJ0",
    "VGFra2FuIHBlcm5haCBjYXBlayBiaWxhbmcgaWx5",
    "TXVuZ2tpbiBpbmkgYWxheSwgdGFwaSBiaWFyaW4=",
    "S2FsbyBrbSBtZXJhc2EgaW5pIGFsYXksIGJpbGFuZyB5YXA=",
    "QXlhZmx1",
    "SSA8MyB5b3U=",
    "YWt1IHNheWFuZyBrbQ==",
    "SSB3dXYgeW91",
    "QnVsYW5ueWEgaW5kYWggeWE=",
]


def get_closings():
    return f"{b64decode(choice(closings)).decode()}, A."

def get_uwu_gif():
    return choice(uwu_gif)
