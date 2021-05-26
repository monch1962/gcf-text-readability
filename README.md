# gcf-text-readability
Google Cloud Function to check text readability

## To deploy

`$ ./gcf-deploy.sh`

## To use

Send it a http POST with a JSON payload such as 
```
{
    "text": "This is the text I would like you to check for me"
}
```

and you should get a response back that looks something like
```
{
    "corrected_text": "This is the text I would like you to check for me",
    "errors_found": [],
    "original_text": "This is the text I would like you to check for me",
    "readability": 1.0
}
```
The `readability` number in the response corresponds to years of education, so a '9.0' would indicate year 9 of education.

### Spelling mistake correction

If you send it text with a spelling mistake such as 
```
{
    "text": "This text has a speling mistake"
}
```
you will get back something like
```
{
    "corrected_text": "This text has a spelling mistake",
    "errors_found": [
        "\"Offset 16, length 7, Rule ID: MORFOLOGIK_RULE_EN_AU\\nMessage: Possible spelling mistake found.\\nSuggestion: spelling; spewing; spieling\\nThis text has a speling mistake\\n                ^^^^^^^\""
    ],
    "original_text": "This text has a speling mistake",
    "readability": 2.0
}
```
Note that the mistake has been corrected, and an explanation of the text is also included

### Grammar error detection/correction

If you send it text with a punctuation error such as
```
{
    "text": "This text has a, grammatical mistake that makes it hard to read"
}
```
you will get back
```
{
    "corrected_text": "This text has a, grammatical mistake that makes it hard to read",
    "errors_found": ["\"Offset 14, length 2, Rule ID: THE_PUNCT\\nMessage: A word may be missing after \‘a\’.\\nThis text has a, grammatical mistake that makes it hard ...\\n              ^^\""
    ],
    "original_text": "This text has a, grammatical mistake that makes it hard to read",
    "readability": 6.0
}
```
Note that the mistake was detected and reported, but it was unable to fix it because it couldn't work out what the text should look like

