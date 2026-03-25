from googletrans import Translator

translator = Translator()

text = input("Enter any sentence: ")
lang = input("Enter target language (e.g., 'ta', 'hi', 'fr'): ")

result = translator.translate(text, dest=lang)

print("Original:", text)
print("Translated:", result.text)
