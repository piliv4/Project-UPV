import sys
import re
import os

def translate_Script(input_file):
    output_file = input_file.split('.')[0] + '_translated.txt'
    with open(input_file, encoding="utf8") as f:
        lines = f.read().splitlines() 

    formatted_lines = []
    speaker = ''
    prev_speaker = ''
    # Process each line as needed
    for line in lines:
        speakerPattern = r'^[a-zA-Z?]{2,3}:'
        formatted_line = ''

        if re.search(speakerPattern , line) :
            speaker = re.search(speakerPattern , line).group()
            text_only = parseMessageSpeaker(line.replace(speaker, "", 1).strip())

            formatted_line = parseSpeaker(speaker.upper()) + ' "' + text_only + '"' + '\n\n'

            if speaker == prev_speaker:
                formatted_lines[-1] = (formatted_lines[-1])[:-2] + '\n'
            prev_speaker = speaker
        else:
            if line != '':
                prev_speaker = '' 
                formatted_line = '#' + line +'\n\n'

        formatted_lines.append(formatted_line)

        with open(output_file, 'w') as f:
            for line in formatted_lines:
                f.write(line)

    return output_file

def parseSpeaker(speaker):
    speakerParsed = speaker.replace("PAN", "panero").replace("JL", "joseluis").replace("BZ", "bazooka").replace("MC", "mc").replace("???", "incognito").replace("GP", "# gp")
    speakerParsed = speakerParsed.replace(":", ".character")
    return speakerParsed

def parseMessageSpeaker(message):
    propertyPattern = r"\[([^\[\]]+)\s+([^\[\]]+)\]"
    wellFormedPattern = r'[!?).\]]$'
    messageParsed = message
    if re.search(propertyPattern , message):
        messageParsed = message.replace("[Lolero", "[joseluis").replace("[Pan", "[panero").replace("[bazooka", "bazooka").replace("[mc", "[mc")
        messageParsed = messageParsed.replace(" nombre]", ".name]")
    if not re.search(wellFormedPattern , messageParsed):
        messageParsed = messageParsed + "."
    return messageParsed


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Para usarlo: python traductor.py input_file ")
    else:
        input_file = sys.argv[1]
        # Check if the input file exists
        if not os.path.exists(input_file):
            print(f"The input file '{input_file}' does not exist.")
        else:
            output_file = translate_Script(input_file)
            print("Formatting complete. Output saved to", output_file)