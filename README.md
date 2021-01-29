# TextHelper

### TextHelper can help you convert your text into uppercase or lowercase, and translate your text in any language into English

You can watch the [introduction video](https://youtu.be/GWdkXNxz8-8)

## Functions
>Function 1: Convertor

How to use it?

1. input your text in the `Text`
2. set the range of your text, which you want to convert. There are three chooses: `Full text`, `Only the first letter of every word`, `Only the first letter of every sentence`.
3. decide converting into uppercase or lowercase, by clicking the button of `From lowercase into uppercase` or `From uppercase into lowercase`

>Function 2: Translator

How to use it?

1. input your text in the `Text`
2. click the button of `Translate into English`, then you can get your translated text
```
Tips:
- the text you input can be in any language, and the translated text will be in English
- there is a google translate guider at the bottom of this webpage, you input your text here, this website will bring you to google translate website
```

## Relative links
1. [application](project/application.py)
2. [index](project/index.html)
3. [translator](project/translator.html)
4. [layout](project/layout.html)

# Commands
input `flask run` in the `Terminal` 
this link will bring you to the `Home` page of the TextHelper website
In the `Home` page, you can use the convertor, which helps you convert your text into lowercase or uppercase
If you want to use the translator, you need to click the `Translator`, which is nearby `Home`

# Details about this project
>The `application.py` includes all the functions, which realize the abilities of this project to convert or translate behind the webpages
>The `README.md` contains the introduction of this website, now you are reading it
>During the file of static, the `favicon.ico` shows the icon of this website, I drew this icon
>During the file of static, the `icon.bmp` shows the picture you can see at the top of the website
>During the file of static, the `styles.css` contains some details about the styles of the website
>During the file of templates, the `layout.html` shows us the overall style of this website
>During the file of templates, the `index.html`, in some degrees, maybe you can call it `convertor.html`, which includes the details about, what methods I used to get and show the text. The codes of this part are a little ugly, though it works well. I need to improve it in the future.
>During the file of templates, the `translator.html` includes both the getting the text users input and showing the translated text, and the guider, which sends the text users input to the google translate website, so the users are able to get the google translate outputs, in case, the users are unsure whether the translated results they get in this website are right or not
>Add: google changed the API before, so, I didn't apply the `googletrans`, but `google_trans_new`, which works well

# Ads of this project
- **Are you getting sick of clicking your keyboard again and again, just for converting your text into uppercase? TextHelper can help you solve this trouble!**
- **Only click twice, you can get a converted long text in 1 second! :+1: :+1: :+1:**
- **Have a try!**
