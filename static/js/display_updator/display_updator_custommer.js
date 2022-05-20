// MOCKS
room = 1
//

function clearDisplay() {
  const elt = document.getElementById('displayPanel');
  elt.innerHTML = "";
}

function updateSentence (comeFromLoad = false) {
  $.ajax({
    type:'GET',
    url:'/sentences',
    data:{
      'nb_sentence':sentences.length,
      'room':room,
      'lang':selected_language
    },
    success:function(response)
    {
      if(comeFromLoad) {
        clearDisplay();
      }
      const elt = document.getElementById('displayPanel');
      const sentences_ = response.sentences;
      const keys = Object.keys(sentences_);

      for (var i = 0; i < keys.length; i++) {
        sentence_rank = keys[i];
        if (!document.getElementById(getSentenceId(sentence_rank))) {
          current_nb_sentence ++;
          elt.innerHTML += GenerateSentence(sentences_[sentence_rank],  sentence_rank, getSentenceImgId(sentence_rank, true));
          if (current_nb_sentence > MAX_SENTENCES) {
            removeExtraSentence(sentence_rank);
          }
        }
        //sentences = sentences.concat(sentences_[sentence_rank]);
      }
    }
 });
}

// function to load automatically the server
function updateTitle(){
  $.ajax({
    type: 'GET',
    url: '/confTitle',
    data: {},
    success: function(response){
      e = document.getElementById('title-conf')
      if (response.title != ''){
        console.log('1', e);
        if (e != null){
          console.log('2', e);
          e.innerHTML = response.title;
        } else {
          console.log('3', e);
          e = document.getElementById('noTitle-conf');
          e.id = 'title-conf';
          e.innerHTML = response.title;
        }
      } else if (e != null) {
        console.log('4', e);
        e.id = 'noTitle-conf';
      }
    }
  });
}



// Updates the display part
async function display_update () {
  //Ongoing on healthfull basis
  updateTitle();
  if (!updateUngoing || previous_display != selected_display) {
    updateUngoing = true;

    if(previous_display != selected_display) {
      document.getElementById('displayPanel').innerHTML = "";
      if(selected_display == SENTENCES ) {
        loadSentences();
      }
    }

    if(selected_display == WORD_CLOUD) {
      previous_display = WORD_CLOUD;
      wordCloud_update();

    } else if (selected_display == SENTENCES) {
      document.getElementById('displayPanel').style.backgroundImage ="" //Remove wordcloud if exists
      previous_display = SENTENCES;
      updateSentence();
   }
   updateUngoing = false;
  }
}



// remove the sentence if there are more than the MAX_SENTENCES limit
function removeExtraSentence(last_sentence_index) {
  // We count from 1, but ranks are from 0
  sentences = document.getElementsByClassName('sentence');
  while (sentences.length>  MAX_SENTENCES) {
    removeElement(sentences[0]);
    sentences = document.getElementsByClassName('sentence');
  }
  current_nb_sentence --;
}
