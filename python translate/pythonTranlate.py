from googletrans import Translator

convert  = Translator()
sentence  = "Hello World! \ni am Guido van Rossum"

exp = convert.translate(sentence, src = "en", dest = "tr",)
print(exp.text)

# Terminal ekranından çıktısını görebilirsiniz.