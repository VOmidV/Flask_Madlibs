"""Madlibs Stories."""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)



class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/')
def forFOr():
    return render_template("main.html", word=story.prompts)





@app.route('/story', methods = ['GET'])
def stor():
    first = request.args.get('place')
    sec = request.args.get('noun')
    third = request.args.get('verb')
    fourth = request.args.get('adjective')
    fifth = request.args.get('plural_noun')
    ans = {'place': first, 'noun': sec, 'verb': third, 'adjective': fourth, 'plural_noun': fifth}
    final = story.generate(ans)
    return render_template('story.html', post=final)

