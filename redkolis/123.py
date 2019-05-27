import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
# <div data-qa="vacancy-serp__vacancy_snippet_responsibility"><resp></resp></div>
# <div data-qa="vacancy-serp__vacancy_snippet_requirement">Basic algorithms and data structures. Good knowledge of <span class="highlighted highlighted_short">Python</span>. Shell scripting is a plus. Knowledge of C, PHP, Perl and...</div>