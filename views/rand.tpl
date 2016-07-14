<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Idées de sujets de dessin</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel='stylesheet' id='customizr-skin-css'  href='static/styles.css?v=0.1' type='text/css' media='all' />
        <link href='https://fonts.googleapis.com/css?family=Lato:400,700' rel='stylesheet' type='text/css'>
    </head>
    <body>
        <div class="container">
            <h1>Je sais pas quoi dessiner ?</h1>
            <div class="reponse">
                %for texte in objet:
                    <span class="item objet">{{texte}}</span>
                %end
                %for texte in situation:
                    <span class="item situation">{{texte}}</span>
                %end
            </div>
            <a href="/" class="btn reload">mouais...</a>
        </div>
        <div class="social">
            <a class="github" href="https://github.com/galenskap/jesaispasquoidessiner" title="Get the code on Github">Github</a>
        </div>
    </body>
</html>
