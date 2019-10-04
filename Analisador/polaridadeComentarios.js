const vader = require('vader-sentiment');


function verificaPolaridadeNegativa(JsonComentarios){
    const polaridade =  vader.SentimentIntensityAnalyzer.polarity_scores(JsonComentarios);
}


const input = 'Had CamScanner for a long time and loved it; but now flagged by Norton as malicious. After some research, it contains library with malware. Please resolve this or refund my purchase!';
const intensity = vader.SentimentIntensityAnalyzer.polarity_scores(input);
if(intensity.neg > 0.5) console.log(intensity.neg);
