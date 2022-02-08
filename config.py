import os

class Config(object):
  SECRET_KEY = 'very-hard-to-guess'
  MONGO_URI = "mongodb://localhost:27017/flask_guestbook"
  RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
  RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'