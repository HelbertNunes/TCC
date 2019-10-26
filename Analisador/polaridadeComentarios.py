from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer() 


comentarios = open("Z:\Playgroud\TCC\ComentariosSeparados.txt", "r", encoding="utf8")

arquivoComentariosPositivos = open("Z:\Playgroud\TCC\ComentariosPositivos.txt", "w" ,encoding="utf8")
arquivoComentariosNegativos = open("Z:\Playgroud\TCC\ComentariosNegativos.txt", "w", encoding="utf8")
arquivoComentariosNeutros = open("Z:\Playgroud\TCC\ComentariosNeutros.txt", "w", encoding="utf8")

def separaPolaridadeComentarios(sentence):
    score = analyser.polarity_scores(sentence)
    if score['neg'] > 0.5:
        arquivoComentariosNegativos.write(sentence)
    elif score['pos'] > 0.5:
        arquivoComentariosPositivos.write(sentence)
    elif score['neu'] > 0.5:
        arquivoComentariosNeutros.write(sentence)  


for line in comentarios:    
    separaPolaridadeComentarios(line)
    
arquivoComentariosPositivos.close()
arquivoComentariosNegativos.close()
arquivoComentariosNeutros.close()
    