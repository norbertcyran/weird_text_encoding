## Weird text encoding
[![CircleCI](https://circleci.com/gh/cyranekpotasu/weird_text_encoding.svg?style=svg)](https://circleci.com/gh/cyranekpotasu/weird_text_encoding)

Text encoding - for each word in original text, the first and last character
stay the same and the rest is shuffled. Punctuation and whitespaces are not
touched.

### Install
1. Create .env file with `SECRET_KEY=<secret_key>` line
2. Install pipenv - `pip install pipenv`
3. Run `pipenv install`
4. `python manage.py runserver`

### Live

Application is hosted on [Heroku](https://weird-encoding-api.herokuapp.com).

### API documentation
For API documentation, please visit /docs endpoint.