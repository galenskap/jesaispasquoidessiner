<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Idées de sujets de dessin</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            <a href="/" class="btn reload">Mouais...</a>
        </div>
    </body>
</html>
