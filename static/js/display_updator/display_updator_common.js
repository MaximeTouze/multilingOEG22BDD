// Fuction wich refreshes the main display
async function Updator() {
      while (continueUpdate) {
        display_update();
        await sleep(WAITING_TIME);
      }
}


// loads the sentences
async function loadSentences () {
  /*const elt = document.getElementById('displayPanel');

  for (var i = 0; i < sentences.length; i++) {
    sentence_rank = i;
    if (!document.getElementById(getSentenceId(sentence_rank))) {
      current_nb_sentence++;
      elt.innerHTML += GenerateSentence(sentences[i],  sentence_rank, getSentenceImgId(sentence_rank, true));
      if (current_nb_sentence > MAX_SENTENCES) {
        removeExtraSentence(sentence_rank);
      }
    }
  }*/

  clearDisplay();
  updateSentence (true);
}

// Update the word cloud
function wordCloud_update() {
  compteur++;
  imgName = selected_display + '.' + selected_language + '.' + IMG_TYPE;
  document.getElementById('displayPanel').style.backgroundImage = "url(../static/exposed/"+imgName + "?" + compteur+")"
}
