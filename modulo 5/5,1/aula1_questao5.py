
import emoji


emojis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

print("Emojis disponíveis:")
for emoticon, code in emojis.items():
    print(f"{emoticon} - {code}")

frase = input("Digite uma frase e ela será emojizada:\n")
frase_emojizada = emoji.emojize(frase)

print("Frase emojizada:")
print(frase_emojizada)
